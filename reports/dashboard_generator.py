def generate_dashboard(
    coverage_result,
    risk_result,
    posture_result,
    validation_summary,
    exploitability_results
):
    """
    Generate executive security dashboard.
    """

    high = len([
        x for x in exploitability_results
        if x.get("risk_level") == "high"
    ])

    medium = len([
        x for x in exploitability_results
        if x.get("risk_level") == "medium"
    ])

    low = len([
        x for x in exploitability_results
        if x.get("risk_level") == "low"
    ])

    return {
        "coverage_score": coverage_result.get("coverage_score", 0),

        "validation_score": validation_summary.get("validation_score", 0),

        "validated_findings": validation_summary.get("validated", 0),
        "failed_validations": validation_summary.get("failed", 0),
        "untested_items": validation_summary.get("untested", 0),

        "exploitability_risk": {
            "high": high,
            "medium": medium,
            "low": low
        },

        "overall_risk": risk_result,

        "security_posture": posture_result.get("security_posture", "Unknown")
    }