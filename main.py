import json

from scanners.wordpress_scan import scan_wordpress
from scanners.auth_scan import scan_login_page
from scanners.sql_scan import scan_sql_injection
from scanners.xss_scan import scan_xss

from workflow.attack_surface import build_attack_surface
from workflow.test_plan import generate_test_plan


def main():
    try:
        with open("config.json", "r") as config_file:
            config = json.load(config_file)

        url = config["url"]

        # ----------------------------
        # Run scanners
        # ----------------------------
        results = {
            "wordpress": scan_wordpress(url),
            "auth": scan_login_page(url),
            "sql": scan_sql_injection(url),
            "xss": scan_xss(url)
        }

        # ----------------------------
        # Build attack surface
        # ----------------------------
        attack_surface = build_attack_surface(results)

        # ----------------------------
        # Generate test plan
        # ----------------------------
        test_plan = generate_test_plan(
            attack_surface
        )

        # ----------------------------
        # Append workflow results
        # ----------------------------
        results["attack_surface"] = attack_surface
        results["test_plan"] = test_plan

        print(
            json.dumps(
                results,
                indent=2
            )
        )

    except Exception as e:
        print(
            json.dumps(
                {
                    "error": str(e)
                },
                indent=2
            )
        )


if __name__ == "__main__":
    main()