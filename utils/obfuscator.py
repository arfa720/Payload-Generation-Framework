import random

def random_case(text):
    return ''.join(
        c.upper() if random.choice([True, False]) else c.lower()
        for c in text
    )

def insert_generic_comments(payload):
    keywords = ["script", "select", "union", "or"]
    
    for k in keywords:
        if k in payload.lower():
            payload = payload.replace(k, k[:2] + "/**/" + k[2:])
    
    return payload

def add_whitespace(payload):
    return payload.replace(";", "; ")

def apply_obfuscation(payloads):
    obfuscated = []

    for p in payloads:
        temp = insert_generic_comments(p)
        temp = add_whitespace(temp)
        temp = random_case(temp)
        obfuscated.append(temp)

    return obfuscated