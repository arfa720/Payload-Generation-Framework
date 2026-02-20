import json
import os


def export_payloads(payloads, format_type):
    os.makedirs("outputs", exist_ok=True)

    if format_type == "json":
        with open("outputs/payloads.json", "w") as f:
            json.dump(payloads, f, indent=4)

    elif format_type == "txt":
        with open("outputs/payloads.txt", "w") as f:
            for p in payloads:
                f.write(p + "\n")