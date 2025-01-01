# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTextEdit, QToolBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(700, 500))
        MainWindow.setMaximumSize(QSize(900, 700))
        icon = QIcon()
        icon.addFile(u":/icons/app_icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.action_run = QAction(MainWindow)
        self.action_run.setObjectName(u"action_run")
        icon1 = QIcon()
        icon1.addFile(u":/icons/run.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_run.setIcon(icon1)
        self.action_clear = QAction(MainWindow)
        self.action_clear.setObjectName(u"action_clear")
        icon2 = QIcon()
        icon2.addFile(u":/icons/clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_clear.setIcon(icon2)
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        icon3 = QIcon()
        icon3.addFile(u":/icons/exit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_exit.setIcon(icon3)
        self.action_read_documentation = QAction(MainWindow)
        self.action_read_documentation.setObjectName(u"action_read_documentation")
        self.action_check_for_updates = QAction(MainWindow)
        self.action_check_for_updates.setObjectName(u"action_check_for_updates")
        self.action_update_check_at_startup = QAction(MainWindow)
        self.action_update_check_at_startup.setObjectName(u"action_update_check_at_startup")
        self.action_update_check_at_startup.setCheckable(True)
        self.action_update_check_at_startup.setChecked(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, 15, 15, 15)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_organiser = QWidget()
        self.tab_organiser.setObjectName(u"tab_organiser")
        self.gridLayout_3 = QGridLayout(self.tab_organiser)
        self.gridLayout_3.setSpacing(15)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(15, 15, 15, 15)
        self.btn_browse = QPushButton(self.tab_organiser)
        self.btn_browse.setObjectName(u"btn_browse")
        self.btn_browse.setMinimumSize(QSize(110, 0))
        icon4 = QIcon()
        icon4.addFile(u":/icons/folder_open.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_browse.setIcon(icon4)

        self.gridLayout_3.addWidget(self.btn_browse, 0, 2, 1, 1)

        self.textedit_log = QTextEdit(self.tab_organiser)
        self.textedit_log.setObjectName(u"textedit_log")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textedit_log.sizePolicy().hasHeightForWidth())
        self.textedit_log.setSizePolicy(sizePolicy)
        self.textedit_log.setReadOnly(True)

        self.gridLayout_3.addWidget(self.textedit_log, 2, 1, 1, 1)

        self.label = QLabel(self.tab_organiser)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1, Qt.AlignRight)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.tab_organiser)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_files_moved_count = QLabel(self.tab_organiser)
        self.label_files_moved_count.setObjectName(u"label_files_moved_count")
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(20)
        self.label_files_moved_count.setFont(font)

        self.verticalLayout_2.addWidget(self.label_files_moved_count)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.tab_organiser)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.label_folder_created_count = QLabel(self.tab_organiser)
        self.label_folder_created_count.setObjectName(u"label_folder_created_count")
        self.label_folder_created_count.setFont(font)

        self.verticalLayout_4.addWidget(self.label_folder_created_count)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.tab_organiser)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_folder_deleted_count = QLabel(self.tab_organiser)
        self.label_folder_deleted_count.setObjectName(u"label_folder_deleted_count")
        self.label_folder_deleted_count.setFont(font)

        self.verticalLayout_3.addWidget(self.label_folder_deleted_count)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.gridLayout_3.addLayout(self.verticalLayout_5, 2, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkbox_unfolder = QCheckBox(self.tab_organiser)
        self.checkbox_unfolder.setObjectName(u"checkbox_unfolder")
        self.checkbox_unfolder.setMinimumSize(QSize(120, 0))

        self.verticalLayout.addWidget(self.checkbox_unfolder)

        self.checkbox_organise = QCheckBox(self.tab_organiser)
        self.checkbox_organise.setObjectName(u"checkbox_organise")
        self.checkbox_organise.setMinimumSize(QSize(120, 0))

        self.verticalLayout.addWidget(self.checkbox_organise)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_3.addLayout(self.verticalLayout, 2, 2, 1, 1)

        self.lineedit_folder_path = QLineEdit(self.tab_organiser)
        self.lineedit_folder_path.setObjectName(u"lineedit_folder_path")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineedit_folder_path.sizePolicy().hasHeightForWidth())
        self.lineedit_folder_path.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.lineedit_folder_path, 0, 1, 1, 1)

        self.line = QFrame(self.tab_organiser)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 3)

        self.tabWidget.addTab(self.tab_organiser, "")
        self.tab_settings = QWidget()
        self.tab_settings.setObjectName(u"tab_settings")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_settings)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(15, 15, 15, 15)
        self.groupbox_categories = QGroupBox(self.tab_settings)
        self.groupbox_categories.setObjectName(u"groupbox_categories")
        self.gridLayout = QGridLayout(self.groupbox_categories)
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(15, 15, 15, 15)
        self.lineedit_category = QLineEdit(self.groupbox_categories)
        self.lineedit_category.setObjectName(u"lineedit_category")

        self.gridLayout.addWidget(self.lineedit_category, 0, 0, 1, 2)

        self.listWidget_categories = QListWidget(self.groupbox_categories)
        self.listWidget_categories.setObjectName(u"listWidget_categories")

        self.gridLayout.addWidget(self.listWidget_categories, 1, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btn_add_category = QPushButton(self.groupbox_categories)
        self.btn_add_category.setObjectName(u"btn_add_category")
        icon5 = QIcon()
        icon5.addFile(u":/icons/add.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_add_category.setIcon(icon5)

        self.verticalLayout_6.addWidget(self.btn_add_category)

        self.btn_rename_category = QPushButton(self.groupbox_categories)
        self.btn_rename_category.setObjectName(u"btn_rename_category")
        icon6 = QIcon()
        icon6.addFile(u":/icons/edit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_rename_category.setIcon(icon6)

        self.verticalLayout_6.addWidget(self.btn_rename_category)

        self.btn_delete_category = QPushButton(self.groupbox_categories)
        self.btn_delete_category.setObjectName(u"btn_delete_category")
        icon7 = QIcon()
        icon7.addFile(u":/icons/delete.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_delete_category.setIcon(icon7)

        self.verticalLayout_6.addWidget(self.btn_delete_category)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)


        self.gridLayout.addLayout(self.verticalLayout_6, 1, 1, 1, 1)


        self.horizontalLayout_4.addWidget(self.groupbox_categories)

        self.groupbox_extensions = QGroupBox(self.tab_settings)
        self.groupbox_extensions.setObjectName(u"groupbox_extensions")
        self.gridLayout_2 = QGridLayout(self.groupbox_extensions)
        self.gridLayout_2.setSpacing(15)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(15, 15, 15, 15)
        self.lineedit_extension = QLineEdit(self.groupbox_extensions)
        self.lineedit_extension.setObjectName(u"lineedit_extension")

        self.gridLayout_2.addWidget(self.lineedit_extension, 0, 0, 1, 2)

        self.listWidget_extensions = QListWidget(self.groupbox_extensions)
        self.listWidget_extensions.setObjectName(u"listWidget_extensions")

        self.gridLayout_2.addWidget(self.listWidget_extensions, 1, 0, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btn_add_extension = QPushButton(self.groupbox_extensions)
        self.btn_add_extension.setObjectName(u"btn_add_extension")
        self.btn_add_extension.setIcon(icon5)

        self.verticalLayout_7.addWidget(self.btn_add_extension)

        self.btn_delete_extension = QPushButton(self.groupbox_extensions)
        self.btn_delete_extension.setObjectName(u"btn_delete_extension")
        self.btn_delete_extension.setIcon(icon7)

        self.verticalLayout_7.addWidget(self.btn_delete_extension)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)


        self.gridLayout_2.addLayout(self.verticalLayout_7, 1, 1, 1, 1)


        self.horizontalLayout_4.addWidget(self.groupbox_extensions)

        icon8 = QIcon()
        icon8.addFile(u":/icons/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.tab_settings, icon8, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QSize(50, 35))
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 800, 26))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menuBar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuPreferences = QMenu(self.menuBar)
        self.menuPreferences.setObjectName(u"menuPreferences")
        MainWindow.setMenuBar(self.menuBar)

        self.toolBar.addAction(self.action_run)
        self.toolBar.addAction(self.action_clear)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_exit)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuBar.addAction(self.menuPreferences.menuAction())
        self.menuFile.addAction(self.action_run)
        self.menuFile.addAction(self.action_exit)
        self.menuEdit.addAction(self.action_clear)
        self.menuHelp.addAction(self.action_read_documentation)
        self.menuHelp.addAction(self.action_check_for_updates)
        self.menuPreferences.addAction(self.action_update_check_at_startup)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.action_run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
#if QT_CONFIG(tooltip)
        self.action_run.setToolTip(QCoreApplication.translate("MainWindow", u"Run", None))
#endif // QT_CONFIG(tooltip)
        self.action_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
#if QT_CONFIG(tooltip)
        self.action_clear.setToolTip(QCoreApplication.translate("MainWindow", u"Clear", None))
#endif // QT_CONFIG(tooltip)
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(tooltip)
        self.action_exit.setToolTip(QCoreApplication.translate("MainWindow", u"Exit", None))
#endif // QT_CONFIG(tooltip)
        self.action_read_documentation.setText(QCoreApplication.translate("MainWindow", u"Read Documentation", None))
        self.action_check_for_updates.setText(QCoreApplication.translate("MainWindow", u"Check for Updates...", None))
        self.action_update_check_at_startup.setText(QCoreApplication.translate("MainWindow", u"Check for updates at startup", None))
        self.btn_browse.setText(QCoreApplication.translate("MainWindow", u" Browse", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Folder Path:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Total Files Organised:", None))
        self.label_files_moved_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Total Folders Created:", None))
        self.label_folder_created_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Total Folders Deleted:", None))
        self.label_folder_deleted_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.checkbox_unfolder.setText(QCoreApplication.translate("MainWindow", u"Unfolder", None))
        self.checkbox_organise.setText(QCoreApplication.translate("MainWindow", u"Organise", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_organiser), QCoreApplication.translate("MainWindow", u"Organiser", None))
        self.groupbox_categories.setTitle(QCoreApplication.translate("MainWindow", u"Categories", None))
        self.lineedit_category.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Category Name", None))
        self.btn_add_category.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.btn_rename_category.setText(QCoreApplication.translate("MainWindow", u"Rename", None))
        self.btn_delete_category.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.groupbox_extensions.setTitle(QCoreApplication.translate("MainWindow", u"Extensions", None))
        self.lineedit_extension.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Extension (example: .jpg)", None))
        self.btn_add_extension.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.btn_delete_extension.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_settings), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuPreferences.setTitle(QCoreApplication.translate("MainWindow", u"Preferences", None))
        pass
    # retranslateUi

