from pprint import pprint
from ms_graph.client import MicrosoftGraphClient
import dotenv
import pathlib
import os
import json

scopes = [
        'Calendars.ReadWrite',
        'Files.ReadWrite.All',
        'User.ReadWrite.All',
        'Notes.ReadWrite.All',
        'Directory.ReadWrite.All',
        'User.Read.All',
        'Directory.Read.All'
        #'offline_access',
        #'openid',
        #'profile'
    ]

# Load the environment variables file.
env_path = pathlib.Path('../../.env')
dotenv.load_dotenv(dotenv_path=env_path)

# Get the specified credentials.
client_id = os.environ['azure_client_id']
client_secret = os.environ['azure_client_secret']
redirect_uri = os.environ['azure_redirect_uri']

# Initialize the Client.
graph_client = MicrosoftGraphClient(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scopes,
        credentials='config/ms_graph_state.jsonc'
        )

# Login to the Client.
graph_client.login()

# Grab the Drive Services.
drive_services = graph_client.drives()

# Grab the Drive Item Services.
drive_item_services = graph_client.drive_item()

# Create an upload session
upload_session = drive_item_services.create_upload_session(item_path='Documents/test.txt', item='rename')

drive_item_services.upload_large_file(upload_session['uploadUrl'], './upload.txt')
