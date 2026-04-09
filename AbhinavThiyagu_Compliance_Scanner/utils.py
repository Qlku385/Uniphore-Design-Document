# Helper func : JSON loading/printing/formatting

import json

def load_json(file_path):
    #loads JSON file and returns data

    with open(file_path) as f:
        return json.load(f)
    
def print_violations(violations):
    #Prints violations in human_readable format

    if not violations:
        print("No violations found!")
        return
    
    for v in violations:
        print(f"[VIOLATIONS] Service: {v['service_id']}")
        print(f" Policy: {v['policy_id']}")
        print(f" Reason: {v['description']}")
        print("-" * 40)

def print_compliant(services):
    if not services:
        return
    
    print("\nCOMPLIANT SERVICES ✅")
    for s in services:
        print(f"[SUCCESS] Service: {s} meets all policy requirements")