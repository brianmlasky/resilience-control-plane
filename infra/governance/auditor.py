import hcl2
import json
import subprocess
import sys
import os

def get_terraform_json(file_path):
    """Loads and parses the Terraform HCL file."""
    clean_path = file_path.strip()
    with open(clean_path, 'r') as file:
        return hcl2.load(file)

def run_governance_check(tf_json):
    """Flattens the data and evaluates it against OPA policies."""
    # Flatten the resource list
    flattened = []
    for entry in tf_json.get("resource", []):
        for resource_type in entry:
            for resource_name in entry[resource_type]:
                item = entry[resource_type][resource_name]
                flattened.append(item)
    
    data_to_send = {"resources": flattened}
    
    # Save the normalized data for OPA
    with open('plan.json', 'w') as f:
        json.dump(data_to_send, f)
    
    # Execute OPA using the input file
    policy_path = os.path.join(os.path.dirname(__file__), 'policy.rego')
    
    result = subprocess.run(
        ['opa', 'eval', '--format', 'json', '--data', policy_path, '--input', 'plan.json', 'data.terraform.governance.violation'],
        capture_output=True, text=True
    )
    
    # Parse the OPA JSON response
    opa_output = json.loads(result.stdout)
    violations = []
    
    # Extract keys from the "value" object if it exists
    for res in opa_output.get("result", []):
        for expr in res.get("expressions", []):
            # The violations are returned as keys in the value dictionary
            violations = list(expr.get("value", {}).keys())
    
    return violations

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 auditor.py <filename>")
        sys.exit(1)
        
    try:
        target_file = sys.argv[1]
        tf_data = get_terraform_json(target_file)
        violations = run_governance_check(tf_data)
        
        # Display violations or pass
        if violations:
            for v in violations:
                print(f"BLOCKING DEPLOYMENT: {v}")
            sys.exit(1)
        else:
            print("POLICY PASSED: Proceeding to deployment.")
            
    except Exception as e:
        print(f"Error during audit: {e}")
        sys.exit(1)