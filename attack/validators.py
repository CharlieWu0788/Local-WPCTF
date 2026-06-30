from requests import Response


def is_login_success(response: Response) -> bool:
    """
    Smart WordPress login success detection
    """

    # 1. redirect to admin panel
    if "wp-admin" in response.url:
        return True

    # 2. login cookie appears
    if "wordpress_logged_in" in response.cookies.get_dict():
        return True

    # 3. typical failure message check
    if "ERROR" in response.text and "incorrect" in response.text.lower():
        return False

    # 4. heuristic: WordPress often returns 200 even on failure
    if "wp-login.php" in response.url and "dashboard" not in response.text:
        return False

    return False