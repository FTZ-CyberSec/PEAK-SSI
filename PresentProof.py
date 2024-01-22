import requests
import json

# Set the base URL for the agent
base_url = 'http://82.165.247.238'

# Function to send a presentation request
def send_presentation_request(connection_id):
    url = f'{base_url}:11000/present-proof-2.0/send-request'
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}

    data = {
        "auto_verify": True,
        "comment": "string",
        "connection_id": connection_id,
        "presentation_request": {
            "indy": {
                "name": "Proof request",
                "non_revoked": {"to": 1640995199},
                "nonce": "1",
                "requested_attributes": {
                    "additionalProp1": {"name": "Name", "non_revoked": {"to": 1704902269}},
                    "additionalProp2": {"name": "Anschrift", "non_revoked": {"to": 1704902269}},
                    "additionalProp3": {"name": "Geburtsdatum", "non_revoked": {"to": 1704902269}},
                },
                "requested_predicates": {},
                "version": "1.0"
            }
        },
        "trace": False
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Function to get presentation records (prover side)
def get_presentation_records(th_id):
    url = f'{base_url}:11001/present-proof-2.0/records?thread_id={th_id}'
    headers = {'accept': 'application/json'}

    response = requests.get(url, headers=headers)
    return response.json()

# Function to get matching credentials (prover side)
def get_matching_credentials(pres_ex_id):
    url = f'{base_url}:11001/present-proof-2.0/records/{pres_ex_id}/credentials'
    headers = {'accept': 'application/json'}

    response = requests.get(url, headers=headers)
    return response.json()

# Function to send presentation
def send_presentation(pres_ex_id):
    url = f'{base_url}:11001/present-proof-2.0/records/{pres_ex_id}/send-presentation'
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}

    data = {
        "indy": {
            "requested_attributes": {
                "additionalProp1": {"cred_id": "be2dbf70-6b33-40d1-a123-c68aa15a2666", "revealed": True},
                "additionalProp2": {"cred_id": "be2dbf70-6b33-40d1-a123-c68aa15a2666", "revealed": True},
                "additionalProp3": {"cred_id": "be2dbf70-6b33-40d1-a123-c68aa15a2666", "revealed": True},
            },
            "requested_predicates": {},
            "self_attested_attributes": {},
            "trace": False
        },
        "trace": True
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Example usage
connection_id = "95cf3668-5671-43b4-85b8-ce36867e1a3b"
presentation_request_response = send_presentation_request(connection_id)
print("Presentation Request Response:")
print(json.dumps(presentation_request_response, indent=2))

presentation_records = get_presentation_records(presentation_request_response['thread_id'])
print("\nPresentation Records:")
print(json.dumps(presentation_records, indent=2))

if presentation_records["results"]:
    pres_ex_id = presentation_records["results"][0]["pres_ex_id"]
    matching_credentials = get_matching_credentials(pres_ex_id)
    print("\nMatching Credentials:")
    print(json.dumps(matching_credentials, indent=2))

    send_presentation_response = send_presentation(pres_ex_id)
    print("\nSend Presentation Response:")
    print(json.dumps(send_presentation_response, indent=2))
