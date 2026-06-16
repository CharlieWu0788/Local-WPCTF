import os
import json
import sys

from scanners.wordpress_scan import scan_wordpress
from scanners.auth_scan import scan_authentication
from scanners.sql_scan import scan_sql_injection
from scanners.xss_scan import scan_xss

from workflow.attack_surface import build_attack_surface
from workflow.test_plan import generate_test_plan

from reports.owasp_mapper import classify_test_plan
from reports.json_report import generate_report


def main():

    if len(sys.argv) < 2:
        print("Usage: python main.py <url>")
        return

    url = sys.argv[1]

    print("[*] Running WordPress detection...")
    wordpress_result = scan_wordpress(url)

    print("[*] Running authentication scan...")
    auth_result = scan_authentication(url)
    print(auth_result)

    print("[DEBUG] Auth Result:")
    print(json.dumps(auth_result, indent=4))

    print("[*] Running SQL reconnaissance...")
    sql_result = scan_sql_injection(url)

    print("[*] Running XSS reconnaissance...")
    xss_result = scan_xss(url)

    print("[*] Building attack surface...")
    scan_results = {
        "wordpress": wordpress_result,
        "auth": auth_result,
        "sql": sql_result,
        "xss": xss_result
    }

    attack_surface = build_attack_surface(
        scan_results
    )

    print(json.dumps(
    attack_surface,
    indent=4
    ))

    print("[*] Generating test plan...")
    test_plan = generate_test_plan(attack_surface)

    print("[*] Mapping to OWASP Top 10...")
    owasp_report = classify_test_plan(test_plan)

    report = generate_report(
        url,
        attack_surface,
        test_plan,
        owasp_report["owasp"]
    )

    print("\n[*] Generating standardized report...\n")

    print(
        json.dumps(
            report,
            indent=4
        )
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

    print(
        "\n[+] Report saved to report.json"
    )


if __name__ == "__main__":
    main()

