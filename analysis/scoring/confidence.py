"""
Confidence Scoring Module
- Measures reliability of attack surface detection
"""

def score_attack_surface(surface, auth_result=None):
    """
    Return confidence score: 0.0 - 1.0
    """

    score = 0.0

    surface_type = surface.get("type", "")
    target = surface.get("target", "")

    # --------------------------
    # Authentication surface
    # --------------------------
    if surface_type == "authentication":

        score += 0.3

        if target and "login" in target:
            score += 0.3

        if auth_result and auth_result.get("evidence"):
            score += 0.2

        for e in (auth_result or {}).get("evidence", []):
            if e.get("method") == "validation":
                score += 0.2
                break

    # --------------------------
    # WordPress surface
    # --------------------------
    elif surface_type == "wordpress":

        score += 0.2

        if "wp-login" in target or "wordpress" in target:
            score += 0.4

        score += 0.2

    # --------------------------
    # Generic
    # --------------------------
    else:
        score += 0.1

    return round(min(score, 1.0), 2)