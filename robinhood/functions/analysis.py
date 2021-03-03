import account
import pandas as pd
import onedrivesdk

'''

~/robinhood/functions/analysis.py
@description:
    Contains data transformations and analytics functions for presenting data and making decisions

'''

# Model the build_holdings object
def create_holdings_table():
    holdings = account.build_holdings() # get the holdings
    data = [] # list to hold stock data
    
    # Loop through stocks
    for name, stats in holdings.items():
        stock = {"name": name} # initialize name/value
        stock = {**stock, **stats} # merge stats dict with stocks
        data.append(stock) # append to data list

    # store data as a pandas DataFrame
    df = pd.DataFrame(data)

    # write df to csv file: /outputs/holdings.csv
    df.to_csv("./outputs/holdings.csv")

    return df
#
