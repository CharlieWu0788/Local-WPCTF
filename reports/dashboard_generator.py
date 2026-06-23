def generate_dashboard(
    coverage_result,
    risk_result,
    posture_result
):
    """
    Generate executive summary dashboard.
    """

    return {
        "coverage_score":
            coverage_result.get(
                "coverage_score",
                0
            ),

        "overall_risk":
            risk_result,

        "security_posture":
            posture_result.get(
                "security_posture",
                "Unknown"
            )
    }