from datetime import datetime


def generate_report(ctx: dict):
    """
    Final Report Renderer
    - NO computation
    - NO business logic
    - ONLY formatting
    """

    return {
        "metadata": {
            "framework": "Local WPCTF",
            "version": ctx.get("metadata", {}).get("framework_version", "v1.1.0"),
            "target": ctx.get("target_url"),
            "timestamp": datetime.utcnow().isoformat() + "Z"
        },

        # --------------------------
        # Core classification
        # --------------------------
        "classification": ctx.get("classification"),

        # --------------------------
        # Scan results
        # --------------------------
        "scan_results": ctx.get("scan_results"),

        # --------------------------
        # Analysis layer (ALL scoring already done upstream)
        # --------------------------
        "analysis": ctx.get("analysis"),

        # --------------------------
        # Risk / posture already computed
        # --------------------------
        "risk_profile": ctx.get("risk_profile"),

        # --------------------------
        # Endpoints
        # --------------------------
        "endpoints": ctx.get("endpoints"),
    }