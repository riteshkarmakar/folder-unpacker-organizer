import logging
from pathlib import Path


class FolderUnpacker:
    def __init__(self, root_path: str | Path):
        self.root_path = Path(root_path)
        self.validate_path(self.root_path)
        self.empty_folders: list[Path] = []
        self.files_moved_count = 0
        self.folders_deleted_count = 0

    @staticmethod
    def validate_path(path: Path) -> None:
        """Validates that the root path exists and is a directory.

        Raises:
            FileNotFoundError: If the folder path does not exist.
            NotADirectoryError: If the specified path is not a directory.
        """
        if not path.exists():
            raise FileNotFoundError(f"Invalid Path: {path.as_posix()!r}")
        elif not path.is_dir():
            raise NotADirectoryError(f"Path is not a directory: {path.as_posix()!r}")

    def move_files_to_root(self) -> list[Path]:
        """Moves all files in subdirectories to the root directory.

        Returns:
            list[Path]: A list of empty directories pending deletion.
        """
        logging.info(f"<b>Moving files to the root directory:</b> {self.root_path.name!r}")
        for path in self.root_path.rglob("*"):
            if path.is_file() and path.parent != self.root_path:

                target_path = self.root_path / path.name
                suffix = 0
                while target_path.exists():
                    suffix += 1
                    target_path = target_path.with_stem(f"{path.stem}_{suffix}")

                try:
                    path.rename(target_path)
                    self.files_moved_count += 1
                    logging.info(f"{path.name!r} moved to {self.root_path.name!r}")
                except Exception as e:
                    logging.error(f"Failed to move {path.name!r} to {self.root_path.name!r}: {e}")
                    
            elif path.is_dir():
                self.empty_folders.append(path)

    def remove_empty_folders(self) -> int:
        """Removes empty directories from the provided list.

        Args:
            directories (list[Path]): A list of directories to be deleted if empty.
        """
        logging.info(f"<b>Deleting empty folders</b>")
        for directory in self.empty_folders:
            try:
                directory.rmdir()
                logging.info(f"Deleted empty folder: {directory.name!r}")
                self.folders_deleted_count += 1
            except Exception as e:
                logging.error(f"Failed to delete {directory.name!r}: {e}")
