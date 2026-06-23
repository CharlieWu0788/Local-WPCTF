from datetime import datetime


def generate_report(
    target_url,
    attack_surface,
    test_plan,
    owasp_findings,
    coverage_result,
    risk_result,
    posture_result,
    validation_results,
    validation_summary,
    exploitability_results,
    dashboard_result
):
    """
    Generate standardized assessment report.
    """

    return {
        "metadata": {
            "framework": "Local WPCTF",
            "version": "v0.7.1",
            "target": target_url,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        },

        "summary": {
            "attack_surface_count": len(attack_surface),
            "test_count": len(test_plan),
            "finding_count": len(owasp_findings),
            "validated_count": validation_summary.get("validated", 0),
            "high_risk_exploitability": len([
                x for x in exploitability_results
                if x.get("risk_level") == "high"
            ])
        },

        "attack_surface": attack_surface,
        "test_plan": test_plan,

        "validation_results": validation_results,
        "validation_summary": validation_summary,

        "exploitability_results": exploitability_results,

        "owasp": owasp_findings,

        "analytics": {
            "coverage": coverage_result,
            "risk_distribution": risk_result,
            "security_posture": posture_result,
            "dashboard": dashboard_result
        }
    }