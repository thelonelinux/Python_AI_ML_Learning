"""File_Handling: read and write files using the built-in open API."""

from pathlib import Path


def write_text_file(path: str, content: str) -> None:
    """Write text content to a file."""
    with open(path, "w", encoding="utf-8") as file_handle:
        file_handle.write(content)


def append_text_file(path: str, content: str) -> None:
    """Append text to an existing file."""
    with open(path, "a", encoding="utf-8") as file_handle:
        file_handle.write(content)


def read_text_file(path: str) -> str:
    """Read file contents as a string."""
    with open(path, "r", encoding="utf-8") as file_handle:
        return file_handle.read()


def pathlib_example(directory: str):
    """Use pathlib to create directories and inspect file paths."""
    path = Path(directory)
    path.mkdir(parents=True, exist_ok=True)
    file_path = path / "pathlib_example.txt"
    file_path.write_text("Pathlib example content\n", encoding="utf-8")
    return file_path.read_text(encoding="utf-8")


if __name__ == "__main__":
    filename = "file_handling_example.txt"
    write_text_file(filename, "Hello, file handling!\n")
    append_text_file(filename, "This line is appended.\n")
    print("File contents:\n", read_text_file(filename))
    print("Pathlib read/write result:\n", pathlib_example("file_demo_dir"))
