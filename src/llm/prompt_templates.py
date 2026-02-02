def fault_explanation_prompt(fault, severity, sensor_data):
    return (
        "You are an automotive diagnostic assistant.\n\n"
        f"Fault detected: {fault}\n"
        f"Severity level: {severity}\n\n"
        "Vehicle sensor summary:\n"
        f"{sensor_data}\n\n"
        "Explain:\n"
        "1. What this fault means\n"
        "2. Common causes\n"
        "3. Is it safe to drive?\n"
        "4. Recommended next action\n\n"
        "Use simple language."
    )