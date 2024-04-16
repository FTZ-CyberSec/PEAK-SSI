import requests
import json
import random
import datetime
import time
from createVC import create_vc
from config import BASE_URL, platform_DID, grid_DID


# Function to perform the credential exchange
def issue_credential(type, holder_port=11002):
    id = random.randint(00000, 99999)
    match type:
        case "persoCert":
            issuer_port = 11000
        case "ownerCert":
            issuer_port = 11000
        case "gridCert":
            issuer_port = 11001
        case "assetCert":
            issuer_port = 11001
        case "warrantCert":
            issuer_port = 11000
    # Define the data for the credential proposal
    credential_proposal_data = create_vc(type, holder_port)

    # Send Credential Proposal
    response = requests.post(f'http://{BASE_URL}:{holder_port}/issue-credential-2.0/send-proposal',
                             headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                             data=json.dumps(credential_proposal_data))

    # Print response
    print("Credential Proposal Response:")
    print(response.json())
    print("\n")
    time.sleep(0.1)
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
            f"http://{BASE_URL}:{issuer_port}/issue-credential-2.0/records",
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
            f'http://{BASE_URL}:{issuer_port}/issue-credential-2.0/records/{cred_ex_id_issuer}/send-offer',
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
            f'http://{BASE_URL}:{holder_port}/issue-credential-2.0/records/{cred_ex_id_holder}/send-request',
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
            f'http://{BASE_URL}:{issuer_port}/issue-credential-2.0/records/{cred_ex_id_issuer}/issue',
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
            f'http://{BASE_URL}:{holder_port}/issue-credential-2.0/records/{cred_ex_id_holder}/store',
            headers={'accept': 'application/json', 'Content-Type': 'application/json'},
            data=json.dumps({"credential_id": type}))
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

def present_credential(type, holder_port=11002):
    match type:
        case "persoCert":
            issuer_port = 11000
            which = platform_DID
            vc = ["name", "adress", "birthdate"]
        case "ownerCert":
            issuer_port = 11000
            which = platform_DID
            vc = ["lizenznummer"]
        case "gridCert":
            issuer_port = 11001
            which = grid_DID
            vc = ["zaehlerID", "smartMeterID", "marktlokation", "HEMS", "steuerbox", "verbrauchpA"]
        case "assetCert":
            issuer_port = 11001
            which = grid_DID
            vc = ["anlagenTyp", "stellschritteP", "Pmax", "Pmin", "energieArt", "steuerbarkeit", "speicherKapa"]
        case "warrantCert":
            issuer_port = 11000
            which = platform_DID
            vc = ["handelsRichtung", "maxEinspeisung", "maxLast", "handelsArt"]
    attributes = {}
    current_timestamp = int(datetime.datetime.now().timestamp())
    for attribute in vc:
        attributes[attribute] = {"name": attribute, "non_revoked": {"to": current_timestamp}}
    # Fetch the connection ID of the verifier agent
    invitation_key = requests.get(f'http://{BASE_URL}:{holder_port}/connections?state=active&their_public_did={which}').json()['results'][0].get(
        'invitation_key')
    params = {
        'invitation_key': invitation_key,
        'state': 'active'
    }
    time.sleep(0.1)
    verifier_connection_id = \
        requests.get(f"http://{BASE_URL}:{issuer_port}/connections", params=params).json()['results'][0]['connection_id']
    url = f'http://{BASE_URL}:{issuer_port}/present-proof-2.0/send-request'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    payload = {
        "auto_verify": False,
        "auto_remove": False,
        "comment": "please confirm",
        "connection_id": verifier_connection_id,
        "presentation_request": {
            "indy": {
                "name": "Proof request",
                "non_revoked": {
                    "to": current_timestamp
                },
                "nonce": "1",
                "requested_attributes": attributes,
                "requested_predicates": {},
                "version": "1.0"
            }
        },
        "trace": False
    }
    # Sending POST request to ACA-Py
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code != 200:
        print("Failed to send presentation request.")
        print(f"Status Code: {response.status_code}, Response: {response.text}")
        return None

    thread_id = response.json()["thread_id"]
    pres_ex_id_issuer = response.json()["pres_ex_id"]
    # print(thread_id)
    # print(pres_ex_id_issuer)

    # Fetch the presentation record on the verifier agent
    time.sleep(0.1)
    try:
        # Make the GET request
        params = {
            'thread_id': thread_id
        }
        fetch_record_response = requests.get(
            f"http://{BASE_URL}:{holder_port}/present-proof-2.0/records",
            headers={'accept': 'application/json'}, params=params)

        # Check if the response was successful (status code 200)
        if fetch_record_response.status_code != 200:
            # Handle responses with error status codes
            print(f"Error fetching presentation record: {fetch_record_response.status_code}")
            print(fetch_record_response.text)
    except requests.exceptions.RequestException as e:
        # Handle requests exceptions (e.g., network errors, timeouts)
        print(f"Request failed: {e}")

    if fetch_record_response.json()['results']:
        pres_ex_id_holder = fetch_record_response.json()['results'][0]['pres_ex_id']
    else:
        return "No credential exchange record found"

    # print(pres_ex_id_holder)

    # Fetch the credentials that fit the request on the holder agent
    try:
        # Make the GET request
        fetch_record_response = requests.get(
            f"http://{BASE_URL}:{holder_port}/present-proof-2.0/records/{pres_ex_id_holder}/credentials",
            headers={'accept': 'application/json'})

        # Check if the response was successful (status code 200)
        if fetch_record_response.status_code != 200:
            # Handle responses with error status codes
            print(f"Error fetching credentials: {fetch_record_response.status_code}")
            print(fetch_record_response.text)

    except requests.exceptions.RequestException as e:
        # Handle requests exceptions (e.g., network errors, timeouts)
        print(f"Request failed: {e}")
    # Build Presentation attributes
    req_attributes = {}
    for attribute in vc:
        req_attributes[attribute] = {'cred_id': type, 'revealed': True}
    time.sleep(0.1)
    # Create Presentation from Holder
    presentation_data = {
        "indy": {
            "requested_attributes": req_attributes,
            "requested_predicates": {
            },
            "self_attested_attributes": {
            },
            "trace": False
        },
        "trace": True
    }
    # Send Presentation from Holder
    try:
        presentation_response = requests.post(
            f'http://{BASE_URL}:{holder_port}/present-proof-2.0/records/{pres_ex_id_holder}/send-presentation',
            headers={'accept': 'application/json', 'Content-Type': 'application/json'},
            data=json.dumps(presentation_data))
        # Check if the response was successful (status code 200)
        if presentation_response.status_code != 200:
            # Handle responses with error status codes
            print(f"Error sending presentation: {presentation_response.status_code}")
            print(presentation_response.text)
    except requests.exceptions.RequestException as e:
        # Handle requests exceptions (e.g., network errors, timeouts)
        print(f"Request failed: {e}")

    time.sleep(0.1)
    # Verify Presentation
    try:
        verify_response = requests.post(
            f'http://{BASE_URL}:{issuer_port}/present-proof-2.0/records/{pres_ex_id_issuer}/verify-presentation',
            headers={'accept': 'application/json', 'Content-Type': 'application/json'},
            data=json.dumps({}))
        # Check if the response was successful (status code 200)
        if verify_response.status_code == 200:
            # Process the successful response here
            print("Verify Presentation Response:")
            print(verify_response.json())
            print("\n")
            return verify_response.json()
        else:
            # Handle responses with error status codes
            print(f"Error verifying presentation: {verify_response.status_code}")
            print(verify_response.text)
    except requests.exceptions.RequestException as e:
        # Handle requests exceptions (e.g., network errors, timeouts)
        print(f"Request failed: {e}")

def define_credential(type):
    match type:
        case "persoCert":
            issuer_port = 11000
            attributes = ["name", "adress", "birthdate"]
        case "ownerCert":
            issuer_port = 11000
            attributes = ["lizenznummer"]
        case "gridCert":
            issuer_port = 11001
            attributes = ["zaehlerID", "smartMeterID", "marktlokation", "HEMS", "steuerbox", "verbrauchpA"]
        case "assetCert":
            issuer_port = 11001
            attributes = ["anlagenTyp", "stellschritteP", "Pmax", "Pmin", "energieArt", "steuerbarkeit", "speicherKapa"]
        case "warrantCert":
            issuer_port = 11000
            attributes = ["handelsRichtung", "maxEinspeisung", "maxLast", "handelsArt"]
    name = type

    # Create Schema
    schema_data = {
        "attributes": attributes,
        "schema_name": name,
        "schema_version": "1.0"
    }
    response = requests.post(f'http://{BASE_URL}:{issuer_port}/schemas',
                             headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                             data=json.dumps(schema_data))
    print(response.json())
    print("\n")
    # Extract the value seqNo from the response
    seqNo = response.json()["sent"]["schema"]["seqNo"]
    time.sleep(0.1)
    # Create Credential Definition
    credential_definition_data = {
        "revocation_registry_size": 10000,
        "schema_id": f"{BASE_URL}:2:{name}:1.0",
        "support_revocation": True,
        "tag": "default"
    }
    response = requests.post(f'http://{BASE_URL}:{issuer_port}/credential-definitions',
                             headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                             data=json.dumps(credential_definition_data))
    print(response.json())
    print("\n")
    time.sleep(0.1)
    # Create Revocation Registry
    revocation_registry_data = {
        "credential_definition_id": f"{BASE_URL}:3:CL:{seqNo}:default",
        "max_cred_num": 10000
    }
    response = requests.post(f'http://{BASE_URL}:{issuer_port}/revocation/create-registry',
                             headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                             data=json.dumps(revocation_registry_data))
    print(response.json())
