import requests
import json
from config import BASE_URL as url

def connect_agents(receive_port: int, target: str):
    if receive_port < 11002 or receive_port >= 12000:
        print("Error: Port number out of range")
        return 0
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    if target == "platform":
        invite_port = 11000
        label = "Platform"
    elif target == "grid":
        invite_port = 11001
        label = "Grid"
    else:
        print("Invalid target")
        return 0
    data = {
        "accept": [
            "didcomm/aip1",
            "didcomm/aip2;env=rfc19"
        ],
        "alias": label,
        "handshake_protocols": [
            "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/didexchange/1.0"
        ],
        "metadata": {},
        "my_label": f"{target} {receive_port}",
        "protocol_version": "1.1",
        "use_public_did": False
    }

    # Creates and sends invitation from Alice to Bob
    response = requests.post(f"http://{url}:{invite_port}/out-of-band/create-invitation?auto_accept=true&multi_use=false",
                             headers=headers, json=data)

    if response.status_code == 200:
        # Parse the JSON response
        response_json = json.loads(response.text)

        # Extract the "invitation" attribute
        invitation = response_json.get("invitation")

        if invitation is not None:
            print("Invitation:")
            print(invitation)
        else:
            print("No 'invitation' attribute found in the JSON response.")
    else:
        print(f"HTTP POST request failed with response code: {response.status_code}")

    if invitation is not None:
        # Accepts the Invitation, Connection is established if successful
        response2 = requests.post(
            f"http://{url}:{receive_port}/out-of-band/receive-invitation?auto_accept=true&use_existing_connection=false",
            headers=headers, json=invitation)

        if response2.status_code == 200:
            print(response2.text)
            return 1
        else:
            print(f"HTTP POST request failed with response code: {response2.status_code}")
            return 0
    else:
        print("No invitation available to accept.")
        return 0
