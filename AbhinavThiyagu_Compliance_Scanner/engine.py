# Core logic : violates checks / rule eval

def violates(service, policy):
    #Returns True if service violates the policy
    if service["resourceType"] != policy["resourceType"]:
        return False
    
    if service ["environment"] not in policy ["environment"]:
        return False
    
    for key, expected in policy["conditions"].items():

        if key == "replicas":
            if service.get(key, 0) < expected:
                return True
        else:
            if service.get(key) != expected:
                return True
    return False
    
def evaluate_rules(services, policies):
        #returns list of violations
    violations = []
    compliant_services = []

    for service in services:
        service_violated = False
        
        for policy in policies:
            if violates(service, policy):
                service_violated = True
                violations.append({
                    "service_id": service["service_id"],
                    "policy_id": policy["policy_id"],
                    "description": policy["description"]
                })
        if not service_violated:
            compliant_services.append(service["service_id"])

    return violations, compliant_services