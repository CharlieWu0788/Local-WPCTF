"""
OWASP Top 10 Classification Module

Maps generated test plans to OWASP Top 10 categories.
"""


OWASP_MAPPING = {
    "weak_password": {
        "owasp_id": "A07",
        "owasp_name": "Identification and Authentication Failures"
    },

    "auth_bypass": {
        "owasp_id": "A07",
        "owasp_name": "Identification and Authentication Failures"
    },

    "session_management": {
        "owasp_id": "A07",
        "owasp_name": "Identification and Authentication Failures"
    },

    "sql_injection": {
        "owasp_id": "A03",
        "owasp_name": "Injection"
    },

    "xss": {
        "owasp_id": "A03",
        "owasp_name": "Injection"
    },

    "plugin_enumeration": {
        "owasp_id": "A05",
        "owasp_name": "Security Misconfiguration"
    },

    "version_detection": {
        "owasp_id": "A05",
        "owasp_name": "Security Misconfiguration"
    },

    "version_disclosure": {
        "owasp_id": "A05",
        "owasp_name": "Security Misconfiguration"
    }
}


def classify_test_plan(test_plan):
    """
    Converts test plan tasks into OWASP findings.

    Args:
        test_plan (list): Generated test plan.

    Returns:
        dict: OWASP classification report.
    """

    findings = []

    for task in test_plan:

        test_name = task.get("test")

        if test_name not in OWASP_MAPPING:
            continue

        mapping = OWASP_MAPPING[test_name]

        findings.append({
            "target": task.get("target"),
            "test": test_name,
            "owasp_id": mapping["owasp_id"],
            "owasp_name": mapping["owasp_name"]
        })

    return {
        "owasp": findings
    }