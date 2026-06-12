def build_attack_surface(scan_results):
    """
    Convert scanner outputs into attack surface entries.
    """

    attack_surface = []

    # Authentication surface
    auth_result = scan_results.get("auth", {})

    if auth_result.get("login_page_found"):

        login_urls = auth_result.get("login_urls") or []

        for login_url in login_urls:
            if "lostpassword" in login_url.lower():
                continue

            attack_surface.append({
                "type": "authentication",
                "target": login_url,
                "possible_tests": [
                    "weak_password",
                    "auth_bypass",
                    "session_management"
                ]
            })

    # WordPress surface
    wp_result = scan_results.get("wordpress", {})

    if wp_result.get("wordpress_detected"):

        attack_surface.append({
            "type": "wordpress",
            "target": "wordpress_instance",
            "possible_tests": [
                "plugin_enumeration",
                "version_detection"
            ]
        })

    return attack_surface