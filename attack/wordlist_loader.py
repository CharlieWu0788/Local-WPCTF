from typing import List


def load_wordlist(file_path: str) -> List[str]:
    """
    Load password wordlist
    """

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return [line.strip() for line in f if line.strip()]