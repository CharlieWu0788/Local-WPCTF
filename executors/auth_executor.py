import requests
from bs4 import BeautifulSoup


def execute_auth_validation(task):
    """
    Safely validate authentication surface (V1.0.1 schema-safe)
    """

    target = task.get("target", "")

    result = {
        "surface_type": "auth",
        "target": target,
        "validated": False,
        "evidence": [],
        "error": None
    }

    try:
        response = requests.get(
            target,
            timeout=5
        )

        if response.status_code == 200:

            soup = BeautifulSoup(response.text, "html.parser")
            form = soup.find("form")

            if form:

                result["validated"] = True
                result["evidence"].append("Login form detected")

                action = form.get("action")
                if action:
                    result["evidence"].append(f"Form action: {action}")

    except Exception as e:
        result["error"] = str(e)

    return result