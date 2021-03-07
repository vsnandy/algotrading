import os
import dotenv
from pathlib import Path

import pyotp
import robin_stocks.robinhood as r

'''

~/robinhood/functions/account.py
@description:
    Contains all functions related to Robinhood account data.

'''


# Login to Robinhood account using environment variables
def login():
    # load the environment variable file
    env_path = Path("../../.env")
    dotenv.load_dotenv(dotenv_path=env_path)

    # Get OTP & use it to login
    totp = pyotp.TOTP(os.environ['robin_mfa']).now()
    login = r.login(os.environ['robin_username'], os.environ['robin_password'], store_session=False, mfa_code=totp)
#

# Logout of Robinhood
def logout():
    r.logout()
#
