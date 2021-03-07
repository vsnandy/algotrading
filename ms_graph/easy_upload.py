from ms_graph.client import MicrosoftGraphClient
import dotenv
import pathlib
import os
import json

# Graph API scopes
scopes = [
    'Files.ReadWrite.All',
    'User.ReadWrite.All',
    'Directory.ReadWrite.All'
]

# Load the environment variables file.
env_path = pathlib.Path('../../.env')
dotenv.load_dotenv(dotenv_path=env_path)

# Get the specified credentials.
client_id = os.environ['azure_client_id']
client_secret = os.environ['azure_client_secret']
redirect_uri = os.environ['azure_redirect_uri']

# Upload function
def upload(item_path, upload_type, file_path):
    # Initialize the Graph Client.
    graph_client = MicrosoftGraphClient(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scopes,
        credentials='config/ms_graph_state.jsonc'
    )

    # Login
    graph_client.login()

    # Grab the Drive Item services
    drive_item_services = graph_client.drive_item()

    # Create an upload session
    upload_session = drive_item_services.create_upload_session(item_path=item_path, item=upload_type)

    drive_item_services.upload_large_file(upload_session['uploadUrl'], file_path)
