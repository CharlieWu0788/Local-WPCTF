import os

IGNORE = {
    "__pycache__",
    ".pyc",
    ".venv",
    "venv",
    ".git",
    ".DS_Store"
}


def should_ignore(name: str) -> bool:
    return any(i in name for i in IGNORE)


def tree(dir_path, prefix=""):
    """
    Clean version of 'tree /f'
    """

    try:
        items = sorted(os.listdir(dir_path))
    except PermissionError:
        return

    items = [i for i in items if not should_ignore(i)]

    for i, item in enumerate(items):
        path = os.path.join(dir_path, item)

        connector = "└── " if i == len(items) - 1 else "├── "
        print(prefix + connector + item)

        if os.path.isdir(path):
            extension = "    " if i == len(items) - 1 else "│   "
            tree(path, prefix + extension)


if __name__ == "__main__":
    print("Clean Tree View (tree /f replacement)\n")
    print(".")
    tree(".")