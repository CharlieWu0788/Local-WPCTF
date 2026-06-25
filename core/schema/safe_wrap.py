from core.schema.scanner_schema import default_scan_result


def safe_scanner_result(result: dict) -> dict:
    """
    Ensure scanner output never breaks pipeline
    """

    base = default_scan_result()

    if not result:
        return base

    # merge safely
    for k, v in result.items():
        if v is None:
            continue
        base[k] = v

    # enforce list safety
    if base.get("login_urls") is None:
        base["login_urls"] = []

    if base.get("discovered_links") is None:
        base["discovered_links"] = []

    if base.get("evidence") is None:
        base["evidence"] = []

    return base