from pprint import pprint
from ms_graph.client import MicrosoftGraphClient
import dotenv
import pathlib
import os

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

# Grab the User Services.
user_services = graph_client.users()

# List the Users.
pprint(user_services.list_users())

# Grab the Drive Services.
drive_services = graph_client.drives()

# List the Root Drive.
pprint(drive_services.get_root_drive())

# List the Root Drive Deltas.
pprint(drive_services.get_root_drive_delta())
