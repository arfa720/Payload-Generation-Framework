import urllib.parse
import base64


def apply_encoding(payloads, encoding_type):
    encoded_payloads = []

    for p in payloads:
        if encoding_type == "url":
            encoded_payloads.append(urllib.parse.quote(p))

        elif encoding_type == "base64":
            encoded_payloads.append(
                base64.b64encode(p.encode()).decode()
            )

        elif encoding_type == "hex":
            encoded_payloads.append(p.encode().hex())

    return encoded_payloads