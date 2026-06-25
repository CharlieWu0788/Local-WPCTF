from typing import Dict, Any


class AppClassifier:
    """
    Application Classification Engine (V1.0)

    Purpose:
    - Identify target application category
    - Remove WordPress-only assumptions
    - Support future web targets

    Output examples:
        wordpress
        training_platform
        generic_web
    """

    def classify(self, scan_results: Dict[str, Any]) -> str:

        # ----------------------------------
        # WordPress Detection
        # ----------------------------------

        wordpress_result = scan_results.get(
            "wordpress",
            {}
        )

        if wordpress_result.get(
            "wordpress_detected",
            False
        ):
            return "wordpress"

        # ----------------------------------
        # Authentication Fingerprints
        # ----------------------------------

        auth_result = scan_results.get(
            "auth",
            {}
        )

        login_urls = auth_result.get(
            "login_urls",
            []
        )

        # V1 CLEAN: assume schema layer guarantees list
        login_text = " ".join(
            str(x).lower()
            for x in login_urls
        )

        # ----------------------------------
        # DVWA
        # ----------------------------------

        if "dvwa" in login_text:
            return "training_platform"

        # ----------------------------------
        # Juice Shop
        # ----------------------------------

        if "juice" in login_text:
            return "training_platform"

        # ----------------------------------
        # WebGoat
        # ----------------------------------

        if "webgoat" in login_text:
            return "training_platform"

        # ----------------------------------
        # Mutillidae
        # ----------------------------------

        if "mutillidae" in login_text:
            return "training_platform"

        # ----------------------------------
        # Default
        # ----------------------------------

        return "generic_web"


def classify_application(
    scan_results: Dict[str, Any]
) -> str:

    classifier = AppClassifier()

    return classifier.classify(
        scan_results
    )