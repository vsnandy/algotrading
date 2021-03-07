import account
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
    holdings = r.build_holdings() # get the holdings
    data = [] # list to hold stock data
    
    # Loop through stocks
    for name, stats in holdings.items():
        stock = {"name": name} # initialize name/value
        stock = {**stock, **stats} # merge stats dict with stocks
        data.append(stock) # append to data list

    # store data as a pandas DataFrame
    df = pd.DataFrame(data)

    # write df to csv file: /outputs/holdings.xlsx
    df.to_excel("./outputs/holdings.xlsx")

    return df
#

# Upload all files in /outputs
def upload_outputs():
    # Upload files
    onedrive.upload(item_path='raspberrypi/test/holdings.xlsx', upload_type='rename', file_path='./outputs/holdings.xlsx')

    # Remove local files
    os.remove('./outputs/holdings.xlsx')
    print("Done")

# Main method
if __name__ == "__main__":
    # Login
    account.login()

    # Create outputs
    holdings = create_holdings_table()

    # Upload outputs
    upload_outputs()

    # Logout
    account.logout()
