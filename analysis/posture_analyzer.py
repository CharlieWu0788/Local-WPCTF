def analyze_posture(
    coverage_result,
    risk_result
):
    """
    Overall security posture.
    """

    coverage = coverage_result.get(
        "coverage_score",
        0
    )

    critical = risk_result.get(
        "critical",
        0
    )

    high = risk_result.get(
        "high",
        0
    )

    if critical > 0:
        posture = "Weak"

    elif high >= 3:
        posture = "Weak"

    elif coverage < 50:
        posture = "Weak"

    elif coverage < 80:
        posture = "Moderate"

    else:
        posture = "Good"

    return {
        "security_posture": posture
    }