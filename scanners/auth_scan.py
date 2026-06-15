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
    Hybrid authentication page scanner:
    - Generic login discovery (CMS-agnostic)
    - Optional WordPress fallback detection
    """

    LOGIN_KEYWORDS = [
        "login",
        "log in",
        "sign in",
        "signin",
        "auth",
        "account"
    ]

    evidence = []
    detected = False
    login_urls = set()

    try:
        response = requests.get(url, timeout=10, allow_redirects=True)
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
            normalized_url = normalize_login_url(
                full_url
            )

            lower_href = href.lower()

            # keyword match in href or text
            if any(keyword in lower_href or keyword in text
                for keyword in LOGIN_KEYWORDS):
                    login_urls.add(normalized_url)

        # ----------------------------
        # Step 2: Validate candidates
        # ----------------------------
        for login_url in login_urls:

            try:
                r = requests.get(login_url, timeout=10, allow_redirects=True)
                content = r.text.lower()

                # generic login indicators
                if (
                    "password" in content
                    or "username" in content
                    or "login" in content
                    or "sign in" in content
                ):
                    detected = True
                    evidence.append(
                        f"Login page detected at {r.url}"
                    )

                # WordPress fallback heuristic (optional enhancement)
                if "wordpress" in content and "wp-login" in r.url:
                    evidence.append(
                        f"WordPress login endpoint confirmed at {r.url}"
                    )
                    detected = True

            except requests.RequestException as e:
                evidence.append(f"Failed to access {login_url}: {str(e)}")

        # ----------------------------
        # Step 3: direct fallback (light CMS heuristic)
        # ----------------------------
        if not login_urls:
            # fallback heuristic scan (still generic)
            if "login" in response.text.lower():
                evidence.append("Login keyword found in homepage content (no explicit link)")
                detected = True

        return {
            "login_page_found": detected,
            "login_urls": list(login_urls) if login_urls else None,
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