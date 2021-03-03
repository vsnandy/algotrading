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

# Get account information
def get_data(info=None):
    # Login
    #login()

    # Get data
    data = r.account.load_phoenix_account(info)

    # Logout
    #logout()

    return data
#

# Get historical account data
# ERRORING
def get_historical_data(interval="week"):
    # Login
    #login()

    # Get data
    data = r.account.get_historical_portfolio(interval)

    # Logout
    #logout()

    return data
#

# Get all positions ever traded
def get_all_positions(info=None):
    # Login
    #login()

    # Get data
    data = r.account.get_all_positions(info)

    # Logout
    #logout()

    return data
#

# Get open stock positions
def get_open_stock_positions(info=None):
    #Login
    #login()

    # Get data
    data = r.account.get_open_stock_positions(info)

    # Logout
    #logout()

    return data
#

# Get holdings data
def build_holdings(with_dividends=False):
    #Login
    #login()

    # Get data
    data = r.account.build_holdings(with_dividends)

    # Logout
    #logout()

    return data
#

