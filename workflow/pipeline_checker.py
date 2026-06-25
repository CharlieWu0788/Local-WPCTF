def validate_scan_results(scan_results):
    required_keys = ["wordpress", "auth", "sql", "xss"]

    if not isinstance(scan_results, dict):
        raise ValueError("[PIPELINE ERROR] scan_results must be a dict")

    for key in required_keys:
        if key not in scan_results:
            raise ValueError(f"[PIPELINE ERROR] Missing scan result: {key}")

    return True


def validate_functions(functions):

    if not isinstance(functions, list):
        raise ValueError("[PIPELINE ERROR] functions must be a list")

    if len(functions) == 0:
        raise ValueError("[PIPELINE ERROR] functions is empty")

    return True


def validate_attack_surface(attack_surface):

    if not isinstance(attack_surface, list):
        raise ValueError("[PIPELINE ERROR] attack_surface must be a list")

    if len(attack_surface) == 0:
        raise ValueError("[PIPELINE ERROR] attack_surface is empty")

    return True


def validate_test_plan(test_plan):

    if not isinstance(test_plan, list):
        raise ValueError("[PIPELINE ERROR] test_plan must be a list")

    if len(test_plan) == 0:
        raise ValueError("[PIPELINE ERROR] test_plan is empty")

    return True


def validate_owasp(owasp_report, test_plan):

    if not isinstance(owasp_report, dict):
        raise ValueError("[PIPELINE ERROR] owasp_report must be a dict")

    if "owasp" not in owasp_report:
        raise ValueError("[PIPELINE ERROR] missing owasp field")

    if len(owasp_report["owasp"]) == 0:
        raise ValueError("[PIPELINE ERROR] empty owasp mapping")

    return True


def validate_semantic_integrity(
    functions,
    attack_surface,
    test_plan,
    owasp_report
):
    """
    V1 Semantic Integrity Validation
    """

    functions = functions or []
    attack_surface = attack_surface or []
    test_plan = test_plan or []
    owasp_report = owasp_report or {}

    function_targets = {
        str(f.get("target", ""))
        for f in functions
        if isinstance(f, dict) and f.get("target")
    }

    surface_targets = {
        str(a.get("target", ""))
        for a in attack_surface
        if isinstance(a, dict) and a.get("target")
    }

    test_targets = {
        str(t.get("target", ""))
        for t in test_plan
        if isinstance(t, dict) and t.get("target")
    }

    owasp_targets = set()

    for item in owasp_report.get("owasp", []):

        if not isinstance(item, dict):
            continue

        if item.get("target"):
            owasp_targets.add(str(item["target"]))

        elif item.get("path"):
            owasp_targets.update(
                str(node)
                for node in item.get("path", [])
            )

    missing_from_surface = function_targets - surface_targets

    if missing_from_surface:
        print(
            "[PIPELINE WARNING] functions not in attack_surface: "
            f"{missing_from_surface}"
        )

    missing_from_test = surface_targets - test_targets

    if missing_from_test:
        print(
            "[PIPELINE WARNING] attack_surface not in test_plan: "
            f"{missing_from_test}"
        )

    if owasp_targets:
        missing_from_owasp = test_targets - owasp_targets

        if missing_from_owasp:
            print(
                "[PIPELINE WARNING] test_plan not in OWASP mapping: "
                f"{missing_from_owasp}"
            )

    return True


def validate_pipeline(
    scan_results,
    functions,
    attack_surface,
    test_plan,
    owasp_report
):

    validate_scan_results(scan_results)
    validate_functions(functions)
    validate_attack_surface(attack_surface)
    validate_test_plan(test_plan)
    validate_owasp(owasp_report, test_plan)
    validate_semantic_integrity(
        functions,
        attack_surface,
        test_plan,
        owasp_report
    )

    print(
        "[PIPELINE CHECKER] ✔ V1 Semantic Validation Passed"
    )

    return True