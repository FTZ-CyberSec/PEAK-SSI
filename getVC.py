import requests
import json
import random
import datetime
import time

BASE_URL = 'http://82.165.247.238'


# Function to perform the credential exchange
def perform_credential_exchange(holder_port, issuer_port=11000):
    id = random.randint(00000, 99999)
    # Define the data for the credential proposal
    credential_proposal_data = {
        "auto_remove": False,
        "comment": "Please give me permission to trade",
        "connection_id": requests.get(f'{BASE_URL}:{holder_port}/connections').json()['results'][0].get(
            'connection_id'),
        "credential_preview": {
            "@type": "issue-credential/2.0/credential-preview",
            # TODO: Add a list of attribute sets and find a way to input values
            "attributes": [
                {"name": "ownerID", "value": f"de{id}"},
                {"name": "energyAgentID", "value": f"ea{id}"},
                {"name": "gridID", "value": f"p21033h{id}"},
                {"name": "maxProd", "value": f"{random.randint(1000, 10000)}"},
                {"name": "tradeDirection", "value": "all"},
                {"name": "assetIDs", "value": "PV1, PV2, PV3"},
                {"name": "storageCapacity", "value": f"{random.randint(7000, 20000)}"}
            ]
        },
        # TODO: Add a list of schemas to choose from
        "filter": {
            "indy": {
                "cred_def_id": "X8THiyo3G9EDYcNfg4aM2f:3:CL:12:authProsumers",
                "issuer_did": "X8THiyo3G9EDYcNfg4aM2f",
                "schema_id": "X8THiyo3G9EDYcNfg4aM2f:2:tradeAuth:1.0",
                "schema_issuer_did": "X8THiyo3G9EDYcNfg4aM2f",
                "schema_name": "tradeAuth",
                "schema_version": "1.0"
            },
            "ld_proof": {
                "credential": {
                    "@context": [
                        "https://www.w3.org/2018/credentials/v1",
                        "https://www.w3.org/2018/credentials/examples/v1"
                    ],
                    "credentialSubject": {"type": ["Person", "Prosumer"]},
                    "issuanceDate": f"{datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')}",
                    "issuer": "did:sov:X8THiyo3G9EDYcNfg4aM2f",
                    "name": "P2P Trading Licence",
                    "type": ["VerifiableCredential", "P2PTradingLicence"],
                },
                "options": {"proofType": "Ed25519Signature2018"}
            }
        },
        "trace": True
    }

    # Send Credential Proposal
    response = requests.post(f'{BASE_URL}:{holder_port}/issue-credential-2.0/send-proposal',
                             headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                             data=json.dumps(credential_proposal_data))

    # Print response
    print("Credential Proposal Response:")
    print(response.json())
    print("\n")

    thread_id = response.json()["thread_id"]
    print(thread_id)
    cred_ex_id_holder = response.json()["cred_ex_id"]

    # Fetch Credential Record on Issuer Agent
    time.sleep(0.5)
    try:
        # Make the GET request
        params = {
            'thread_id': thread_id
        }
        fetch_record_response = requests.get(
            f"{BASE_URL}:{issuer_port}/issue-credential-2.0/records",
            headers={'accept': 'application/json'}, params=params)

        # Check if the response was successful (status code 200)
        if fetch_record_response.status_code == 200:
            # Process the successful response here
            print("Fetch Credential Record Response:")
            print(fetch_record_response.json())
            print("\n")
        else:
            # Handle responses with error status codes
            print(f"Error fetching credential record: {fetch_record_response.status_code}")
            print(fetch_record_response.text)
    except requests.exceptions.RequestException as e:
        # Handle requests exceptions (e.g., network errors, timeouts)
        print(f"Request failed: {e}")

    if fetch_record_response.json()['results']:
        cred_ex_id_issuer = fetch_record_response.json()['results'][0]['cred_ex_record']['cred_ex_id']
    else:
        return "No credential exchange record found"
    # TODO: Add control algorithm to check the request
    # Send Offer from Issuer
    try:
        offer_response = requests.post(
            f'{BASE_URL}:{issuer_port}/issue-credential-2.0/records/{cred_ex_id_issuer}/send-offer',
            headers={'accept': 'application/json', 'Content-Type': 'application/json'},
            data=json.dumps({}))
        # Check if the response was successful (status code 200)
        if offer_response.status_code == 200:
            # Process the successful response here
            print("Offer Credential to Holder:")
            print(offer_response.json())
            print("\n")
        else:
            # Handle responses with error status codes
            print(f"Error fetching credential record: {offer_response.status_code}")
            print(offer_response.text)
    except requests.exceptions.RequestException as e:
        # Handle requests exceptions (e.g., network errors, timeouts)
        print(f"Request failed: {e}")
    time.sleep(0.5)

    # Request Credential from Holder
    try:
        request_credential_response = requests.post(
            f'{BASE_URL}:{holder_port}/issue-credential-2.0/records/{cred_ex_id_holder}/send-request',
            headers={'accept': 'application/json', 'Content-Type': 'application/json'},
            data=json.dumps({}))
        # Check if the response was successful (status code 200)
        if request_credential_response.status_code == 200:
            # Process the successful response here
            print("Request Credential Response:")
            print(request_credential_response.json())
            print("\n")
        else:
            # Handle responses with error status codes
            print(f"Error fetching credential record: {request_credential_response.status_code}")
            print(request_credential_response.text)
    except requests.exceptions.RequestException as e:
        # Handle requests exceptions (e.g., network errors, timeouts)
        print(f"Request failed: {e}")
    time.sleep(0.5)
    # Issue Credential
    try:
        issue_credential_response = requests.post(
            f'{BASE_URL}:{issuer_port}/issue-credential-2.0/records/{cred_ex_id_issuer}/issue',
            headers={'accept': 'application/json', 'Content-Type': 'application/json'},
            data=json.dumps({"comment": "there you go"}))
        # Check if the response was successful (status code 200)
        if issue_credential_response.status_code == 200:
            # Process the successful response here
            print("Issue Credential Response:")
            print(issue_credential_response.json())
            print("\n")
        else:
            # Handle responses with error status codes
            print(f"Error fetching credential record: {issue_credential_response.status_code}")
            print(issue_credential_response.text)
    except requests.exceptions.RequestException as e:
        # Handle requests exceptions (e.g., network errors, timeouts)
        print(f"Request failed: {e}")
    time.sleep(0.5)
    # Store Credential
    try:
        store_credential_response = requests.post(
            f'{BASE_URL}:{holder_port}/issue-credential-2.0/records/{cred_ex_id_holder}/store',
            headers={'accept': 'application/json', 'Content-Type': 'application/json'},
            data=json.dumps({"credential_id": "tradeAuth"}))
        # Check if the response was successful (status code 200)
        if store_credential_response.status_code == 200:
            # Process the successful response here
            print("Store Credential Response:")
            print(store_credential_response.json())
            print("\n")
        else:
            # Handle responses with error status codes
            print(f"Error fetching credential record: {store_credential_response.status_code}")
            print(store_credential_response.text)
    except requests.exceptions.RequestException as e:
        # Handle requests exceptions (e.g., network errors, timeouts)
        print(f"Request failed: {e}")

    # Check if Credential is in Wallet
    try:
        check_credential_response = requests.get(f'http://{BASE_URL}:{holder_port}/credentials',
                                                 headers={'accept': 'application/json'})
        # Check if the response was successful (status code 200)
        if check_credential_response.status_code == 200:
            # Process the successful response here
            print("Check Credential Response:")
            print(check_credential_response.json())
            print("\n")
        else:
            # Handle responses with error status codes
            print(f"Error fetching credential record: {check_credential_response.status_code}")
            print(check_credential_response.text)
    except requests.exceptions.RequestException as e:
        # Handle requests exceptions (e.g., network errors, timeouts)
        print(f"Request failed: {e}")


# Example usage
perform_credential_exchange(11009)