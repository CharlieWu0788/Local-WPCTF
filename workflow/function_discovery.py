from urllib.parse import urlparse


IGNORE_PATTERNS = [
    "#",
    "/#",
    "javascript:void(0)",
    ""
]


def is_valid_target(url):
    """
    Filter out fake / UI-only links
    """

    if not url:
        return False

    if url in IGNORE_PATTERNS:
        return False

    parsed = urlparse(url)

    # must have real path OR real endpoint
    if parsed.path in ["", "/"] and parsed.fragment:
        return False

    return True


def normalize_function_name(text):
    """
    Normalize UI text into function name
    """

    if not text:
        return "unknown"

    return text.lower().strip().replace(" ", "_")


def discover_functions(scan_results):
    """
    Extract meaningful application functions only
    """

    functions = []
    seen = set()

    auth = scan_results.get("auth", {})
    wp = scan_results.get("wordpress", {})

    # ---------------------------
    # Auth-based function
    # ---------------------------
    if auth.get("login_page_found"):
        for url in auth.get("login_urls") or []:

            if not is_valid_target(url):
                continue

            key = ("login", url)

            if key not in seen:
                functions.append({
                    "function": "login",
                    "target": url
                })
                seen.add(key)

    # ---------------------------
    # WordPress core function
    # ---------------------------
    if wp.get("wordpress_detected"):
        functions.append({
            "function": "wordpress_admin",
            "target": "wordpress_instance"
        })

    # ---------------------------
    # OPTIONAL: future extension hook
    # ---------------------------
    # (SQL / XSS / crawling can plug in here later)

    return functions