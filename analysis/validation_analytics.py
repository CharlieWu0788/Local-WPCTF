def analyze_validation(
    validation_results
):
    """
    Analyze validation outcomes.
    """

    validated = 0
    failed = 0
    untested = 0

    for result in validation_results:

        evidence = result.get(
            "evidence",
            []
        )

        if (
            result.get(
                "validated",
                False
            )
        ):
            validated += 1

        elif (
            evidence
            and
            evidence[0]
            == "No executor available"
        ):
            untested += 1

        else:
            failed += 1

    total = (
        validated
        + failed
        + untested
    )

    score = 0

    if total:

        score = round(
            validated
            /
            total
            *
            100,
            2
        )

    return {
        "validated": validated,
        "failed": failed,
        "untested": untested,
        "validation_score": score
    }