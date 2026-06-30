from typing import Dict, Any, List, Optional


class AppContext:
    """
    Central State Store (WPCTF V1.1+)

    Purpose:
    - Single source of truth for all scan/analysis/attack results
    - Decouple modules from parameter passing
    """

    def __init__(self, target_url: str):

        self.target_url: str = target_url

        # Core classification
        self.app_type: str = "unknown"
        self.classification: Dict[str, Any] = {}

        # Runtime info
        self.framework: Optional[str] = None
        self.auth_model: Optional[str] = None

        # Data stores
        self.endpoints: List[str] = []
        self.scan_results: Dict[str, Any] = {}

        # Analysis outputs (IMPORTANT)
        self.analysis: Dict[str, Any] = {}

        # Risk / security profile
        self.risk_profile: Dict[str, Any] = {}

        # Metadata
        self.metadata: Dict[str, Any] = {}

    # -------------------------
    # Core setters
    # -------------------------
    def set_app_type(self, app_type: str) -> None:
        self.app_type = app_type

    def set_classification(self, classification: Dict[str, Any]) -> None:
        self.classification = classification

    # -------------------------
    # Data ingestion
    # -------------------------
    def add_scan_result(self, key: str, value: Any) -> None:
        self.scan_results[key] = value

    def add_endpoint(self, endpoint: str) -> None:
        if endpoint not in self.endpoints:
            self.endpoints.append(endpoint)

    # -------------------------
    # Analysis layer
    # -------------------------
    def add_analysis(self, key: str, value: Any) -> None:
        self.analysis[key] = value

    def update_risk_profile(self, key: str, value: Any) -> None:
        self.risk_profile[key] = value

    # -------------------------
    # Metadata
    # -------------------------
    def update_metadata(self, key: str, value: Any) -> None:
        self.metadata[key] = value

    # -------------------------
    # Export
    # -------------------------
    def to_dict(self) -> Dict[str, Any]:
        return {
            "target_url": self.target_url,
            "app_type": self.app_type,
            "classification": self.classification,
            "framework": self.framework,
            "auth_model": self.auth_model,
            "endpoints": self.endpoints,
            "scan_results": self.scan_results,
            "analysis": self.analysis,
            "risk_profile": self.risk_profile,
            "metadata": self.metadata,
        }