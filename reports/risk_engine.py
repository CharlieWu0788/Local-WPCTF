OWASP_WEIGHTS = {
    "A01": 1.0,  # Broken Access Control
    "A03": 0.9,  # Injection
    "A05": 0.7,  # Security Misconfiguration
    "A07": 0.8   # Auth Failures
}


def get_owasp_weight(owasp_id):
    return OWASP_WEIGHTS.get(owasp_id, 0.5)


def compute_risk_score(surface, owasp_results):
    """
    Risk Score Engine v0.5.4

    Final formula:
    risk = confidence × OWASP weight × impact factor
    """

    confidence = surface.get("confidence", 0.5)
    surface_type = surface.get("type", "")

    # -------------------------
    # 1. Base OWASP weight
    # -------------------------
    matched_owasp = [
        o for o in owasp_results
        if o.get("target") in surface.get("target", "")
    ]

    if matched_owasp:
        owasp_weight = max(
            get_owasp_weight(o.get("owasp_id", "A05"))
            for o in matched_owasp
        )
    else:
        owasp_weight = 0.5

    # -------------------------
    # 2. Business impact factor
    # -------------------------
    impact = 1.0

    if surface_type == "authentication":
        impact = 1.0
    elif surface_type == "business_function":
        impact = 1.3
    elif surface_type == "information_disclosure":
        impact = 0.9
    elif surface_type == "content_management":
        impact = 1.1
    else:
        impact = 0.8

    # -------------------------
    # 3. Final risk score
    # -------------------------
    risk = confidence * owasp_weight * impact

    return round(min(risk, 1.0), 2)


def rank_attack_surface(attack_surface, owasp_results):
    """
    Sort attack surface by risk score (descending)
    """

    for surface in attack_surface:
        surface["risk_score"] = compute_risk_score(surface, owasp_results)

    return sorted(
        attack_surface,
        key=lambda x: x["risk_score"],
        reverse=True
    )