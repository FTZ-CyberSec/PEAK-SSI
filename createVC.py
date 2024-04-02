import random
from config import platform_DID, grid_DID

def create_vc(type):
    # Define the data for the credential proposal
    match type:
        case "persoCert":
            attributes = [{"name": "name", "value": input("Vor- und Nachname: ")},
                          {"name": "adress", "value": input("Straße, Hnr., PLZ, Ort: ")},
                          {"name": "birthdate", "value": input("Geburtsdatum: ")}]
            # used for the ld_proof
            issuer = platform_DID
            indy = {
                "cred_def_id": f"{issuer}:3:CL:12:default",
                "issuer_did": issuer,
                "schema_id": f"{issuer}:2:persoCert:1.0",
                "schema_issuer_did": issuer,
                "schema_name": "persoCert",
                "schema_version": "1.0"
            }
            # used for the ld_proof and as second part of the type
            name = "persoCert"

        case "ownerCert":
            {"name": "ownerID", "value": f"de{id}"},
            {"name": "energyAgentID", "value": f"ea{id}"},
            {"name": "gridID", "value": f"p21033h{id}"},
            {"name": "maxProd", "value": f"{random.randint(1000, 10000)}"},
            {"name": "tradeDirection", "value": "all"},
            {"name": "assetIDs", "value": "PV1, PV2, PV3"},
            {"name": "storageCapacity", "value": f"{random.randint(7000, 20000)}"}
        case "gridCert":
            {"name": "ownerID", "value": f"de{id}"},
            {"name": "energyAgentID", "value": f"ea{id}"},
            {"name": "gridID", "value": f"p21033h{id}"},
            {"name": "maxProd", "value": f"{random.randint(1000, 10000)}"},
            {"name": "tradeDirection", "value": "all"},
            {"name": "assetIDs", "value": "PV1, PV2, PV3"},
            {"name": "storageCapacity", "value": f"{random.randint(7000, 20000)}"}
        case "assetCert":
            {"name": "ownerID", "value": f"de{id}"},
            {"name": "energyAgentID", "value": f"ea{id}"},
            {"name": "gridID", "value": f"p21033h{id}"},
            {"name": "maxProd", "value": f"{random.randint(1000, 10000)}"},
            {"name": "tradeDirection", "value": "all"},
            {"name": "assetIDs", "value": "PV1, PV2, PV3"},
            {"name": "storageCapacity", "value": f"{random.randint(7000, 20000)}"}
        case "warrantCert":
            {"name": "ownerID", "value": f"de{id}"},
            {"name": "energyAgentID", "value": f"ea{id}"},
            {"name": "gridID", "value": f"p21033h{id}"},
            {"name": "maxProd", "value": f"{random.randint(1000, 10000)}"},
            {"name": "tradeDirection", "value": "all"},
            {"name": "assetIDs", "value": "PV1, PV2, PV3"},
            {"name": "storageCapacity", "value": f"{random.randint(7000, 20000)}"}
        case _:
            print("Invalid type")
    """credential_proposal_data = {
        "auto_remove": False,
        "comment": "Please give me permission to trade",
        "connection_id": requests.get(f'{BASE_URL}:{holder_port}/connections').json()['results'][0].get(
            'connection_id'),
        "credential_preview": {
            "@type": "issue-credential/2.0/credential-preview",
            # TODO: Add a list of attribute sets and find a way to input values
            "attributes": attributes
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
    }"""
    return attributes, indy, issuer, name
