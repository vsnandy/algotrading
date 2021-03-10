import account
import helper
import pandas as pd
import robin_stocks.robinhood as r
from pprint import pprint
from ms_graph.client import MicrosoftGraphClient
import ms_graph.easy_upload as onedrive
import dotenv
import pathlib
import os
import json

'''

~/robinhood/functions/analysis.py
@description:
    Contains data transformations and analytics functions for presenting data and making decisions

'''

# Model the build_holdings object
def create_holdings_table():
    print("Getting holdings data...")

    holdings = r.build_holdings() # get the holdings
    data = [] # list to hold stock data
    
    print("Transforming data...")

    # Loop through stocks
    for name, stats in holdings.items():
        stock = {"name": name} # initialize name/value
        stock = {**stock, **stats} # merge stats dict with stocks
        data.append(stock) # append to data list

    # Write to Excel
    helper.create_excel(data, 'holdings')
#

# Get all option orders
def create_option_orders_table():
    print("Getting options data...")

    options = r.get_all_option_orders()

    print("Transforming data...")
    data = options

    # Write to Excel
    helper.create_excel(data, 'option_orders')
#

# Upload all files in /outputs
def upload_outputs():
    print("Uploading files to OneDrive...")

    for root, dirs, files in os.walk('./outputs'):
        for name in files:
            # Upload files
            onedrive.upload(item_path='raspberrypi/robinhood/account/{0}'.format(name), upload_type='rename', file_path='./outputs/{0}'.format(name))
            # Remove local files
            os.remove('./outputs/{0}'.format(name))

    print("Files uploaded and local copies removed!")
#

# Main method
if __name__ == "__main__":
    # Login
    print("Logging into Robinhood...")
    account.login()
    print("Logged in")

    # Create Excel files
    create_holdings_table() # current holdings
    create_option_orders_table() # all option orders

    # Upload outputs
    upload_outputs()

    # Logout
    account.logout()
