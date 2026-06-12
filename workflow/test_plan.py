def generate_test_plan(attack_surface):
    """
    Generate test tasks from attack surface.
    """

    tasks = []

    for surface in attack_surface:

        for test in surface.get("possible_tests", []):

            tasks.append({
                "surface_type": surface["type"],
                "target": surface["target"],
                "test": test
            })

    return tasks