import requests
from datetime import datetime


def create_credential(name, address, dob, id_number):
    current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    data = {
        "auto_remove": True,
        "comment": "string",
        "connection_id": "fac7a08e-b1ec-4b72-a025-994e2f718704",
        "credential_preview": {
            "@type": "issue-credential/2.0/credential-preview",
            "attributes": [
                {"name": "Name", "value": name},
                {"name": "Anschrift", "value": address},
                {"name": "Geburtsdatum", "value": dob}
            ]
        },
        "filter": {
            "indy": {
                "cred_def_id": "X8THiyo3G9EDYcNfg4aM2f:3:CL:10:persoTagRegistry",
                "issuer_did": "X8THiyo3G9EDYcNfg4aM2f",
                "schema_id": "X8THiyo3G9EDYcNfg4aM2f:2:persoCert:1.0",
                "schema_issuer_did": "X8THiyo3G9EDYcNfg4aM2f",
                "schema_name": "persoCert",
                "schema_version": "1.0"
            },
            "ld_proof": {
                "credential": {
                    "@context": ["https://www.w3.org/2018/credentials/v1", "https://w3id.org/citizenship/v1"],
                    "credentialSubject": {},
                    "description": "PEAK persoCert",
                    "identifier": id_number,
                    "issuanceDate": current_time,
                    "issuer": "did:sov:X8THiyo3G9EDYcNfg4aM2f",
                    "name": "persoCert",
                    "type": ["VerifiableCredential", "PermanentResidentCard"]
                },
                "options": {"proofType": "Ed25519Signature2018"}
            }
        },
        "trace": True
    }

    return data


def send_credential_proposal(data):
    url = 'http://82.165.247.238:11001/issue-credential-2.0/send-proposal'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.post(url, json=data, headers=headers)
    response_content = response.json()


    if response.status_code == 200:
        #return the shared thread id and the cred_ex_id of the proposed holder
        return response_content['thread_id'], response_content['cred_ex_id']
    else:
        print(f'Error sending credential proposal. Status code: {response.status_code}, Response: {response.text}')


def send_credential_function(ceID, port, function):
    if function == "issue" or function == "store":
        url = f"http://82.165.247.238:{port}/issue-credential-2.0/records/{ceID}/{function}"
    else:
        url = f"http://82.165.247.238:{port}/issue-credential-2.0/records/{ceID}/send-{function}"
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    if function != "issue":
        response = requests.post(url, data=None, headers=headers)
    else:
        response = requests.post(url, json={"comment": "Hier ist ihr persoCert"}, headers=headers)

    if response.status_code == 200:
        print(f"Credential {function}ed successfully")
    else:
        print(f'Error sending credential {function}. Status code: {response.status_code}, Response: {response.text}')


# Replace these values with your actual data
print("Bitte Vor- und Nachnamen eintragen: ")
name = input()
print("Bitte Adresse(Straße & Hausnummer, PLZ & Stadt, Land) eintragen: ")
address = input()
print("Bitte Geburtsdatum eintragen(Format: YYYY-MM-DD): ")
dob = input()
id_number_counter = 3  # Starting with 000002

# Convert the counter to a formatted string
id_number = f"{id_number_counter:06d}"

# Create the credential data
credential_data = create_credential(name, address, dob, id_number)

# Send the credential proposal
thread_id, cred_ex_id_holder = send_credential_proposal(credential_data)

# Get issuer cred_ex_id for the credential dance
cred_ex_id_issuer = requests.get(f"http://82.165.247.238:11000/issue-credential-2.0/records?role=issuer&state=proposal-received&thread_id={thread_id}", data=None)
cred_ex_id_issuer = cred_ex_id_issuer.json()
cred_ex_id_issuer = cred_ex_id_issuer['results'][0]['cred_ex_record']['cred_ex_id']
# print(cred_ex_id_issuer)

# proposed credential has to be offered, requested, issued and the stored
send_credential_function(cred_ex_id_issuer, 11000, "offer")
send_credential_function(cred_ex_id_holder, 11001, "request")
send_credential_function(cred_ex_id_issuer, 11000, "issue")
send_credential_function(cred_ex_id_holder, 11001, "store")


