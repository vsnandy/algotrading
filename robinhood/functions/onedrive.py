import os
import dotenv
from pathlib import Path

import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer

'''

~/robinhood/functions/onedrive.py
@description:
    Functions for OneDrive API

'''

# Sign in and authenticate to OneDrive
def sign_in():
    # Load the environment variable file
    env_path = Path("../../.env")
    dotenv.load_dotenv(dotenv_path=env_path)
    client_id = os.environ['azure_client_id']
    client_secret = os.environ['azure_client_secret']
    redirect_uri = os.environ['azure_redirect_uri']

    # Azure Auth flow
    client = onedrivesdk.get_default_client(client_id=client_id, scopes=['wl.signin', 'wl.offline_access', 'onedrive.readwrite'])
    print("client:", client)
    auth_url = client.auth_provider.get_auth_url(redirect_uri)
    print('auth_url:', auth_url)

    # Block thread until we have the code
    code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)
    print('code:', code)
    # Finally, authenticate!
    client.auth_provider.authenticate(code, redirect_uri, client_secret)
    print('client:', client)

    return client
#

# Display all items in the user's OneDrive
def list_items(client):
    item_id = "root"
    items = client.item(id=item_id).children.get()
    return items
#
