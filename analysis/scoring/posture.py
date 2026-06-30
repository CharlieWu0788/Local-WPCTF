"""
Security Posture Analyzer
- Combines coverage + risk into overall posture
"""


def analyze_posture(coverage_result, risk_result):

    coverage_score = coverage_result.get("coverage_score", 0.0)
    avg_risk = risk_result.get("average_risk", 0.0)

    posture_score = (coverage_score * 0.5) + (avg_risk * 0.5)

    if posture_score > 0.7:
        level = "high_risk"
    elif posture_score > 0.4:
        level = "medium_risk"
    else:
        level = "low_risk"

    return {
        "posture_score": round(posture_score, 2),
        "level": level,
        "coverage_score": coverage_score,
        "average_risk": avg_risk
    }