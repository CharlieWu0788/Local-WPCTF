"""
Risk Scoring Engine
- OWASP weighted risk computation
"""

OWASP_WEIGHTS = {
    "A01": 1.0,
    "A03": 0.9,
    "A05": 0.7,
    "A07": 0.8
}


def get_owasp_weight(owasp_id):
    return OWASP_WEIGHTS.get(owasp_id, 0.5)


def safe_str(x):
    return "" if x is None else str(x)


def extract_owasp_ids(owasp_results):
    ids = []

    for o in owasp_results or []:

        if isinstance(o.get("owasp"), list):
            ids.extend(o.get("owasp"))

        elif o.get("owasp"):
            ids.append(o.get("owasp"))

        elif o.get("owasp_id"):
            ids.append(o.get("owasp_id"))

    return ids


def compute_risk_score(surface, owasp_results):

    confidence = surface.get("confidence", 0.5)
    surface_type = surface.get("type", "")

    owasp_ids = extract_owasp_ids(owasp_results)

    surface_target = safe_str(surface.get("target"))

    matched = [
        oid for oid in owasp_ids
        if safe_str(oid) in surface_target or surface_target in safe_str(oid)
    ]

    if matched:
        owasp_weight = max(get_owasp_weight(i) for i in matched)
    else:
        owasp_weight = 0.5

    impact_map = {
        "authentication": 1.0,
        "business_function": 1.3,
        "information_disclosure": 0.9,
        "content_management": 1.1
    }

    impact = impact_map.get(surface_type, 0.8)

    risk = confidence * owasp_weight * impact

    return round(min(risk, 1.0), 2)


def rank_attack_surface(attack_surface, owasp_results):

    ranked = []

    for surface in attack_surface:
        item = dict(surface)
        item["risk_score"] = compute_risk_score(surface, owasp_results)
        ranked.append(item)

    return sorted(ranked, key=lambda x: x.get("risk_score", 0), reverse=True)