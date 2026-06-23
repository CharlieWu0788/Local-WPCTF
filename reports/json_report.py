from datetime import datetime


def generate_report(
    target_url,
    attack_surface,
    test_plan,
    owasp_findings,
    coverage_result,
    risk_result,
    posture_result,
    dashboard_result
):
    """
    Generate standardized assessment report.
    """

    report = {
        "metadata": {
            "framework": "Local WPCTF",
            "version": "v0.6.0",
            "target": target_url,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        },

        "summary": {
            "attack_surface_count": len(
                attack_surface
            ),
            "test_count": len(
                test_plan
            ),
            "finding_count": len(
                owasp_findings
            )
        },

        "attack_surface": attack_surface,

        "test_plan": test_plan,

        "owasp": owasp_findings,

        "analytics": {

            "coverage": coverage_result,

            "risk_distribution": risk_result,

            "security_posture": posture_result,

            "dashboard": dashboard_result
}
    }

    return report