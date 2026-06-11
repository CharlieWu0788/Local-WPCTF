import requests
from bs4 import BeautifulSoup

def scan_wordpress(url):
    """
    Scans a given URL to detect if it's a WordPress installation.
    
    Args:
        url (str): The URL to be scanned.
        
    Returns:
        dict: A dictionary containing the detection result and evidence.
    """
    try:
        # Send an HTTP GET request to the target URL
        response = requests.get(
            url,
            timeout=5,
            allow_redirects=True
        )
    except requests.RequestException as e:
        # Handle any network-related errors during the request
        return {
            "wordpress_detected": False,
            "evidence": [],
            "error": str(e)
        }
    
    # Check if the response status code is within the successful range (200-299)
    if response.status_code < 200 or response.status_code >= 300:
        return {
            "wordpress_detected": False,
            "evidence": [],
            "error": f"HTTP {response.status_code}"
        }
    
    # Parse the response content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    evidence_list = []

    # Check for the presence of "wp-content" in the response body (case-insensitive)
    if "wp-content" in response.text.lower():
        evidence_list.append("wp-content found")

    # Check for the presence of "wp-includes" in the response body (case-insensitive)
    if "wp-includes" in response.text.lower():
        evidence_list.append("wp-includes found")

    # Look for a meta generator tag containing 'wordpress' in its content
    generator_found = False
    for meta_tag in soup.find_all('meta'):
        name = meta_tag.get('name', '')
        content = meta_tag.get('content', '')
        if name.lower() == "generator":
            if 'wordpress' in content.lower():
                evidence_list.append("generator tag found")
                generator_found = True
                break  # Found one, no need to check further

    # Determine if any evidence of WordPress was found
    wordpress_detected = len(evidence_list) > 0

    return {
        'wordpress_detected': wordpress_detected,
        'evidence': evidence_list
    }
