import requests
from urllib.parse import urljoin


def scan_login_page(url):
    """
    Detect common WordPress authentication endpoints.

    Returns:
        {
            "login_page_found": bool,
            "login_url": str | None,
            "status_code": int | None,
            "evidence": list,
            "error": str | None
        }
    """

    LOGIN_PATHS = [
        "/wp-login.php",
        "/wp-admin"
    ]

    evidence = []

    for path in LOGIN_PATHS:

        target_url = urljoin(url, path)

        try:
            response = requests.get(
                target_url,
                allow_redirects=True,
                timeout=10
            )

            response_text = response.text.lower()

            if (
                "wordpress" in response_text
                and "login" in response_text
            ):
                evidence.append(
                    f"WordPress login page detected at {response.url}"
                )

                return {
                    "login_page_found": True,
                    "login_url": response.url,
                    "status_code": response.status_code,
                    "evidence": evidence,
                    "error": None
                }

            if "user_login" in response_text:
                evidence.append(
                    f"WordPress login form detected at {response.url}"
                )

                return {
                    "login_page_found": True,
                    "login_url": response.url,
                    "status_code": response.status_code,
                    "evidence": evidence,
                    "error": None
                }

        except requests.RequestException as e:
            evidence.append(
                f"Failed to access {target_url}: {str(e)}"
            )

    return {
        "login_page_found": False,
        "login_url": None,
        "status_code": None,
        "evidence": evidence,
        "error": None
    }