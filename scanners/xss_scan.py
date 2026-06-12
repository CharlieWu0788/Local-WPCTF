import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def scan_xss(url):
    """
    Basic reflected XSS scanner.

    Returns:
        {
            "xss_detected": bool,
            "evidence": list,
            "tested_payloads": list
        }
    """

    PAYLOADS = [
        "<script>alert(1)</script>",
        "\"><script>alert(1)</script>",
        "<img src=x onerror=alert(1)>"
    ]

    evidence = []
    detected = False

    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        forms = soup.find_all("form")

        if not forms:
            return {
                "xss_detected": False,
                "evidence": ["No forms discovered"],
                "tested_payloads": PAYLOADS
            }

        evidence.append(f"Discovered {len(forms)} form(s)")

        for form in forms:

            action = form.get("action")
            method = form.get("method", "get").lower()

            target_url = urljoin(url, action) if action else url

            evidence.append(
                f"Testing form at {target_url} using {method.upper()}"
            )

            inputs = form.find_all(["input", "textarea"])

            for payload in PAYLOADS:

                form_data = {}

                for field in inputs:

                    name = field.get("name")

                    if not name:
                        continue

                    field_type = field.get("type", "text").lower()

                    if field_type in [
                        "text",
                        "search",
                        "email",
                        "url",
                        "hidden",
                        "textarea"
                    ]:
                        form_data[name] = payload
                    else:
                        form_data[name] = "test"

                try:

                    if method == "post":
                        test_response = requests.post(
                            target_url,
                            data=form_data,
                            timeout=5
                        )
                    else:
                        test_response = requests.get(
                            target_url,
                            params=form_data,
                            timeout=5
                        )

                    response_text = test_response.text

                    if payload in response_text:

                        detected = True

                        evidence.append(
                            f"Unescaped payload reflected at {target_url}"
                        )

                    elif "alert(1)" in response_text:

                        evidence.append(
                            f"Payload content reflected but appears encoded at {target_url}"
                        )

                except requests.RequestException as e:

                    evidence.append(
                        f"Request failed for {target_url}: {str(e)}"
                    )

        return {
            "xss_detected": detected,
            "evidence": list(set(evidence)),
            "tested_payloads": PAYLOADS
        }

    except requests.RequestException as e:

        return {
            "xss_detected": False,
            "evidence": [f"Initial request failed: {str(e)}"],
            "tested_payloads": PAYLOADS
        }