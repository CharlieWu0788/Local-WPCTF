import requests

def scan_login_page(url):
    try:
        response = requests.get(
            url,
            allow_redirects=True,
            timeout=10
        )

        final_url = response.url

        found = (
            "/wp-login.php" in final_url or
            "/wp-admin" in final_url
        )

        return {
            "login_page_found": found,
            "login_url": final_url if found else None,
            "status_code": response.status_code,
            "error": None
        }

    except requests.RequestException as e:
        return {
            "login_page_found": False,
            "login_url": None,
            "status_code": None,
            "error": str(e)
        }