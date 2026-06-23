def discover_functions(scan_results):
    """
    Discover application functions from scan results.

    V0.7.1
    - Uses WordPress detection
    - Uses authentication findings
    - Uses discovered links
    - Produces richer function mapping
    """

    functions = []

    auth = scan_results.get("auth", {})
    wordpress = scan_results.get("wordpress", {})

    # ----------------------------------
    # WordPress Admin
    # ----------------------------------
    if wordpress.get("wordpress_detected"):

        functions.append({
            "function": "wordpress_admin",
            "target": "/wp-admin"
        })

    # ----------------------------------
    # Login Detection
    # ----------------------------------
    if auth.get("login_page_found"):

        for login_url in auth.get("login_urls", []):

            functions.append({
                "function": "login",
                "target": login_url
            })

    # ----------------------------------
    # Link-Based Discovery
    # ----------------------------------
    for link in auth.get("discovered_links", []):

        text = link.get("text", "").strip().lower()
        url = link.get("url", "")

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

        elif text in ["faq", "faqs"]:

            functions.append({
                "function": "faq",
                "target": url
            })

        elif text in ["author", "authors"]:

            functions.append({
                "function": "author",
                "target": url
            })

        elif text in ["event", "events"]:

            functions.append({
                "function": "event",
                "target": url
            })

        elif text == "shop":

            functions.append({
                "function": "shop",
                "target": url
            })

    # ----------------------------------
    # Remove Duplicates
    # ----------------------------------
    unique_functions = []

    seen = set()

    for function in functions:

        key = (
            function["function"],
            function["target"]
        )

        if key not in seen:

            seen.add(key)
            unique_functions.append(function)

    # ----------------------------------
    # Safety Fallback
    # ----------------------------------
    if not unique_functions:

        unique_functions.append({
            "function": "wordpress_admin",
            "target": "/wp-admin"
        })

    return unique_functions