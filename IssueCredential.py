import requests
import json
from datetime import datetime, timezone

# Replace these values with the actual IP addresses and port numbers of your ACA-py instances
AGENT1_URL = "http://82.165.247.238:11000"
AGENT2_URL = "http://82.165.247.238:11001"
CONNECTION_ID_AGENT1 = "74cc0205-04a2-44d1-afe8-ce3cc90d9ee1"
CONNECTION_ID_AGENT2 =  "246eed58-3ce4-4528-929f-366b0f3e9238"

# Function to send a POST request to a given endpoint
def send_post_request(url, endpoint, payload):
    response = requests.post(f"{url}/{endpoint}", headers={'accept': 'application/json', 'Content-Type': 'application/json'}, json=payload)
    response.raise_for_status()
    return response.json()

# Step 1: Create DIDs for Agent 1
agent_did_create_payload = {
    "method": "key",
    "options": {
        "key_type": "ed25519"
    }
}

agent1_did = send_post_request(AGENT1_URL, "wallet/did/create", agent_did_create_payload)
agent1_did = agent1_did["result"]["did"]
print(agent1_did)
# Step 2: Create DIDs for Agent 2

agent2_did = send_post_request(AGENT2_URL, "wallet/did/create", agent_did_create_payload)
agent2_did = agent2_did["result"]["did"]
print(agent2_did)

# Step 3: Send credential offer from Agent 1 to Agent 2
current_time_utc = datetime.now(timezone.utc)
formatted_time = current_time_utc.strftime('%Y-%m-%dT%H:%M:%SZ')

# This is the Credential, all fields except for Context, options, and the ones with assigned variables can be altered
offer_payload = {
    "connection_id": CONNECTION_ID_AGENT1,
    "filter": {
        "ld_proof": {
            "credential": {
                "@context": [
                    "https://www.w3.org/2018/credentials/v1",
                    "https://www.w3.org/2018/credentials/examples/v1"
                ],
                "type": ["VerifiableCredential", "TestCredential"],
                "issuer": agent1_did,
                "issuanceDate": formatted_time,
                "credentialSubject": {
                    "id": agent2_did,
                    "givenName": "Bob",
                    "familyName": "Bobson",
                    "degree": {
                        "type": "MastersDegree",
                        "degreeType": "Graduate",
                        "name": "Master of Bobery"
                    },
                    "college": "Alices College"
                }
            },
            "options": {
                "proofType": "Ed25519Signature2018"
            }
        }
    }
}

offer_response = send_post_request(AGENT1_URL, "issue-credential-2.0/send-offer", offer_payload)

# Step 3.5: Find out cred_ex_id for Agent 2 by looking up the issue credential records (thread id is thankfully the same for both agents)
record_response = requests.get(f"{AGENT2_URL}/issue-credential-2.0/records?connection_id={CONNECTION_ID_AGENT2}&&role=holder&state=offer-received&thread_id={offer_response['thread_id']}", data=None)
record_response = record_response.json()
record_response = record_response['results'][0]['cred_ex_record']
print(record_response)

# Step 4: Send credential request from Agent 2 to Agent 1
request_payload = {
    "holder_did": agent2_did
}

request_response = send_post_request(AGENT2_URL, "issue-credential-2.0/records/" + record_response["cred_ex_id"] + "/send-request", request_payload)

# Step 5: Issue the credential from Agent 1
issue_payload = {
    "comment": "Here you go"
}

issue_response = send_post_request(AGENT1_URL, "issue-credential-2.0/records/" + offer_response["cred_ex_id"] + "/issue", issue_payload)

# Step 6: Store the credential by Agent 2
store_payload = {
    "credential_id": offer_response["cred_ex_id"]
}

store_response = send_post_request(AGENT2_URL, "issue-credential-2.0/records/" + record_response["cred_ex_id"] + "/store", store_payload)

# Print the final results
print("Agent 1 DID:", agent1_did)
print("Agent 2 DID:", agent2_did)
print("Credential Exchange ID:", offer_response["cred_ex_id"])
print("Credential Issued Successfully!")
