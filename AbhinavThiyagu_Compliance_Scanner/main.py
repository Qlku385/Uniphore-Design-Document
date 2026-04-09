# Entry point - Flow of code / calls engine and utils

from engine import evaluate_rules
from utils import load_json, print_compliant, print_violations

def main():

    services = load_json("services.json")
    policies = load_json("policies.json")

    violations, compliant_services = evaluate_rules(services, policies)

    print_violations(violations)
    print_compliant(compliant_services)

if __name__ == "__main__":
    main()