import json

from scanners.wordpress_scan import scan_wordpress
from scanners.auth_scan import scan_login_page
from scanners.sql_scan import scan_sql_injection
from scanners.xss_scan import scan_xss


def main():
    try:
        with open("config.json", "r") as config_file:
            config = json.load(config_file)

        url = config["url"]

        results = {
            "wordpress": scan_wordpress(url),
            "auth": scan_login_page(url),
            "sql": scan_sql_injection(url),
            "xss": scan_xss(url)
        }

        print(json.dumps(results, indent=2))

    except Exception as e:
        print(json.dumps({
            "error": str(e)
        }, indent=2))


if __name__ == "__main__":
    main()