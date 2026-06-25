def analyze_coverage(attack_surface, test_plan):
    """
    V1.0.1 Coverage Analyzer (schema-safe)
    """

    attack_surface = attack_surface or []
    test_plan = test_plan or []

    surface_count = len(attack_surface)
    covered_count = min(len(test_plan), surface_count)

    coverage_score = 0

    if surface_count > 0:
        coverage_score = round(
            covered_count / surface_count * 100,
            2
        )

    result = {
        "surface_count": surface_count,
        "covered_count": covered_count,
        "uncovered_count": max(surface_count - covered_count, 0),
        "coverage_score": coverage_score
    }

    return result