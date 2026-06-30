from workflow.attack_graph import AttackGraph, AttackNode


# =========================================================
# Capability Mapping Layer
# =========================================================
CAPABILITY_MAP = {
    "authentication": ["login", "signin", "auth", "logout", "wp-login"],
    "content": ["blog", "post", "content", "comment", "page"],
    "information": ["about", "faq", "info", "help"],
    "user": ["user", "profile", "account"],
    "business": ["shop", "checkout", "payment", "cart"],
    "api": ["api", "endpoint", "graphql", "rest", "wp-json"],
    "upload": ["upload", "file"]
}


def detect_capability(text: str):
    """
    Map endpoint/text to capability type
    """
    if not isinstance(text, str):
        return "generic"

    text = text.lower()

    for capability, keywords in CAPABILITY_MAP.items():
        if any(k in text for k in keywords):
            return capability

    return "generic"


# =========================================================
# MAIN BUILDER (SCAN_RESULTS BASED)
# =========================================================
def build_attack_surface(scan_results: dict):
    """
    V2 Scan-Based Attack Surface Builder

    Input:
        scan_results (dict)

    Output:
        {
            graph,
            surface_list
        }
    """

    scan_results = scan_results or {}

    graph = AttackGraph()
    attack_surface = []

    previous_node_id = None
    node_index = 0

    # =========================================================
    # Helper: create node
    # =========================================================
    def add_node(source, items, surface_type_prefix):
        nonlocal node_index, previous_node_id

        for item in items or []:

            node_id = f"node_{node_index}_{surface_type_prefix}"

            capability = detect_capability(
                item.get("url") if isinstance(item, dict) else str(item)
            )

            node_type = f"{capability}_surface"

            node = AttackNode(
                node_id=node_id,
                node_type=node_type,
                target=item.get("url") if isinstance(item, dict) else str(item)
            )

            node.add_attribute("capability", capability)
            node.add_attribute("source", source)
            node.add_attribute("raw", item)

            graph.add_node(node)

            if previous_node_id:
                graph.add_edge(previous_node_id, node_id)

            previous_node_id = node_id

            attack_surface.append({
                "id": node_id,
                "type": node_type,
                "capability": capability,
                "target": node.target,
                "source_scanner": source,
                "metadata": item if isinstance(item, dict) else {}
            })

            node_index += 1

    # =========================================================
    # 1. WordPress Surface
    # =========================================================
    wp = scan_results.get("wordpress", {})

    if wp.get("wordpress_detected"):
        add_node(
            "wordpress",
            [{"url": wp.get("final_url", "")}],
            "wordpress"
        )

    # =========================================================
    # 2. Auth Surface
    # =========================================================
    auth = scan_results.get("auth", {})

    add_node(
        "auth_login_urls",
        [{"url": u} for u in auth.get("login_urls", [])],
        "auth"
    )

    add_node(
        "auth_links",
        auth.get("discovered_links", []),
        "auth"
    )

    # =========================================================
    # 3. SQL Surface
    # =========================================================
    sql = scan_results.get("sql", {})

    add_node(
        "sql_params",
        [{"url": "parameter_based_scan"}] if sql.get("tested_payloads") else [],
        "sql"
    )

    # =========================================================
    # 4. XSS Surface
    # =========================================================
    xss = scan_results.get("xss", {})

    if xss.get("tested_payloads"):
        add_node(
            "xss_payloads",
            [{"url": "form_based_input"}],
            "xss"
        )

    # =========================================================
    # Final Output
    # =========================================================
    return {
        "schema_version": "v2.0.0",
        "graph": graph.to_dict(),
        "surface_list": attack_surface
    }