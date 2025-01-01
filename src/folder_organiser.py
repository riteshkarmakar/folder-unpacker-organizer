import logging
from pathlib import Path


class FolderOrganiser:
    def __init__(self, root_path: str | Path) -> None:
        self.root_path = Path(root_path)
        self.validate_path(self.root_path)
        self.files_organised_count = 0
        self.folders_created_count = 0

    @staticmethod
    def validate_path(path: Path) -> None:
        """Validates that the root path exists and is a directory.

        Raises:
            FileNotFoundError: If the folder path does not exist.
            NotADirectoryError: If the specified path is not a directory.
        """
        if not path.exists():
            raise FileNotFoundError(f"Invalid Path: {path.as_posix()}")
        elif not path.is_dir():
            raise NotADirectoryError(f"Path is not a directory: {path.as_posix()}")
        
    def filter_files_by_extension(self, extensions: list[str]) -> list[Path]:
        """Finds and collects files from the specified folder that match the given extensions.

        Args:
            extensions (list[str]): A list of file extensions to match. The matching is case-insensitive.
        Returns:
            list[Path]: A list of Path objects representing the files that match the given extensions.
        """
        files_to_move = []
        for ext in extensions:
            for file_path in self.root_path.iterdir():
                if file_path.suffix.lower() == ext.lower():
                    files_to_move.append(file_path)
        return files_to_move

    def move_files(self, file_paths_lst: list[Path], folder_path: Path) -> None:
        """Moves specified files to a designated folder.

        Args:
            file_paths_lst (list[Path]): A list of file paths representing the files to be moved.
            folder_path (Path): The destination folder path where the files will be moved.
        """
        for file_path in file_paths_lst:

            target_path: Path = folder_path / file_path.name
            suffix = 0
            while target_path.exists():
                suffix += 1
                target_path = target_path.with_stem(f"{file_path.stem}_{suffix}")

            try:
                file_path.rename(target_path)
                self.files_organised_count += 1
                logging.info(f"{file_path.name!r} moved to {folder_path.name!r}")
            except Exception as e:
                logging.error(f"Failed to move {file_path.name!r} to {folder_path.name!r}: {e}")

    def organise_by_category(self, file_extensions_mapping: dict[str, list[str]]):
        """Organizes files in the specified folder by moving them into categorized subfolders based on their extensions."""

        logging.info(f"<b>Organising files to their respective category folders:</b>")
        for category, file_extensions in file_extensions_mapping.items():
            files_to_move = self.filter_files_by_extension(file_extensions)
            if not files_to_move:
                continue
            
            category_folder_path = self.root_path / category
            category_folder_path.mkdir(exist_ok=True)
            self.folders_created_count += 1
            self.move_files(files_to_move, category_folder_path)
