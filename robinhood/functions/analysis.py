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
    print("Getting holdings data...")

    holdings = r.build_holdings() # get the holdings
    data = [] # list to hold stock data
    
    print("Transforming data...")

    # Loop through stocks
    for name, stats in holdings.items():
        stock = {"name": name} # initialize name/value
        stock = {**stock, **stats} # merge stats dict with stocks
        data.append(stock) # append to data list

    # store data as a pandas DataFrame
    df = pd.DataFrame(data)

    print("Writing data to Excel...")

    # Create a Pandas Excel writer using XlsxWriter as the engine
    writer = pd.ExcelWriter('./outputs/holdings.xlsx', engine='xlsxwriter')

    # Write the dataframe data to Xlsxwriter. Turn off the default header and 
    # index and skip one row to allow us to insert a user defined header
    df.to_excel(writer, sheet_name='Sheet1', startrow=1, header=False, index=False)

    # Get the xlsxwriter workbook and worksheet objects.
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    # Get the dimension of the dataframe
    (max_row, max_col) = df.shape

    # Create a list of column headers, to use in add_table()
    column_settings = [{'header': column} for column in df.columns]

    # Add the Excel table structure. Pandas will add the data
    worksheet.add_table(0, 0, max_row, max_col - 1, {'columns': column_settings})

    # Make the columns wider for clarity.
    worksheet.set_column(0, max_col - 1, 12)

    # Close the Pandas Excel writer and output the Excel file
    writer.save()

    print("File created!")

    return df
#

# Upload all files in /outputs
def upload_outputs():
    print("Uploading files to OneDrive...")

    # Upload files
    onedrive.upload(item_path='raspberrypi/test/holdings.xlsx', upload_type='rename', file_path='./outputs/holdings.xlsx')

    print("Files uploaded!")

    # Remove local files
    os.remove('./outputs/holdings.xlsx')

    print("Removed local file copies!")

# Main method
if __name__ == "__main__":
    # Login
    print("Logging into Robinhood...")
    account.login()
    print("Logged in")

    # Create outputs
    holdings = create_holdings_table()

    # Upload outputs
    upload_outputs()

    # Logout
    account.logout()
