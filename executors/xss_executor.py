import requests


def execute_xss_validation(task):
    """
    Safe reflection validation (V1.0.1 schema-safe)
    """

    target = task.get("target", "")
    marker = "WPCTF_TEST"

    result = {
        "surface_type": "xss",
        "target": target,
        "validated": False,
        "evidence": [],
        "error": None
    }

    try:
        response = requests.get(
            target,
            params={"q": marker},
            timeout=5
        )

        if marker in response.text:
            result["validated"] = True
            result["evidence"].append("Input reflected in response")

    except Exception as e:
        result["error"] = str(e)

    return result