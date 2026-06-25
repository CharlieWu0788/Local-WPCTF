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
                "target": login_url
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
                "target": "/wp-admin"
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
                "target": "/"
            },

            {
                "function": "user_management",
                "target": "/login"
            },

            {
                "function": "vulnerability_module",
                "target": "/"
            }

        ])

    # =====================================================
    # Generic Web Application
    # =====================================================

    else:

        functions.append({
            "function": "web_application",
            "target": "/"
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

        if text == "blog":

            functions.append({
                "function": "blog",
                "target": url
            })

        elif text == "about":

            functions.append({
                "function": "about",
                "target": url
            })

        elif text in [
            "faq",
            "faqs"
        ]:

            functions.append({
                "function": "faq",
                "target": url
            })

        elif text in [
            "author",
            "authors"
        ]:

            functions.append({
                "function": "author",
                "target": url
            })

        elif text in [
            "shop",
            "store"
        ]:

            functions.append({
                "function": "shop",
                "target": url
            })

        elif text in [
            "profile",
            "account"
        ]:

            functions.append({
                "function": "profile",
                "target": url
            })

        elif text in [
            "admin",
            "dashboard"
        ]:

            functions.append({
                "function": "admin_panel",
                "target": url
            })

        elif text in [
            "search"
        ]:

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
            "target": "/"
        })

    return unique_functions