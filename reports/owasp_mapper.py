def classify_test_plan(test_plan):
    """
    Map generated test cases to OWASP Top 10 categories.
    """

    TEST_OWASP_MAP = {

        # A07
        "weak_password": (
            "A07",
            "Identification and Authentication Failures"
        ),

        "auth_bypass": (
            "A07",
            "Identification and Authentication Failures"
        ),

        "session_management": (
            "A07",
            "Identification and Authentication Failures"
        ),

        "username_enumeration": (
            "A07",
            "Identification and Authentication Failures"
        ),

        # A01
        "access_control": (
            "A01",
            "Broken Access Control"
        ),

        "workflow_bypass": (
            "A01",
            "Broken Access Control"
        ),

        # A03
        "stored_xss": (
            "A03",
            "Injection"
        ),

        "content_injection": (
            "A03",
            "Injection"
        ),

        "parameter_tampering": (
            "A03",
            "Injection"
        ),

        "price_manipulation": (
            "A03",
            "Injection"
        ),

        # A05
        "plugin_enumeration": (
            "A05",
            "Security Misconfiguration"
        ),

        "version_detection": (
            "A05",
            "Security Misconfiguration"
        ),

        "information_leakage": (
            "A05",
            "Security Misconfiguration"
        ),

        "sensitive_information_exposure": (
            "A05",
            "Security Misconfiguration"
        ),

        "user_disclosure": (
            "A05",
            "Security Misconfiguration"
        )
    }

    findings = []

    for task in test_plan:

        test_name = task["test"]

        if test_name not in TEST_OWASP_MAP:
            continue

        owasp_id, owasp_name = TEST_OWASP_MAP[test_name]

        findings.append({
            "target": task["target"],
            "test": test_name,
            "owasp_id": owasp_id,
            "owasp_name": owasp_name
        })

    return {
        "owasp": findings
    }