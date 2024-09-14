# >>> Payman Afshari - 2024 <<<
import csv
import requests
import argparse
# Function to add object to FortiGate
def add_object_to_fortigate(fgt_ip, api_token, data):
    api_url = f"https://{fgt_ip}/api/v2/cmdb/firewall/address/"
    
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

    # Print data for debugging
    print(f"Sending data to FortiGate: {data}")
    
    response = requests.post(api_url, headers=headers, json=data, verify=False)
    
    if response.status_code == 200:
        print(f"Successfully added object: {data['name']}")
    else:
        print(f"Failed to add object: {data['name']}, Status Code: {response.status_code}, Response: {response.text}")

# Function to create address object
def create_address_object(row, fgt_ip, api_token):
    obj_type = row['type']
    data = {
        "name": row['name'],
        "comment": row['comment'],
        "color": "0"  # Optional: setting the color to 0 (default)
    }
    
    if obj_type == 'ipmask':
        data["subnet"] = row['subnet']
    elif obj_type == 'iprange':
        data["start-ip"] = row['start_ip']
        data["end-ip"] = row['end_ip']
        data["type"] = "iprange"
    elif obj_type == 'fqdn':
        data["fqdn"] = row['fqdn']
        data["type"] = "fqdn"
    elif obj_type == 'geography':
        data["country"] = row['country']
        data["type"] = "geography"
    elif obj_type == 'wildcard':
        data["subnet"] = row['subnet']
        data["type"] = "wildcard"
    elif obj_type == 'mac':
        # For MAC Address, correctly formatted as list of dicts
        if row['macaddr']:
            data["type"] = "mac"
            data["macaddr"] = [{"macaddr": row['macaddr']}]
        else:
            print(f"Error: No MAC address provided for {row['name']}")
            return  # Skip adding this object if macaddr is missing
    elif obj_type == 'wildcard-fqdn':
        data["fqdn"] = row['fqdn']
        data["type"] = "wildcard-fqdn"

    # Add the object to FortiGate
    add_object_to_fortigate(fgt_ip, api_token, data)

# Main function to handle CSV and arguments
def main():
    # Argument parsing
    parser = argparse.ArgumentParser(description="FortiGate Address Importer")
    parser.add_argument("--ip", required=True, help="FortiGate IP address")
    parser.add_argument("--token", required=True, help="FortiGate API token")
    parser.add_argument("--file", required=True, help="Path to the CSV file")

    args = parser.parse_args()

    # Reading CSV file
    with open(args.file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            create_address_object(row, args.ip, args.token)

if __name__ == "__main__":
    main()
