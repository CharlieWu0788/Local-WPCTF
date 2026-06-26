import os
import json
import argparse

from analysis.coverage_analyzer import analyze_coverage
from analysis.posture_analyzer import analyze_posture
from analysis.risk_analytics import analyze_risk
from analysis.validation_analytics import analyze_validation

from core.app_classifier import classify_application
from core.app_context import AppContext

from core.schema.safe_wrap import safe_scanner_result

from reports.dashboard_generator import generate_dashboard
from reports.json_report import generate_report
from reports.owasp_mapper import classify_test_plan
from reports.risk_engine import rank_attack_surface

from scanners.auth_scan import scan_authentication
from scanners.sql_scan import scan_sql_injection
from scanners.wordpress_scan import scan_wordpress
from scanners.xss_scan import scan_xss

from tools.tree_view import tree

from workflow.attack_surface import build_attack_surface
from workflow.exploit_simulation import run_exploitability_analysis
from workflow.exploit_path_engine import ExploitPathEngine
from workflow.function_discovery import discover_functions
from workflow.pipeline_checker import validate_pipeline
from workflow.test_plan import generate_test_plan
from workflow.validation_execution import execute_validation


# =========================================================
# Runtime Arguments
# =========================================================
def get_args():
    parser = argparse.ArgumentParser(description="Local WPCTF Runtime Engine")

    parser.add_argument(
        "--mode",
        default="scan",
        choices=["scan", "tree"],
        help="Runtime mode: scan or tree view"
    )

    return parser.parse_args()


# =========================================================
# Main Entry
# =========================================================
def main():

    # -------------------------
    # Parse runtime args
    # -------------------------
    args = get_args()

    # -------------------------
    # Tree Mode (fast exit)
    # -------------------------
    if args.mode == "tree":
        print("[*] Running Tree View Mode")
        tree(".")
        return

    # -------------------------
    # Scan Mode
    # -------------------------
    print("[*] Running Scan Mode")

    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    url = config["target_url"]

    print(f"[*] Target: {url}")

    # =========================================================
    # Scanners
    # =========================================================
    print("[*] Running WordPress detection...")
    wordpress_result = safe_scanner_result(scan_wordpress(url))

    print("[*] Running authentication scan...")
    auth_result = safe_scanner_result(scan_authentication(url))

    print("[*] Running SQL reconnaissance...")
    sql_result = safe_scanner_result(scan_sql_injection(url))

    print("[*] Running XSS reconnaissance...")
    xss_result = safe_scanner_result(scan_xss(url))

    scan_results = {
        "wordpress": wordpress_result,
        "auth": auth_result,
        "sql": sql_result,
        "xss": xss_result
    }

    # =========================================================
    # App Classification
    # =========================================================
    print("[*] Classifying application...")

    app_type = classify_application(scan_results)

    print(f"[*] Application Type: {app_type}")

    # =========================================================
    # App Context
    # =========================================================
    print("[*] Building application context...")

    app_context = AppContext(url)
    app_context.set_app_type(app_type)

    # Store scan results
    app_context.add_scan_result("wordpress", wordpress_result)
    app_context.add_scan_result("auth", auth_result)
    app_context.add_scan_result("sql", sql_result)
    app_context.add_scan_result("xss", xss_result)

    # Metadata
    app_context.update_metadata("framework_version", "v1.0.0")
    app_context.update_metadata("classification_engine", "AppClassifier")

    # Auth model inference
    if auth_result.get("login_page_found"):
        app_context.auth_model = "session_based"
    else:
        app_context.auth_model = "unknown"

    # Endpoints
    for endpoint in auth_result.get("login_urls", []):
        app_context.add_endpoint(endpoint)

    # =========================================================
    # Function Discovery
    # =========================================================
    print("[*] Discovering functions...")

    functions = discover_functions(scan_results, app_context)

    # =========================================================
    # Attack Surface
    # =========================================================
    print("[*] Building attack surface...")

    surface_result = build_attack_surface(functions, auth_result)

    attack_surface = surface_result["surface_list"]
    attack_graph = surface_result["graph"]

    # =========================================================
    # Exploit Path Engine
    # =========================================================
    print("[*] Extracting exploit paths...")

    engine = ExploitPathEngine(attack_graph)
    exploit_paths = engine.build_paths()

    enriched_attack_surface = {
        "surface_list": attack_surface,
        "graph": attack_graph,
        "exploit_paths": exploit_paths
    }

    # =========================================================
    # Test Plan
    # =========================================================
    print("[*] Generating test plan...")

    test_plan = generate_test_plan(attack_surface)

    # =========================================================
    # OWASP Mapping
    # =========================================================
    print("[*] Mapping to OWASP Top 10...")

    owasp_report = classify_test_plan(test_plan)

    # =========================================================
    # Risk Ranking
    # =========================================================
    print("[*] Ranking attack surface...")

    attack_surface_ranked = rank_attack_surface(
        attack_surface,
        owasp_report["owasp"]
    )

    # =========================================================
    # Validation Execution
    # =========================================================
    print("[*] Executing validation layer...")

    validation_results = execute_validation(test_plan)

    # =========================================================
    # Validation Analytics
    # =========================================================
    print("[*] Running validation analytics...")

    validation_summary = analyze_validation(validation_results)

    # =========================================================
    # Exploitability Analysis
    # =========================================================
    print("[*] Running exploitability analysis...")

    exploitability_results = run_exploitability_analysis(
        attack_surface_ranked,
        validation_results
    )

    validate_pipeline(
        scan_results,
        functions,
        attack_surface_ranked,
        test_plan,
        owasp_report
    )

    # =========================================================
    # Coverage / Risk / Posture
    # =========================================================
    print("[*] Running coverage analysis...")
    coverage_result = analyze_coverage(attack_surface_ranked, test_plan)

    print("[*] Running risk analytics...")
    risk_result = analyze_risk(attack_surface_ranked)

    print("[*] Analyzing security posture...")
    posture_result = analyze_posture(coverage_result, risk_result)

    # =========================================================
    # Dashboard
    # =========================================================
    print("[*] Generating dashboard...")

    dashboard_result = generate_dashboard(
        coverage_result,
        risk_result,
        posture_result,
        validation_summary,
        exploitability_results
    )

    # =========================================================
    # Report Generation
    # =========================================================
    print("[*] Generating standardized report...")

    report = generate_report(
        url,
        enriched_attack_surface,
        test_plan,
        owasp_report["owasp"],
        coverage_result,
        risk_result,
        posture_result,
        validation_results,
        validation_summary,
        exploitability_results,
        dashboard_result
    )

    # =========================================================
    # Output
    # =========================================================
    os.makedirs("output", exist_ok=True)

    with open("output/report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)

    print("[+] Report saved to output/report.json")


# =========================================================
# Entry Point
# =========================================================
if __name__ == "__main__":
    main()