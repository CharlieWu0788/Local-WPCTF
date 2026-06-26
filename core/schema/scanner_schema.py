from typing import Dict, Any


def default_scan_result() -> Dict[str, Any]:
    """
    Generic scanner output schema.

    This schema defines the common contract shared by all scanners
    in the framework. It also preserves backward compatibility with
    V1.0.x authentication scanner outputs.
    """

    return {

        # -------------------------------------------------
        # Generic Scanner Metadata
        # -------------------------------------------------
        "scanner": "",
        "success": False,
        "findings": [],
        "metadata": {},

        # -------------------------------------------------
        # Common Output
        # -------------------------------------------------
        "evidence": [],
        "error": None,

        # -------------------------------------------------
        # Backward Compatibility (V1.0.x)
        # -------------------------------------------------
        "login_page_found": False,
        "login_urls": [],
        "discovered_links": [],
        "final_url": ""
    }