import random
import requests
import datetime
from config import platform_DID, grid_DID, BASE_URL, vc_types

def create_vc(type: vc_types, holder_port: int = 11002):
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
        case "ownerCert":
            attributes = [{"name": "lizenznummer", "value": f"{random.randint(0, 100000)}"}]
            issuer = platform_DID
            indy = {
                "cred_def_id": f"{issuer}:3:CL:18:default",
                "issuer_did": issuer,
                "schema_id": f"{issuer}:2:ownerCert:1.0",
                "schema_issuer_did": issuer,
                "schema_name": "ownerCert",
                "schema_version": "1.0"
            }
        case "gridCert":
            id = random.randint(0, 10000)
            dot = "."
            attributes = [
            {"name": "zaehlerID", "value": f"de{id}"},
            {"name": "smartMeterID", "value": f"ea{id}"},
            {"name": "marktlokation", "value": f"p21033h{id}"},
            {"name": "HEMS", "value": str(dict(id = random.randint(0, 10000), adresse = dot.join(map(str, (random.randint(0, 255) for _ in range(4)))), typ = 'HEMS'))},
            {"name": "steuerbox", "value": str(dict(id = random.randint(0, 10000), adresse = dot.join(map(str, (random.randint(0, 255) for _ in range(4)))), typ = 'Steuerbox'))},
            {"name": "verbrauchpA", "value": f"{random.randint(2000, 9000)}"}]
            issuer = grid_DID
            indy = {
                "cred_def_id": f"{issuer}:3:CL:20:default",
                "issuer_did": issuer,
                "schema_id": f"{issuer}:2:gridCert:1.0",
                "schema_issuer_did": issuer,
                "schema_name": "gridCert",
                "schema_version": "1.0"
            }
        case "assetCert":
            attributes = [{"name": "anlagenTyp", "value": f"{random.choice(['PV', 'Wind', 'Biomasse', 'Speicher', 'Wärmepumpe', 'Elektroauto'])}"},
            {"name": "stellschritteP", "value": f"{random.randint(1, 20)*10}"},
            {"name": "Pmax", "value": f"{random.randint(1000, 20000)}"},
            {"name": "Pmin", "value": f"{random.randint(10, 1000)}"},
            {"name": "energieArt", "value": f"{random.choice(['Strom', 'Wärme', 'Gas'])}"},
            {"name": "steuerbarkeit", "value": f"{random.choice(['ja', 'nein'])}"},
            {"name": "speicherKapa", "value": f"{random.choice([0,random.randint(4000, 16000)])}"}]
            issuer = grid_DID
            indy = {
                "cred_def_id": f"{issuer}:3:CL:26:default",
                "issuer_did": issuer,
                "schema_id": f"{issuer}:2:assetCert:1.0",
                "schema_issuer_did": issuer,
                "schema_name": "assetCert",
                "schema_version": "1.0"
            }
        case "warrantCert":
            attributes = [{"name": "handelsRichtung", "value": f"{random.choice(['Einkauf', 'Verkauf', 'Beides'])}"},
            {"name": "maxEinspeisung", "value": f"{random.randint(1000, 10000)}"},
            {"name": "maxLast", "value": f"{random.randint(1000, 10000)}"},
            {"name": "handelsArt", "value": f"{random.choice(['Flex', 'Energie', 'Beides'])}"}]
            issuer = platform_DID
            indy = {
                "cred_def_id": f"{issuer}:3:CL:32:default",
                "issuer_did": issuer,
                "schema_id": f"{issuer}:2:warrantCert:1.0",
                "schema_issuer_did": issuer,
                "schema_name": "warrantCert",
                "schema_version": "1.0"
            }
        case _:
            print("Invalid type")
            return
    name = type
    # Important for fetching the right connection_id
    if issuer == platform_DID:
        which = platform_DID
        conn_input = "platform"
    elif issuer == grid_DID:
        which = grid_DID
        conn_input = "grid"
    # Inserts the generated data into the credential proposal
    connections = requests.get(f'http://{BASE_URL}:{holder_port}/connections?state=active').json()
    connection_id = get_latest_platform_connection_id(connections, conn_input)
    credential_proposal_data = {
        "auto_remove": False,
        "comment": "Please give me permission to trade",
        "connection_id": connection_id,
        "credential_preview": {
            "@type": "issue-credential/2.0/credential-preview",
            "attributes": attributes
        },
        "filter": {
            "indy": indy,
            "ld_proof": {
                "credential": {
                    "@context": [
                        "https://www.w3.org/2018/credentials/v1",
                        "https://www.w3.org/2018/credentials/examples/v1"
                    ],
                    "credentialSubject": {"type": ["Person", "Prosumer"]},
                    "issuanceDate": f"{datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')}",
                    "issuer": f"did:sov:{issuer}",
                    "name": name,
                    "type": ["VerifiableCredential", name],
                },
                "options": {"proofType": "Ed25519Signature2018"}
            }
        },
        "trace": True
    }
    return credential_proposal_data


def get_latest_platform_connection_id(data, type: str = "platform"):
    latest_entry = None
    latest_timestamp = None

    for entry in data['results']:
        if type in entry['their_label']:
            updated_at = datetime.datetime.fromisoformat(entry['updated_at'].replace("Z", "+00:00"))
            if latest_timestamp is None or updated_at > latest_timestamp:
                latest_timestamp = updated_at
                latest_entry = entry

    if latest_entry:
        return latest_entry['connection_id']
    return None