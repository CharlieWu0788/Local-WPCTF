import json

from scanners.wordpress_scan import scan_wordpress

def main():
    try:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)

        url = config['url']

        result = scan_wordpress(url)

        print(json.dumps(result))

    except Exception as e:
        print(json.dumps({
            "wordpress_detected": False,
            "evidence": [],
            "error": str(e)
        }))

if __name__ == "__main__":
    main()