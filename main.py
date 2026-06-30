import os
import json
import argparse

from analysis.coverage_analyzer import analyze_coverage
from analysis.posture_analyzer import analyze_posture
from analysis.risk_analytics import analyze_risk
from analysis.validation_analytics import analyze_validation

from attack.brute_force_engine import WordPressBruteForceEngine
from attack.wordlist_loader import load_wordlist

from core.app_classifier import classify_application
from core.app_context import AppContext
from core.schema.safe_wrap import safe_scanner_result

from reports.json_report import generate_report

from scanners.auth_scan import scan_authentication
from scanners.sql_scan import scan_sql_injection
from scanners.wordpress_scan import scan_wordpress
from scanners.xss_scan import scan_xss

from scripts.tree_view import tree

from workflow.attack_surface import build_attack_surface
from workflow.test_plan import generate_test_plan


# =========================================================
# Args
# =========================================================
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="scan", choices=["scan", "tree"])
    return parser.parse_args()


# =========================================================
# Scanner Pipeline
# =========================================================
def run_scanners(url: str):
    """
    Execute all scanners.
    """

    return {
        "wordpress": safe_scanner_result(scan_wordpress(url)),
        "auth": safe_scanner_result(scan_authentication(url)),
        "sql": safe_scanner_result(scan_sql_injection(url)),
        "xss": safe_scanner_result(scan_xss(url))
    }


# =========================================================
# Bruteforce
# =========================================================
def run_bruteforce(url: str):
    """
    Legacy execution entry.

    TODO:
        Move execution decision into Workflow Execution Planner.
    """

    passwords = load_wordlist("wordlist.txt")

    engine = WordPressBruteForceEngine(
        target_url=url,
        username="admin",
        delay=0.3
    )

    return engine.attack(passwords)


# =========================================================
# Analysis Pipeline
# =========================================================
def run_analysis_pipeline(surface_list, test_tasks):
    """
    Execute analysis modules.
    """

    coverage = analyze_coverage(surface_list, test_tasks)
    risk = analyze_risk(surface_list)
    posture = analyze_posture(coverage, risk)
    validation = analyze_validation(test_tasks)

    return {
        "coverage": coverage,
        "risk": risk,
        "posture": posture,
        "validation": validation
    }


# =========================================================
# Main
# =========================================================
def main():

    args = get_args()

    # -----------------------------------------------------
    # Tree Mode
    # -----------------------------------------------------
    if args.mode == "tree":
        tree(".")
        return

    print("[*] Scan mode")

    # -----------------------------------------------------
    # Load Config
    # -----------------------------------------------------
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    url = config["target_url"]

    # -----------------------------------------------------
    # Scanner Pipeline
    # -----------------------------------------------------
    scan_results = run_scanners(url)

    # -----------------------------------------------------
    # Context
    # -----------------------------------------------------
    ctx = AppContext(url)

    for scanner_name, result in scan_results.items():
        ctx.add_scan_result(scanner_name, result)

    # -----------------------------------------------------
    # Classification
    # -----------------------------------------------------
    classification = classify_application(scan_results)

    ctx.set_app_type(classification["app_type"])
    ctx.set_classification(classification)

    ctx.update_metadata(
        "classification_confidence",
        classification["confidence"]
    )

    print(f"[*] App: {ctx.app_type}")

    # -----------------------------------------------------
    # Workflow
    # -----------------------------------------------------
    surface_result = build_attack_surface(scan_results)

    surface_list = surface_result["surface_list"]
    graph = surface_result["graph"]

    ctx.update_metadata("attack_graph", graph)

    test_tasks = generate_test_plan(surface_list)

    # -----------------------------------------------------
    # Attack (Temporary)
    # -----------------------------------------------------
    if (
        ctx.app_type == "wordpress"
        and "bruteforce" in classification["attack_suggestions"]
    ):
        print("[*] Running bruteforce...")

        bruteforce_result = run_bruteforce(url)

        ctx.add_analysis(
            "bruteforce",
            bruteforce_result
        )

    # -----------------------------------------------------
    # Analysis
    # -----------------------------------------------------
    analysis = run_analysis_pipeline(
        surface_list,
        test_tasks
    )

    for name, result in analysis.items():
        ctx.add_analysis(name, result)

    # -----------------------------------------------------
    # Report
    # -----------------------------------------------------
    report = generate_report(ctx.to_dict())

    os.makedirs("output", exist_ok=True)

    with open("output/report.json", "w", encoding="utf-8") as f:
        json.dump(
            report,
            f,
            indent=4,
            ensure_ascii=False
        )

    print("[+] Done -> output/report.json")


if __name__ == "__main__":
    main()