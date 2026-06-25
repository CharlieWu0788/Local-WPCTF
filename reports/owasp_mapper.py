def classify_test_plan(test_plan=None, exploit_paths=None):
    """
    V1 OWASP Mapper (Graph-aware version)

    Supports:
    - Legacy test_plan (fallback)
    - V1 exploit_paths (primary input)
    """

    owasp_mapping = []

    # =====================================================
    # V1 MODE: exploit path based classification (preferred)
    # =====================================================
    if exploit_paths:

        for path_obj in exploit_paths:

            path = path_obj.get("path", [])
            score = path_obj.get("risk_score", 0)

            categories = set()

            for node in path:

                node_lower = str(node).lower()

                # -------------------------
                # Authentication weakness
                # -------------------------
                if "login" in node_lower or "auth" in node_lower:
                    categories.add("A07: Identification and Authentication Failures")

                # -------------------------
                # Injection / SQL / XSS
                # -------------------------
                if "sql" in node_lower or "inject" in node_lower:
                    categories.add("A03: Injection")

                if "xss" in node_lower or "content" in node_lower:
                    categories.add("A03: Injection")

                # -------------------------
                # Access Control Issues
                # -------------------------
                if "admin" in node_lower or "user" in node_lower:
                    categories.add("A01: Broken Access Control")

                # -------------------------
                # Business Logic
                # -------------------------
                if "payment" in node_lower or "checkout" in node_lower:
                    categories.add("A04: Insecure Design")

            owasp_mapping.append({
                "path": path,
                "risk_score": score,
                "owasp": list(categories) if categories else ["A05: Security Misconfiguration"]
            })

        return {
            "owasp": owasp_mapping
        }

    # =====================================================
    # LEGACY MODE: fallback for old test_plan
    # =====================================================
    if test_plan:

        for item in test_plan:

            tests = item.get("possible_tests", [])

            categories = set()

            for t in tests:

                if "auth" in t:
                    categories.add("A07: Authentication Failures")

                if "sql" in t:
                    categories.add("A03: Injection")

                if "xss" in t:
                    categories.add("A03: Injection")

                if "bypass" in t:
                    categories.add("A01: Broken Access Control")

            owasp_mapping.append({
                "test": item,
                "owasp": list(categories) if categories else ["A05: Security Misconfiguration"]
            })

        return {
            "owasp": owasp_mapping
        }

    # =====================================================
    # EMPTY SAFE RETURN (fixes your crash)
    # =====================================================
    return {
        "owasp": [
            {
                "owasp": ["A05: Security Misconfiguration"],
                "note": "No exploit paths or test plan available"
            }
        ]
    }