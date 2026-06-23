import requests
from bs4 import BeautifulSoup


def execute_auth_validation(task):
    """
    Safely validate authentication surface.
    """

    target = task["target"]

    result = {
        "surface_type": "auth",
        "target": target,
        "validated": False,
        "evidence": []
    }

    try:

        response = requests.get(
            target,
            timeout=5
        )

        if response.status_code == 200:

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            form = soup.find("form")

            if form:

                result["validated"] = True

                result["evidence"].append(
                    "Login form detected"
                )

                if form.get("action"):

                    result["evidence"].append(
                        f"Form action: {form.get('action')}"
                    )

    except Exception as e:

        result["evidence"].append(
            f"Validation error: {str(e)}"
        )

    return result