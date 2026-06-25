from typing import List, Dict, Any


def default_scan_result() -> Dict[str, Any]:
    """
    Standardized scanner output schema
    V1.0.1 Contract Layer
    """

    return {
        "login_page_found": False,
        "login_urls": [],
        "discovered_links": [],
        "final_url": "",
        "evidence": [],
        "error": None
    }