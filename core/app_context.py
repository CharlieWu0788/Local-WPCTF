from typing import Dict, Any, List, Optional


class AppContext:
    """
    Core context object for Web Application Security Assessment Framework (V1.0).

    This object represents a normalized view of any target application,
    decoupling scanners and workflow logic from framework-specific assumptions
    (e.g., WordPress).
    """

    def __init__(self, target_url: str):
        # Target application entry point
        self.target_url: str = target_url

        # Application classification result (e.g., wordpress, dvwa, generic)
        self.app_type: str = "unknown"

        # Detected or inferred technology stack
        self.framework: Optional[str] = None

        # Authentication model (session-based, JWT, OAuth, etc.)
        self.auth_model: Optional[str] = None

        # Discovered endpoints (URLs, APIs, pages)
        self.endpoints: List[str] = []

        # Input surface model (parameters, headers, body fields)
        self.input_surface: Dict[str, Any] = {}

        # Attack surface graph (logical representation of components)
        self.attack_surface: Dict[str, Any] = {}

        # Scanner outputs (normalized results)
        self.scan_results: Dict[str, Any] = {}

        # Execution metadata (runtime info, timing, etc.)
        self.metadata: Dict[str, Any] = {}

        # Risk aggregation results
        self.risk_profile: Dict[str, Any] = {}

    def set_app_type(self, app_type: str) -> None:
        """
        Set detected application type.
        """
        self.app_type = app_type

    def set_framework(self, framework: str) -> None:
        """
        Set detected backend/framework type.
        """
        self.framework = framework

    def add_endpoint(self, endpoint: str) -> None:
        """
        Add a discovered endpoint to the context.
        """
        if endpoint not in self.endpoints:
            self.endpoints.append(endpoint)

    def update_input_surface(self, key: str, value: Any) -> None:
        """
        Update input surface model (parameters, forms, APIs).
        """
        self.input_surface[key] = value

    def update_attack_surface(self, key: str, value: Any) -> None:
        """
        Update attack surface graph representation.
        """
        self.attack_surface[key] = value

    def add_scan_result(self, scanner_name: str, result: Any) -> None:
        """
        Store scanner output in normalized format.
        """
        self.scan_results[scanner_name] = result

    def update_metadata(self, key: str, value: Any) -> None:
        """
        Store runtime or execution metadata.
        """
        self.metadata[key] = value

    def update_risk_profile(self, key: str, value: Any) -> None:
        """
        Store risk analysis results.
        """
        self.risk_profile[key] = value

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert full context into a serializable dictionary.
        Used for reporting layer (report.json).
        """
        return {
            "target_url": self.target_url,
            "app_type": self.app_type,
            "framework": self.framework,
            "auth_model": self.auth_model,
            "endpoints": self.endpoints,
            "input_surface": self.input_surface,
            "attack_surface": self.attack_surface,
            "scan_results": self.scan_results,
            "metadata": self.metadata,
            "risk_profile": self.risk_profile,
        }