import requests
from config import BASE_URL


# Function to get all connections
def get_connections(port):
    base_url = f"http://{BASE_URL}:{port}/connections"
    response = requests.get(base_url)
    if response.status_code == 200:
        return response.json()['results']
    else:
        print(f"Failed to retrieve connections: {response.status_code}")
        return []


# Function to delete a connection by connection_id
def delete_connection(connection_id, port):
    delete_url = f"http://{BASE_URL}:{port}/connections/{connection_id}"
    response = requests.delete(delete_url)
    if response.status_code == 200:
        print(f"Successfully deleted connection {connection_id}")
    else:
        print(f"Failed to delete connection {connection_id}: {response.status_code}")


# Main script -> Deletes all Connections of an agent
def delete_all_connections(port):
    # Get all connections
    connections = get_connections(port)

    # Loop through the results and delete each connection
    for connection in connections:
        connection_id = connection['connection_id']
        delete_connection(connection_id, port)


