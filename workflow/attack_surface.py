def build_attack_surface(scan_results):

    attack_surface = []

    auth_result = scan_results.get("auth", {})

    if auth_result.get("login_page_found"):

        login_urls = auth_result.get(
            "login_urls"
        ) or []

        for login_url in login_urls:

            attack_surface.append({
                "type": "authentication",
                "target": login_url,
                "possible_tests": [
                    "weak_password",
                    "auth_bypass",
                    "session_management"
                ]
            })

    wp_result = scan_results.get(
        "wordpress",
        {}
    )

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