
LINK_FUNCTION_MAP = {
    ("blog",): "blog",
    ("about",): "about",
    ("faq", "faqs"): "faq",
    ("author", "authors"): "author",
    ("shop", "store"): "shop",
    ("profile", "account"): "profile",
    ("admin", "dashboard"): "admin_panel",
    ("search",): "search",
}

def discover_functions(
    scan_results,
    app_context=None
):
    """
    Function Discovery V1.0

    Supports:
    - WordPress
    - DVWA
    - OWASP Juice Shop
    - WebGoat
    - Mutillidae
    - Generic Web Applications

    Produces normalized business/security functions
    for attack surface modeling.
    """

    functions = []

    auth = scan_results.get("auth", {})
    wordpress = scan_results.get("wordpress", {})

    app_type = "generic_web"

    if app_context:
        app_type = app_context.app_type

    # =====================================================
    # Authentication Discovery
    # =====================================================

    if auth.get("login_page_found"):

        for login_url in auth.get(
            "login_urls",
            []
        ):

            functions.append({
                "function": "login",
                "target": login_url,
                "source_scanner": "auth_scan",
                "discovery_reason": "Login page detected",
                "metadata": {}
            })

    # =====================================================
    # WordPress Model
    # =====================================================

    if app_type == "wordpress":

        if wordpress.get(
            "wordpress_detected"
        ):

            functions.append({
                "function": "wordpress_admin",
                "target": "/wp-admin",
                "source_scanner": "wordpress_scan",
                "discovery_reason": "WordPress admin endpoint",
                "metadata": {}
            })

    # =====================================================
    # Training Platforms
    # =====================================================

    elif app_type in [
        "dvwa",
        "juice_shop",
        "webgoat",
        "mutillidae"
    ]:

        functions.extend([
            {
                "function": "security_training",
                "target": "/",
                "source_scanner": "platform_detection",
                "discovery_reason": "Training platform profile",
                "metadata": {}
            },

            {
                "function": "user_management",
                "target": "/login",
                "source_scanner": "platform_detection",
                "discovery_reason": "Training platform profile",
                "metadata": {}
            },

            {
                "function": "vulnerability_module",
                "target": "/",
                "source_scanner": "platform_detection",
                "discovery_reason": "Training platform profile",
                "metadata": {}
            }

        ])

    # =====================================================
    # Generic Web Application
    # =====================================================

    else:

        functions.append({
            "function": "web_application",
            "target": "/",
            "source_scanner": "generic_detection",
            "discovery_reason": "Generic web application",
            "metadata": {}
        })

    # =====================================================
    # Link-Based Discovery
    # =====================================================

    for link in auth.get(
        "discovered_links",
        []
    ):

        text = (
            link.get(
                "text",
                ""
            )
            .strip()
            .lower()
        )

        url = link.get(
            "url",
            ""
        )

        matched_function = None

        for keywords, function_name in LINK_FUNCTION_MAP.items():

            if text in keywords:
                matched_function = function_name
                break

        if matched_function:

            functions.append({
                "function": matched_function,
                "target": url,
                "source_scanner": "auth_scan",
                "discovery_reason": "Navigation link discovered",
                "metadata": {
                    "link_text": text
                }
            })

            functions.append({
                "function": "search",
                "target": url
            })

    # =====================================================
    # Remove Duplicates
    # =====================================================

    unique_functions = []

    seen = set()

    for function in functions:

        key = (
            function["function"],
            function["target"]
        )

        if key not in seen:

            seen.add(key)

            unique_functions.append(
                function
            )

    # =====================================================
    # Safety Fallback
    # =====================================================

    if not unique_functions:

        functions.append({
            "function": "web_application",
            "target": "/",
            "source_scanner": "fallback",
            "discovery_reason": "No functions discovered",
            "metadata": {}
        })

    return unique_functions