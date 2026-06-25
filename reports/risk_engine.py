OWASP_WEIGHTS = {
    "A01": 1.0,  # Broken Access Control
    "A03": 0.9,  # Injection
    "A05": 0.7,  # Security Misconfiguration
    "A07": 0.8   # Authentication Failures
}


def get_owasp_weight(owasp_id):
    return OWASP_WEIGHTS.get(owasp_id, 0.5)


def safe_str(x):
    """
    Normalize any input to safe string
    V1 Graph-safe utility
    """
    if x is None:
        return ""
    return str(x)


def extract_owasp_ids(owasp_results):
    """
    Normalize OWASP structure across V0/V1 formats
    """

    ids = []

    for o in owasp_results or []:

        # V1 format: {"owasp": ["A01", "A03"]}
        if isinstance(o.get("owasp"), list):
            ids.extend(o.get("owasp"))

        # fallback: single id
        elif o.get("owasp"):
            ids.append(o.get("owasp"))

        # legacy format
        elif o.get("owasp_id"):
            ids.append(o.get("owasp_id"))

    return ids


def compute_risk_score(surface, owasp_results):
    """
    Risk Score Engine V1

    risk = confidence × OWASP weight × impact factor
    """

    confidence = surface.get("confidence", 0.5)
    surface_type = surface.get("type", "")

    # -------------------------------------------------
    # 1. Normalize OWASP results
    # -------------------------------------------------
    owasp_ids = extract_owasp_ids(owasp_results)

    # -------------------------------------------------
    # 2. Match logic (V1 safe graph matching)
    # -------------------------------------------------
    surface_target = safe_str(surface.get("target"))

    matched_owasp = [
        oid for oid in owasp_ids
        if safe_str(oid) in surface_target or surface_target in safe_str(oid)
    ]

    if matched_owasp:
        owasp_weight = max(
            get_owasp_weight(oid) for oid in matched_owasp
        )
    else:
        owasp_weight = 0.5

    # -------------------------------------------------
    # 3. Business impact factor (unchanged logic)
    # -------------------------------------------------
    impact_map = {
        "authentication": 1.0,
        "business_function": 1.3,
        "information_disclosure": 0.9,
        "content_management": 1.1
    }

    impact = impact_map.get(surface_type, 0.8)

    # -------------------------------------------------
    # 4. Final score
    # -------------------------------------------------
    risk = float(confidence) * float(owasp_weight) * float(impact)

    return round(min(risk, 1.0), 2)


def rank_attack_surface(attack_surface, owasp_results):
    """
    Sort attack surface by risk score (descending)
    """

    if not attack_surface:
        return []

    for surface in attack_surface:
        surface["risk_score"] = compute_risk_score(surface, owasp_results)

    return sorted(
        attack_surface,
        key=lambda x: x.get("risk_score", 0),
        reverse=True
    )