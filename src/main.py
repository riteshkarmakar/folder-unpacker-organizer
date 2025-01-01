import sys, json, logging, requests
from pathlib import Path

from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog, QMessageBox, QInputDialog
from PySide6.QtGui import QRegularExpressionValidator, QDesktopServices
from PySide6.QtCore import QRegularExpression, QUrl

from ui.main_window import Ui_MainWindow
from ui import resources_rc

from folder_unpacker import FolderUnpacker
from folder_organiser import FolderOrganiser


CURRENT_VERSION = "v1.0.0"
PREFERENCES_PATH = Path("json/preferences.json")
EXTENSIONS_MAP_PATH = Path("json/extensions_map.json")
ABOUT_MESSAGE_PATH = Path("html/about_message.html")


class QTextEditLogger(logging.Handler):
    def __init__(self, text_edit: QTextEdit):
        super().__init__()
        self.text_edit = text_edit

    def emit(self, record):
        msg = self.format(record)
        self.text_edit.append(msg)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.preferences: dict = json.loads(PREFERENCES_PATH.read_text())
        self.file_extensions_map: dict[str, list[str]] = json.loads(EXTENSIONS_MAP_PATH.read_text())
        self.about_message = ABOUT_MESSAGE_PATH.read_text()
        self.init_ui()
        self.init_signals_slots()
        self.setup_logging()
        self.show()
        if self.action_update_check_at_startup.isChecked():
            self.check_for_updates()

    def init_ui(self) -> None:
        self.setWindowTitle(f"Folder Unpacker & Organizer {CURRENT_VERSION}")
        extension_validator = QRegularExpressionValidator(QRegularExpression(r"^\.[a-zA-Z0-9]{0,4}$"), self.lineedit_extension)
        self.lineedit_extension.setValidator(extension_validator)

        self.listWidget_categories.addItems(self.file_extensions_map.keys())
        self.listWidget_categories.sortItems()
        self.action_update_check_at_startup.setChecked(self.preferences.get("update_check_at_startup", True))

        self.textedit_log.setText(self.about_message)

    def init_signals_slots(self) -> None:
        self.action_run.triggered.connect(self.start_organising)
        self.action_exit.triggered.connect(self.close)
        self.action_clear.triggered.connect(self.clear)
        self.action_read_documentation.triggered.connect(
            lambda: QDesktopServices.openUrl(QUrl("https://github.com/riteshkarmakar/folder-unpacker-organizer/blob/master/README.md"))
        )
        self.action_check_for_updates.triggered.connect(self.check_for_updates)

        self.btn_browse.clicked.connect(self.browse_folder)

        self.listWidget_categories.currentRowChanged.connect(self.populate_extensions)
        self.btn_add_category.clicked.connect(self.add_category)
        self.btn_rename_category.clicked.connect(self.rename_category)
        self.btn_delete_category.clicked.connect(self.delete_category)

        self.btn_add_extension.clicked.connect(self.add_extension)
        self.btn_delete_extension.clicked.connect(self.delete_extension)

    def setup_logging(self):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        text_edit_handler = QTextEditLogger(self.textedit_log)
        formatter = logging.Formatter(fmt="%(asctime)s - %(message)s", datefmt="%d-%m-%Y %H:%M:%S")
        text_edit_handler.setFormatter(formatter)
        
        logger.addHandler(text_edit_handler)

    def save_settings(self) -> None:
        self.preferences["update_check_at_startup"] = self.action_update_check_at_startup.isChecked()
        PREFERENCES_PATH.write_text(json.dumps(self.preferences, indent="\t"))
        EXTENSIONS_MAP_PATH.write_text(json.dumps(self.file_extensions_map, indent="\t"))

    def closeEvent(self, event) -> None:
        self.save_settings()
        event.accept()

    def check_for_updates(self) -> None:
        url = f"https://api.github.com/repos/riteshkarmakar/folder-unpacker-organizer/releases/latest"
        try:
            response = None
            response = requests.get(url)
            response.raise_for_status()
        except:
            if self.sender() != self.action_check_for_updates:
                return
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setWindowTitle("Update Check Failed!")
            msg.setText("Unable to fetch update information.")
            msg.setInformativeText("Please check your internet connection or try again later.")
            msg.setDetailedText(f"Error code: {response.status_code if response != None else "None"}\nURL: {url}")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()
            return
        
        release_data = response.json()
        latest_version = release_data['tag_name']
        release_page_url = release_data['html_url']
        download_url = release_data['assets'][0]['browser_download_url']
        
        if latest_version > CURRENT_VERSION:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowTitle("Update Available")
            msg.setText(
                f"<h3>A New Version ({latest_version}) is Available!</h3>"
                f"To learn more about what's new, click 'View Details' below.</p>"
            )
            msg.setInformativeText("Would you like to update now?")
            msg.setStandardButtons(
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Help | QMessageBox.StandardButton.Cancel
            )
            msg.button(QMessageBox.StandardButton.Help).setText("View Details")
            
            # Open the download URL or View Details
            result = msg.exec()
            if result == QMessageBox.StandardButton.Yes:
                QDesktopServices.openUrl(QUrl(download_url))
            elif result == QMessageBox.StandardButton.Help:
                QDesktopServices.openUrl(QUrl(release_page_url))

        else:
            if self.sender() == self.action_check_for_updates:
                QMessageBox.information(
                    self, "No Update Available", f"You are currently using the latest version ({CURRENT_VERSION})"
                )

    def browse_folder(self) -> None:
        directory = QFileDialog.getExistingDirectory(self, "Select Folder")
        if directory:
            self.lineedit_folder_path.setText(directory)

    def clear(self) -> None:
        self.lineedit_folder_path.clear()
        self.lineedit_category.clear()
        self.lineedit_extension.clear()

        self.label_files_moved_count.setText("0")
        self.label_folder_created_count.setText("0")
        self.label_folder_deleted_count.setText("0")

        self.textedit_log.setText(self.about_message)

        self.checkbox_unfolder.setChecked(False)
        self.checkbox_organise.setChecked(False)

    def populate_extensions(self) -> None:
        row = self.listWidget_categories.currentRow()
        if row != -1:
            category = self.listWidget_categories.item(row).text()
            self.groupbox_extensions.setTitle(f"Extensions for {category}")
            self.listWidget_extensions.clear()
            self.listWidget_extensions.addItems(self.file_extensions_map[category])
            self.listWidget_extensions.sortItems()

    def is_duplicate_category(self, new_category: str) -> bool:
        for category in self.file_extensions_map:
            if new_category.lower() == category.lower():
                return True
        return False
    
    def is_duplicate_extension(self, new_extension: str) -> tuple[bool, str | None]:
        for category, extensions_lst in self.file_extensions_map.items():
            for extension in extensions_lst:
                if new_extension == extension:
                    return True, category
        return False, None

    def add_category(self) -> None:
        new_category = self.lineedit_category.text().strip()
        if new_category:
            if self.is_duplicate_category(new_category):
                QMessageBox.warning(
                    self, "Duplicate Category",
                    f"The category <b>{new_category!r}</b> already exists. Please enter a new category."
                )
            else:
                self.file_extensions_map[new_category] = []
                self.listWidget_categories.addItem(new_category)
                self.listWidget_categories.sortItems()
            self.lineedit_category.clear()

    def rename_category(self) -> None:
        category_item = self.listWidget_categories.currentItem()
        if not category_item:
            return
        
        renamed_category, response = QInputDialog.getText(
            self, "Rename Category", "New Category Name:", text=category_item.text()
        )
        if renamed_category.strip() and response:
            if self.is_duplicate_category(renamed_category):
                QMessageBox.warning(
                    self, f"Failed to rename {category_item.text()}",
                    f"The category <b>{renamed_category!r}</b> already exists. Please enter a new category name."
                )
            else:
                self.file_extensions_map[renamed_category] = self.file_extensions_map.pop(category_item.text())
                category_item.setText(renamed_category)
                self.listWidget_categories.sortItems()
    
    def delete_category(self) -> None:
        row = self.listWidget_categories.currentRow()
        category_item = self.listWidget_categories.currentItem()
        if category_item:
            if QMessageBox.question(
                self, "Confirmation", f"Are you sure you want to delete the category: <b>{category_item.text()!r}</b>?"
            ) == QMessageBox.StandardButton.Yes:
                del self.file_extensions_map[category_item.text()]
                self.listWidget_categories.takeItem(row)
    
    def add_extension(self) -> None:
        category_item = self.listWidget_categories.currentItem()
        new_extension = self.lineedit_extension.text().strip().lower()
        if category_item and new_extension:
            is_duplicate, category = self.is_duplicate_extension(new_extension)
            if is_duplicate:
                QMessageBox.warning(
                    self, "Duplicate Extension",
                    f"The extension: <b>{new_extension!r}</b> already exists under category: <b>{category!r}</b>. "
                    "Please enter a new extension."
                )
            else:
                self.file_extensions_map[category_item.text()].append(new_extension)
                self.listWidget_extensions.addItem(new_extension)
                self.listWidget_extensions.sortItems()
            self.lineedit_extension.clear()
        
    def delete_extension(self) -> None:
        row = self.listWidget_extensions.currentRow()
        extension_item = self.listWidget_extensions.currentItem()
        category_item = self.listWidget_categories.currentItem()
        if category_item and extension_item:
            index = self.file_extensions_map[category_item.text()].index(extension_item.text())
            del self.file_extensions_map[category_item.text()][index]
            self.listWidget_extensions.takeItem(row)

    def start_organising(self) -> None:
        self.save_settings()
        root_path = self.lineedit_folder_path.text().strip()

        warning_msg = ""
        if not root_path:
            warning_msg = f"No folder is selected. Please select a folder and try again."
        elif not self.checkbox_unfolder.isChecked() and not self.checkbox_organise.isChecked():
            warning_msg = f"No action is selected. Please select an action from the checkboxes and try again."
        if warning_msg:
            QMessageBox.warning(self, "Empty Fields!", warning_msg)
            return

        files_moved_count = 0
        folders_created_count = 0
        folders_deleted_count = 0

        self.textedit_log.clear()
        try:
            if self.checkbox_unfolder.isChecked():
                unfolder = FolderUnpacker(root_path)
                unfolder.move_files_to_root()
                unfolder.remove_empty_folders()
                files_moved_count += unfolder.files_moved_count
                folders_deleted_count += unfolder.folders_deleted_count

            if self.checkbox_organise.isChecked():
                organiser = FolderOrganiser(root_path)
                organiser.organise_by_category(self.file_extensions_map)
                files_moved_count += organiser.files_organised_count
                folders_created_count += organiser.folders_created_count
        except Exception as e:
            QMessageBox.warning(self, "Invalid Folder Path", str(e))
            self.lineedit_folder_path.clear()
            self.textedit_log.setText(self.about_message)

        self.label_files_moved_count.setText(str(files_moved_count))
        self.label_folder_created_count.setText(str(folders_created_count))
        self.label_folder_deleted_count.setText(str(folders_deleted_count))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("WindowsVista")
    window = MainWindow()
    sys.exit(app.exec())
