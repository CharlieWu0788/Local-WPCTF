def validate_scan_results(scan_results):
    required_keys = ["wordpress", "auth", "sql", "xss"]

    for key in required_keys:
        if key not in scan_results:
            raise ValueError(f"[PIPELINE ERROR] Missing scan result: {key}")

    if not scan_results["auth"]:
        raise ValueError("[PIPELINE ERROR] auth_scan returned empty result")

    return True


def validate_functions(functions):
    if not isinstance(functions, list):
        raise ValueError("[PIPELINE ERROR] functions must be a list")

    if len(functions) == 0:
        raise ValueError("[PIPELINE ERROR] functions is empty")

    for f in functions:
        if "function" not in f or "target" not in f:
            raise ValueError(f"[PIPELINE ERROR] invalid function entry: {f}")

    return True


def validate_attack_surface(attack_surface):
    if not isinstance(attack_surface, list):
        raise ValueError("[PIPELINE ERROR] attack_surface must be a list")

    if len(attack_surface) == 0:
        raise ValueError("[PIPELINE ERROR] attack_surface is empty")

    for item in attack_surface:
        if "target" not in item:
            raise ValueError(f"[PIPELINE ERROR] missing target: {item}")
        if "possible_tests" not in item:
            raise ValueError(f"[PIPELINE ERROR] missing possible_tests: {item}")

    return True


def validate_test_plan(test_plan):
    if not isinstance(test_plan, list):
        raise ValueError("[PIPELINE ERROR] test_plan must be a list")

    if len(test_plan) == 0:
        raise ValueError("[PIPELINE ERROR] test_plan is empty")

    for t in test_plan:
        if "target" not in t and "surface_type" not in t:
            raise ValueError(f"[PIPELINE ERROR] invalid test_plan entry: {t}")

    return True


def validate_owasp(owasp_report, test_plan):
    if "owasp" not in owasp_report:
        raise ValueError("[PIPELINE ERROR] missing owasp field")

    if len(owasp_report["owasp"]) == 0:
        raise ValueError("[PIPELINE ERROR] empty owasp mapping")

    if len(owasp_report["owasp"]) != len(test_plan):
        print("[PIPELINE WARNING] OWASP mapping count != test_plan count")

    return True


# =========================
# 🧠 V0.5 FINAL: SEMANTIC CHECK
# =========================

def validate_semantic_integrity(functions, attack_surface, test_plan, owasp_report):
    
    function_targets = set([f["target"] for f in functions])

    surface_targets = set([a["target"] for a in attack_surface])

    test_targets = set([t["target"] for t in test_plan])

    owasp_targets = set([o["target"] for o in owasp_report["owasp"]])

    # 1. function → attack_surface coverage
    missing_from_surface = function_targets - surface_targets
    if missing_from_surface:
        print(f"[PIPELINE WARNING] functions not in attack_surface: {missing_from_surface}")

    # 2. attack_surface → test_plan coverage
    missing_from_test = surface_targets - test_targets
    if missing_from_test:
        print(f"[PIPELINE WARNING] attack_surface not in test_plan: {missing_from_test}")

    # 3. OWASP coverage check
    missing_from_owasp = test_targets - owasp_targets
    if missing_from_owasp:
        print(f"[PIPELINE WARNING] test_plan not in OWASP mapping: {missing_from_owasp}")

    return True


def validate_pipeline(scan_results, functions, attack_surface, test_plan, owasp_report):
    validate_scan_results(scan_results)
    validate_functions(functions)
    validate_attack_surface(attack_surface)
    validate_test_plan(test_plan)
    validate_owasp(owasp_report, test_plan)

    validate_semantic_integrity(functions, attack_surface, test_plan, owasp_report)

    print("[PIPELINE CHECKER] ✔ V0.5 Final Stable Check Passed")

    return True