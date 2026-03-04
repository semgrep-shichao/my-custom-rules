import os
import yaml
import requests
import sys

MODE = 'MODE_MONITOR'
BASE_URL = 'https://semgrep.dev/api/v1/deployments'


def get_deployment_id(headers):
    """
    Gets the deployment slug for use in other API calls.
    API tokens are currently per-deployment, so there's no need to 
    iterate or paginate.
    """
    r = requests.get(BASE_URL, headers=headers)
    if r.status_code != 200:
        sys.exit(f'Get failed: {r.text}')
    data = r.json()
    print(data)
    deployment_id = data['deployments'][0].get('id')
    print(f'Accessing org: {deployment_id}')
    return deployment_id


def get_policy_id(deployment_id: str, headers) -> str:
    url = f"{BASE_URL}/{deployment_id}/policies"
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Error fetching policies: {response.status_code} - {response.text}")
    
    policies = response.json().get("policies", [])
    
    for policy in policies:
        if policy.get("name") == "Global Policy":
            return policy.get("id")
    
    raise Exception("Global Policy not found")

def find_yaml_files(directory):
    """Recursively finds all YAML files in a given directory."""
    yaml_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.yaml', '.yml')):
                yaml_files.append(os.path.join(root, file))
    return yaml_files


def extract_ids_from_yaml(file_path):
    """Extracts the 'id' field from a given YAML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            if isinstance(data, dict) and 'rules' in data and isinstance(data['rules'], list):
                return [rule['id'] for rule in data['rules'] if 'id' in rule]
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return []



def update_policy(deployment_id, policy_id, policy_mode, path, headers):
    """
    Updates a policy for a given deployment on Semgrep.
    
    Args:
        deployment_id (str): The ID of the deployment.
        policy_id (str): The ID of the policy to update.
        policy_mode (str): The mode of the policy (e.g., "MODE_BLOCK").
        path (str): The path of the rule.
        headers (str): heders for the authentication.
    
    Returns:
        dict: The JSON response from the API.
    """
    url = f"{BASE_URL}/{deployment_id}/policies/{policy_id}?rulePath={path}&policyMode={policy_mode}"
    print(url)
    response = requests.put(url, headers=headers)
    print(response.json())
    return response.json()



def main(directory):
    try:  
        SEMGREP_APP_TOKEN = os.getenv("SEMGREP_APP_TOKEN") 
    except KeyError: 
        print("Please set the environment variable SEMGREP_APP_TOKEN") 
        sys.exit(1)
    headers = {"Accept": "application/json", "Authorization": "Bearer " + SEMGREP_APP_TOKEN}

    deployment_id = get_deployment_id(headers)
    policy_id = get_policy_id(deployment_id, headers)
    yaml_files = find_yaml_files(directory)
    for yaml_file in yaml_files:
        ids = extract_ids_from_yaml(yaml_file)
        if ids:
            print(f"File: {yaml_file}")
            for rule_id in ids:
                print(f"  ID: {rule_id}")
                update_policy(deployment_id, policy_id, MODE, rule_id, headers)

if __name__ == "__main__":
    main("./rules")
