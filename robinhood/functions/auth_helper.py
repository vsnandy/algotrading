import msal
import os
from pathlib import Path
import dotenv
import json
import time

# Load the environment variable file
env_path = Path("../../.env")
dotenv.load_dotenv(dotenv_path=env_path)

# App details
app_id = os.environ['azure_client_id']
app_secret = os.environ['azure_client_secret']
redirect = "http://localhost:8080/graph_login"
scopes = ['user.read', 'mailboxsettings.read', 'calendars.readwrite']
authority = "https://login.microsoftonline.com/common"

#
def load_cache(request):
    # Check for token cache in the session
    cache = msal.SerializableTokenCache()
    if request.session.get("token_cache"):
        cache.deserialize(request.session['token_cache'])

    return cache
#

#
def save_cache(request, cache):
    # If cache has changed, persist back to session
    if cache.has_state_changed:
        request.session['token_cache'] = cache.serialize()
#

#
def get_msal_app(cache=None):
    # Initialize the MSAL confidential client
    auth_app = msal.ConfidentialClientApplication(
            app_id,
            authority=authority,
            client_credential=app_secret,
            token_cache=cache)

    return auth_app
#

# Method to generate a sign-in flow
def get_sign_in_flow():
    auth_app = get_msal_app()

    return auth_app.initiate_auth_code_flow(
            scopes,
            redirect_uri=redirect)
#

# Method to exchange auth code for access token
def get_token_from_code(request):
    cache = load_cache(request)
    auth_app = get_msal_app(cache)

    # Get the flow saved in session
    flow = request.session.pop('auth_flow', {})

    result = auth_app.acquire_token_by_auth_code_flow(flow, request.GET)
    save_cache(request, cache)

    return result
#
