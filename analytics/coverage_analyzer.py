def analyze_coverage(attack_surface, test_plan):
    """
    V0.6 Coverage Analyzer

    Measures how many attack surfaces
    are covered by generated test cases.
    """

    surface_count = len(attack_surface)
    covered_count = min(len(test_plan), surface_count)

    coverage_score = 0

    if surface_count > 0:
        coverage_score = round(
            covered_count / surface_count * 100,
            2
        )

    return {
        "surface_count": surface_count,
        "covered_count": covered_count,
        "uncovered_count": max(
            surface_count - covered_count,
            0
        ),
        "coverage_score": coverage_score
    }