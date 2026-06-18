from reports.confidence_scoring import score_attack_surface


def build_attack_surface(functions, auth_result=None):
    """
    Build attack surfaces from discovered functions.

    v0.5.3 Upgrade:
    - Adds confidence scoring
    - Supports extensible surface mapping
    - Prepares for OWASP + Raptor pipeline
    """

    attack_surface = []

    for function in functions:

        func_name = function.get("function", "")
        target = function.get("target", "")

        surface = None

        # -----------------------------
        # 1. Authentication Surface
        # -----------------------------
        if func_name == "login":

            surface = {
                "type": "authentication",
                "target": target,
                "possible_tests": [
                    "weak_password",
                    "auth_bypass",
                    "session_management"
                ]
            }

        # -----------------------------
        # 2. WordPress Admin Surface
        # -----------------------------
        elif func_name == "wordpress_admin":

            surface = {
                "type": "wordpress",
                "target": target,
                "possible_tests": [
                    "plugin_enumeration",
                    "version_detection"
                ]
            }

        # -----------------------------
        # 3. Blog / Content Surface
        # -----------------------------
        elif func_name in ["blog", "post", "content"]:

            surface = {
                "type": "content_management",
                "target": target,
                "possible_tests": [
                    "stored_xss",
                    "content_injection"
                ]
            }

        # -----------------------------
        # 4. Information Exposure Surface
        # -----------------------------
        elif func_name in ["about", "faq", "info"]:

            surface = {
                "type": "information_disclosure",
                "target": target,
                "possible_tests": [
                    "sensitive_information_exposure",
                    "information_leakage"
                ]
            }

        # -----------------------------
        # 5. User Enumeration Surface
        # -----------------------------
        elif func_name in ["author", "user", "profile"]:

            surface = {
                "type": "user_enumeration",
                "target": target,
                "possible_tests": [
                    "user_disclosure",
                    "username_enumeration"
                ]
            }

        # -----------------------------
        # 6. Business Logic Surface
        # -----------------------------
        elif func_name in ["shop", "checkout", "payment"]:

            surface = {
                "type": "business_function",
                "target": target,
                "possible_tests": [
                    "workflow_bypass",
                    "parameter_tampering",
                    "price_manipulation",
                    "access_control"
                ]
            }

        # -----------------------------
        # Skip unknown functions
        # -----------------------------
        else:
            continue

        # -----------------------------
        # Confidence Scoring (NEW)
        # -----------------------------
        surface["confidence"] = score_attack_surface(surface, auth_result)

        attack_surface.append(surface)

    # -----------------------------
    # Optional: sort by confidence
    # (useful for next-stage planner)
    # -----------------------------
    attack_surface.sort(key=lambda x: x.get("confidence", 0), reverse=True)

    return attack_surface