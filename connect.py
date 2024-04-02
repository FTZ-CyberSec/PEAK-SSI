import requests
import json


def connect_agents(url, receive_port, invite_port):
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    data = {
        "accept": [
            "didcomm/aip1",
            "didcomm/aip2;env=rfc19"
        ],
        "handshake_protocols": [
            "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/didexchange/1.0"
        ],
        "metadata": {},
        "my_label": "Invitation to Bob",
        "protocol_version": "1.1",
        "use_public_did": False
    }

    # Creates and sends invitation from Alice to Bob
    response = requests.post(f"http://{url}:{invite_port}/out-of-band/create-invitation?auto_accept=true&multi_use=true",
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
            f"http://{url}:{receive_port}/out-of-band/receive-invitation?auto_accept=true&use_existing_connection=true",
            headers=headers, json=invitation)

        if response2.status_code == 200:
            print(response2.text)
        else:
            print(f"HTTP POST request failed with response code: {response2.status_code}")
    else:
        print("No invitation available to accept.")
