import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def normalize_login_url(url):
    parsed = urlparse(url)

    return (
        f"{parsed.scheme}://"
        f"{parsed.netloc}"
        f"{parsed.path}"
    )


def scan_authentication(url):
    """
    Auth Scan v0.3.1 - Hybrid Authentication Surface Intelligence

    Layers:
    - Link-based discovery
    - Form-based discovery
    - Endpoint probing (generic + WordPress-safe fallback)
    - Validation engine
    """

    LOGIN_KEYWORDS = [
        "login",
        "log in",
        "sign in",
        "signin",
        "auth",
        "account"
    ]

    COMMON_LOGIN_PATHS = [
        "/wp-login.php",
        "/login",
        "/signin",
        "/admin",
        "/user/login"
    ]

    evidence = []
    detected = False
    login_urls = set()

    try:
        response = requests.get(url, timeout=20, allow_redirects=True)
        soup = BeautifulSoup(response.text, "html.parser")

        # ----------------------------
        # Step 1: Generic link discovery
        # ----------------------------
        for a_tag in soup.find_all("a"):

            href = a_tag.get("href")
            text = (a_tag.text or "").lower()

            if not href:
                continue

            full_url = urljoin(url, href)
            normalized_url = normalize_login_url(full_url)

            lower_href = href.lower()

            if any(keyword in lower_href or keyword in text for keyword in LOGIN_KEYWORDS):
                login_urls.add(normalized_url)

                evidence.append({
                    "method": "link",
                    "detail": f"Login link detected: {normalized_url}",
                    "url": normalized_url
                })

        # ----------------------------
        # Step 1.5: Endpoint probing
        # ----------------------------
        for path in COMMON_LOGIN_PATHS:

            probe_url = urljoin(url, path)

            try:
                r = requests.get(probe_url, timeout=5, allow_redirects=True)
                content = r.text.lower()

                if ("password" in content and "login" in content):
                    detected = True
                    login_urls.add(normalize_login_url(r.url))

                    evidence.append({
                        "method": "endpoint_probe",
                        "detail": f"Login endpoint confirmed at {r.url}",
                        "url": r.url
                    })

            except requests.RequestException:
                continue

        # ----------------------------
        # Step 2: Form-based discovery
        # ----------------------------
        for form in soup.find_all("form"):

            form_text = form.get_text().lower()
            inputs = form.find_all("input")

            has_password_field = any(
                i.get("type", "").lower() == "password"
                for i in inputs
            )

            if has_password_field:

                action = form.get("action", "")
                form_url = urljoin(response.url, action)

                login_urls.add(normalize_login_url(form_url))

                evidence.append({
                    "method": "form_discovery",
                    "detail": f"Login form detected at {form_url}",
                    "url": form_url
                })

        # ----------------------------
        # Step 3: Validation engine
        # ----------------------------
        for login_url in list(login_urls):

            try:
                r = requests.get(login_url, timeout=10, allow_redirects=True)
                content = r.text.lower()

                if (
                    "password" in content
                    and ("username" in content or "login" in content)
                ):
                    detected = True

                    evidence.append({
                        "method": "validation",
                        "detail": f"Login page confirmed at {r.url}",
                        "url": r.url
                    })

            except requests.RequestException as e:
                evidence.append({
                    "method": "error",
                    "detail": str(e),
                    "url": login_url
                })

        # ----------------------------
        # Step 4: fallback heuristic
        # ----------------------------
        if not login_urls:
            if "login" in response.text.lower():
                detected = True

                evidence.append({
                    "method": "fallback",
                    "detail": "Login keyword found in homepage (no explicit surface)",
                    "url": url
                })

        # ----------------------------
        # final cleanup
        # ----------------------------
        login_urls = [
            u for u in login_urls
            if any(x in u.lower() for x in ["login", "wp-login", "signin", "admin"])
        ]

        return {
            "login_page_found": detected,
            "login_urls": login_urls if login_urls else None,
            "final_url": response.url,
            "evidence": evidence,
            "error": None
        }

    except requests.RequestException as e:
        return {
            "login_page_found": False,
            "login_urls": None,
            "final_url": None,
            "evidence": [],
            "error": str(e)
        }