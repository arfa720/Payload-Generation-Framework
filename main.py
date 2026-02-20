import argparse
from modules import xss, sqli, cmd_injection
from utils import encoder, obfuscator, exporter


def main():
    parser = argparse.ArgumentParser(
        description="Educational Payload Generation Framework (OWASP Aligned)"
    )

    parser.add_argument(
        "--module", 
        choices=["xss", "sqli", "cmd"], 
        required=True
    )
    
    parser.add_argument(
        "--encode", 
        choices=["url", "base64", "hex"]
    )
    
    parser.add_argument(
        "--db", 
        choices=["mysql", "postgres", "mssql"]
    )
    
    parser.add_argument(
        "--export", 
        choices=["json", "txt"]
    )
        
    parser.add_argument(
        "--obfuscate",
        action="store_true",
        help="Apply built-in obfuscation techniques"
    )

    args = parser.parse_args()

    payloads = []

    if args.module == "xss":
        payloads = xss.generate_xss_payloads()

    elif args.module == "sqli":
        payloads = sqli.generate_sqli_payloads(args.db or "mysql")

    elif args.module == "cmd":
        payloads = cmd_injection.generate_cmd_payloads()

    # Apply encoding if selected
    if args.encode:
        payloads = encoder.apply_encoding(payloads, args.encode)

    # Apply obfuscation (optional future flag)
    if args.obfuscate:
        payloads = obfuscator.apply_obfuscation(payloads)


    print("\n===================================")
    print("   Payload Generation Framework")
    print("===================================\n")

    print("Educational Use Only - OWASP Aligned\n")


    # Print to CLI
    for p in payloads:
        print(p)

    # Export if selected
    if args.export:
        exporter.export_payloads(payloads, args.export)


if __name__ == "__main__":
    main()