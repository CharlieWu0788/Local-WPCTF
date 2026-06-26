from workflow.attack_graph import AttackGraph, AttackNode
from reports.confidence_scoring import score_attack_surface


# -----------------------------
# V1.0.1 Capability Mapping Layer
# -----------------------------
CAPABILITY_MAP = {
    "authentication": ["login", "signin", "auth", "logout"],
    "content": ["blog", "post", "content", "comment"],
    "information": ["about", "faq", "info", "help"],
    "user": ["user", "profile", "account"],
    "business": ["shop", "checkout", "payment"],
    "api": ["api", "endpoint", "graphql", "rest"]
}


def detect_capability(func_name: str):
    """
    V1.0.1 Generic capability detection layer
    """

    if not isinstance(func_name, str):
        return "generic"

    func_name = func_name.lower()

    for capability, keywords in CAPABILITY_MAP.items():
        if func_name in keywords:
            return capability

    return "generic"


def build_attack_surface(functions, auth_result=None):
    """
    Build attack surface graph (V1.0.1 safe version)
    """

    functions = functions or []

    graph = AttackGraph()
    attack_surface = []

    previous_node_id = None

    for i, function in enumerate(functions):

        if not isinstance(function, dict):
            continue

        func_name = (function.get("function") or "").lower()
        target = function.get("target", "")

        node_id = f"node_{i}_{func_name}"

        # -----------------------------
        # capability detection
        # -----------------------------
        capability = detect_capability(func_name)
        surface_type = f"{capability}_surface"

        # -----------------------------
        # test mapping
        # -----------------------------
        test_map = {
            "authentication": [
                "weak_password_testing",
                "authentication_bypass",
                "session_analysis"
            ],
            "content": [
                "stored_xss",
                "html_injection"
            ],
            "information": [
                "information_disclosure",
                "debug_exposure"
            ],
            "user": [
                "user_enumeration",
                "privilege_escalation"
            ],
            "business": [
                "workflow_bypass",
                "parameter_tampering"
            ],
            "api": [
                "api_auth_bypass",
                "rate_limit_testing"
            ],
            "generic": [
                "input_fuzzing",
                "injection_detection"
            ]
        }

        possible_tests = test_map.get(capability, test_map["generic"])

        # -----------------------------
        # graph node
        # -----------------------------
        node = AttackNode(
            node_id=node_id,
            node_type=surface_type,
            target=target
        )

        node.add_attribute("function", func_name)
        node.add_attribute("capability", capability)
        node.add_attribute("possible_tests", possible_tests)
        node.add_attribute("position", i)

        # -----------------------------
        # confidence scoring
        # -----------------------------
        confidence = score_attack_surface(
            {
                "type": surface_type,
                "target": target,
                "possible_tests": possible_tests
            },
            auth_result
        )

        node.add_attribute("confidence", confidence)

        graph.add_node(node)

        # -----------------------------
        # graph edges
        # -----------------------------
        if previous_node_id:
            graph.add_edge(previous_node_id, node_id)

        previous_node_id = node_id

        # -----------------------------
        # output schema
        # -----------------------------
        attack_surface.append({
            "id": node_id,
            "type": surface_type,
            "capability": capability,
            "target": target,
            "confidence": confidence,
            "possible_tests": possible_tests,

            "source_scanner": function.get("source_scanner", "unknown"),
            "discovery_reason": function.get("discovery_reason", "N/A"),
            "metadata": function.get("metadata", {})
        })

    return {
        "schema_version": "v1.1.0",
        "graph": graph.to_dict(),
        "surface_list": attack_surface
    }