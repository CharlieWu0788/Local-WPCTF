import requests


def execute_sql_validation(task):
    """
    Safe SQL interaction validation (V1.0.1 schema-safe)
    """

    target = task.get("target", "")

    result = {
        "surface_type": "sql",
        "target": target,
        "validated": False,
        "evidence": [],
        "error": None
    }

    try:
        response1 = requests.get(
            target,
            params={"id": 1},
            timeout=5
        )

        response2 = requests.get(
            target,
            params={"id": 2},
            timeout=5
        )

        if response1.status_code == 200 and response2.status_code == 200:

            result["validated"] = True
            result["evidence"].append("Parameter responded")

            if len(response1.text) != len(response2.text):
                result["evidence"].append("Content length variation detected")

    except Exception as e:
        result["error"] = str(e)

    return result