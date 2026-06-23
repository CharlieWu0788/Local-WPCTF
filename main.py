import os
import json

from scanners.wordpress_scan import scan_wordpress
from scanners.auth_scan import scan_authentication
from scanners.sql_scan import scan_sql_injection
from scanners.xss_scan import scan_xss

from workflow.function_discovery import discover_functions
from workflow.attack_surface import build_attack_surface
from workflow.test_plan import generate_test_plan
from workflow.pipeline_checker import validate_pipeline

from workflow.validation_execution import execute_validation
from workflow.exploit_simulation import run_exploitability_analysis

from reports.owasp_mapper import classify_test_plan
from reports.json_report import generate_report
from reports.risk_engine import rank_attack_surface

from analysis.coverage_analyzer import analyze_coverage
from analysis.risk_analytics import analyze_risk
from analysis.posture_analyzer import analyze_posture
from analysis.validation_analytics import analyze_validation

from reports.dashboard_generator import generate_dashboard


def main():

    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    url = config["target_url"]

    print(f"[*] Target: {url}")

    print("[*] Running WordPress detection...")
    wordpress_result = scan_wordpress(url)

    print("[*] Running authentication scan...")
    auth_result = scan_authentication(url)

    print("[*] Running SQL reconnaissance...")
    sql_result = scan_sql_injection(url)

    print("[*] Running XSS reconnaissance...")
    xss_result = scan_xss(url)

    scan_results = {
        "wordpress": wordpress_result,
        "auth": auth_result,
        "sql": sql_result,
        "xss": xss_result
    }

    print("[*] Discovering functions...")
    functions = discover_functions(scan_results)

    print("[*] Building attack surface...")
    attack_surface = build_attack_surface(
        functions,
        auth_result
    )

    print("[*] Generating test plan...")
    test_plan = generate_test_plan(
        attack_surface
    )

    print("[*] Mapping to OWASP Top 10...")
    owasp_report = classify_test_plan(
        test_plan
    )

    print("[*] Ranking attack surface...")
    attack_surface = rank_attack_surface(
        attack_surface,
        owasp_report["owasp"]
    )

    print("[*] Executing validation layer...")
    validation_results = execute_validation(
        test_plan
    )

    print("[*] Running validation analytics...")
    validation_summary = analyze_validation(
        validation_results
    )

    print("[*] Running exploitability analysis...")
    exploitability_results = run_exploitability_analysis(
        attack_surface,
        validation_results
    )

    validate_pipeline(
        scan_results,
        functions,
        attack_surface,
        test_plan,
        owasp_report
    )

    print("[*] Running coverage analysis...")
    coverage_result = analyze_coverage(
        attack_surface,
        test_plan
    )

    print("[*] Running risk analytics...")
    risk_result = analyze_risk(
        attack_surface
    )

    print("[*] Analyzing security posture...")
    posture_result = analyze_posture(
        coverage_result,
        risk_result
    )

    print("[*] Generating dashboard...")
    dashboard_result = generate_dashboard(
        coverage_result,
        risk_result,
        posture_result,
        validation_summary,
        exploitability_results
    )

    print("[*] Generating standardized report...")

    report = generate_report(
        url,
        attack_surface,
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

    os.makedirs(
        "output",
        exist_ok=True
    )

    with open(
        "output/report.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            report,
            f,
            indent=4,
            ensure_ascii=False
        )

    print("[+] Report saved to output/report.json")


if __name__ == "__main__":
    main()