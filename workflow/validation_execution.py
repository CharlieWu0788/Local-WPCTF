from executors.auth_executor import (
    execute_auth_validation
)

from executors.sql_executor import (
    execute_sql_validation
)

from executors.xss_executor import (
    execute_xss_validation
)


def execute_validation(test_plan):
    """
    Execute validation layer.

    V0.7:
    - Consumes generated test plan
    - Dispatches safe validation tasks
    - Collects validation evidence
    - Does NOT perform exploitation
    """

    results = []

    for task in test_plan:

        test_name = task.get(
            "test",
            ""
        )

        # -----------------------------
        # Authentication Validation
        # -----------------------------

        if test_name in [
            "weak_password",
            "auth_bypass",
            "session_management"
        ]:

            results.append(
                execute_auth_validation(task)
            )

        # -----------------------------
        # XSS Validation
        # -----------------------------

        elif test_name in [
            "stored_xss",
            "content_injection"
        ]:

            results.append(
                execute_xss_validation(task)
            )

        # -----------------------------
        # SQL-style Validation
        # -----------------------------

        elif test_name in [
            "parameter_tampering",
            "price_manipulation"
        ]:

            results.append(
                execute_sql_validation(task)
            )

        # -----------------------------
        # Untested Surface
        # -----------------------------

        else:

            results.append({

                "surface_type":
                    task.get(
                        "surface_type",
                        "unknown"
                    ),

                "target":
                    task.get(
                        "target",
                        ""
                    ),

                "test":
                    test_name,

                "validated":
                    False,

                "evidence": [
                    "No validator available"
                ]
            })

    return results