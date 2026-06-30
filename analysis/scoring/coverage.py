"""
Coverage Analyzer
- Measures how much of attack surface is tested
"""


def analyze_coverage(attack_surface, test_plan):

    if not attack_surface:
        return {
            "coverage_score": 0.0,
            "covered": 0,
            "total": 0
        }

    total = len(attack_surface)

    tested_targets = set()

    for test in test_plan or []:
        target = test.get("target")
        if target:
            tested_targets.add(target)

    covered = 0

    for surface in attack_surface:
        if surface.get("target") in tested_targets:
            covered += 1

    coverage_score = covered / total if total else 0.0

    return {
        "coverage_score": round(coverage_score, 2),
        "covered": covered,
        "total": total
    }