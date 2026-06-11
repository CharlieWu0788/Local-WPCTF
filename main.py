import json

from scanners.wordpress_scan import scan_wordpress

def main():
    # Read configuration from config.json
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    url = config['url']
    
    # Scan the URL for WordPress signatures
    result = scan_wordpress(url)
    
    # Output the result in JSON format
    print(json.dumps(result))

if __name__ == "__main__":
    main()
