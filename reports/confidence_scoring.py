from urllib.parse import urlparse


def score_attack_surface(surface, auth_result=None):
    """
    Attack Surface Confidence Scoring v1.1.0

    Output: 0.0 ~ 1.0
    """

    score = 0.0

    surface_type = surface.get("type", "")
    target = surface.get("target", "")

    # --------------------------
    # 1. Authentication surface
    # --------------------------
    if surface_type == "authentication":

        # base score
        score += 0.3

        # strong signal: login url exists
        if target and "login" in target:
            score += 0.3

        # evidence boost
        if auth_result and auth_result.get("evidence"):
            score += 0.2

        # validation signal boost
        for e in (auth_result or {}).get("evidence", []):
            if e.get("method") == "validation":
                score += 0.2
                break

    # --------------------------
    # 2. WordPress surface
    # --------------------------
    elif surface_type == "wordpress":

        score += 0.2

        if "wp-login" in target or "wordpress" in target:
            score += 0.4

        score += 0.2  # heuristic default

    # --------------------------
    # 3. generic / unknown
    # --------------------------
    else:
        score += 0.1

    # --------------------------
    # normalization
    # --------------------------
    if score > 1.0:
        score = 1.0

    return round(score, 2)