from reports.confidence_scoring import score_attack_surface
from workflow.attack_graph import AttackGraph, AttackNode


def build_attack_surface(functions, auth_result=None):
    """
    Build attack surface graph from discovered functions.

    V1.0 Upgrade:
    - Converts flat surface list into graph structure
    - Enables dependency modeling between surfaces
    - Prepares for exploit chain analysis
    """

    graph = AttackGraph()
    attack_surface = []

    previous_node_id = None

    for i, function in enumerate(functions):

        func_name = function.get("function", "").lower()
        target = function.get("target", "")

        node_id = f"node_{i}_{func_name}"

        surface_type = None
        possible_tests = []

        # -----------------------------
        # Authentication Surface
        # -----------------------------
        if func_name in ["login", "signin", "auth"]:

            surface_type = "authentication_surface"
            possible_tests = [
                "weak_password_testing",
                "authentication_bypass",
                "session_management"
            ]

        # -----------------------------
        # Content Surface
        # -----------------------------
        elif func_name in ["blog", "post", "content", "comment"]:

            surface_type = "content_surface"
            possible_tests = [
                "stored_xss",
                "html_injection"
            ]

        # -----------------------------
        # Information Surface
        # -----------------------------
        elif func_name in ["about", "faq", "info"]:

            surface_type = "information_surface"
            possible_tests = [
                "information_disclosure",
                "debug_exposure"
            ]

        # -----------------------------
        # User Surface
        # -----------------------------
        elif func_name in ["user", "profile", "account"]:

            surface_type = "user_surface"
            possible_tests = [
                "user_enumeration",
                "privilege_escalation"
            ]

        # -----------------------------
        # Business Logic Surface
        # -----------------------------
        elif func_name in ["shop", "checkout", "payment"]:

            surface_type = "business_surface"
            possible_tests = [
                "workflow_bypass",
                "parameter_tampering"
            ]

        else:
            surface_type = "generic_surface"
            possible_tests = [
                "input_fuzzing",
                "injection_detection"
            ]

        # -----------------------------
        # Create Graph Node
        # -----------------------------
        node = AttackNode(
            node_id=node_id,
            node_type=surface_type,
            target=target
        )

        node.add_attribute("function", func_name)
        node.add_attribute("possible_tests", possible_tests)

        # Confidence scoring (still reused)
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
        # Create edges (simple flow model)
        # -----------------------------
        if previous_node_id:
            graph.add_edge(previous_node_id, node_id)

        previous_node_id = node_id

        # Keep backward compatibility output
        attack_surface.append({
            "id": node_id,
            "type": surface_type,
            "target": target,
            "confidence": confidence,
            "possible_tests": possible_tests
        })

    return {
        "graph": graph.to_dict(),
        "surface_list": attack_surface
    }