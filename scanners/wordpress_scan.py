import requests
from bs4 import BeautifulSoup

def scan_wordpress(url):
    try:
        response = requests.get(
            url,
            timeout=5,
            allow_redirects=True
        )
    except requests.RequestException as e:
        return {
            "wordpress_detected": False,
            "evidence": [],
            "error": str(e)
        }
    
    if response.status_code < 200 or response.status_code >= 300:
        return {
            "wordpress_detected": False,
            "evidence": [],
            "error": f"HTTP {response.status_code}"
        }
    
    soup = BeautifulSoup(response.text, 'html.parser')
    evidence_list = []

    if "wp-content" in response.text.lower():
        evidence_list.append("wp-content found")

    if "wp-includes" in response.text.lower():
        evidence_list.append("wp-includes found")

    generator = soup.find("meta",attrs={"name": "generator"})
    if generator:
        name = generator.get('name', '')
        content = generator.get('content', '')
        if name.lower() == "generator":
            if 'wordpress' in content.lower():
                evidence_list.append("generator tag found")

    wordpress_detected = any([
        "wp-content found" in evidence_list,
        "wp-includes found" in evidence_list,
        "generator tag found" in evidence_list
    ])

    return {
        'wordpress_detected': wordpress_detected,
        'evidence': evidence_list
    }
