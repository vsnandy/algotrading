import os
import sys
import json
import logging
import dotenv
from pathlib import Path

import requests
import msal

'''

/robinhood/functions/auth.py
@description:
    Functions to authorize Microsoft API access. Source repo: https://github.com/AzureAD/microsoft-authentication-library-for-python

'''

# Create a preferably long-lived app instance which maintains a token cache.
def authenticate():
    # Load the environment variable file
    env_path = Path("../../.env")
    dotenv.load_dotenv(dotenv_path=env_path)
    client_id = os.environ['azure_client_id']
    client_secret = os.environ['azure_client_secret']
    user_id = os.environ['azure_user_id']
    client_authority = "https://login.microsoftonline.com/common"
    scope = ["https://graph.microsoft.com/.default"]

    app = msal.ConfidentialClientApplication(client_id, authority=client_authority, client_credential=client_secret)

    # The pattern to acquire a token looks like this
    result = None

    # Firstly, looks up a token from cache
    # Since we are looking for token for the current app, NOT for an end user,
    # notice we give account parameter as None
    result = app.acquire_token_silent(scope, account=None)

    if not result:
        logging.info("No suitable token exists in cache. Let's get a new one from AAD.")
        result = app.acquire_token_for_client(scopes=scope)

    if "access_token" in result:
        # Calling graph using access token
        graph_data = requests.get( # Use token to call downstream service
                "https://graph.microsoft.com/v1.0/users/",
                headers={'Authorization': 'Bearer ' + result['access_token']},).json()
        print("Graph API call result: %s" % json.dumps(graph_data, indent=2))

    else:
        print(result.get("error"))
        print(result.get("error_description"))
        print(result.get("correlation_id"))
