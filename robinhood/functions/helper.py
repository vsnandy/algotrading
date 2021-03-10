import json
import pandas as pd
import os

'''
~/robinhood/functions/helper.py
@description:
    Contains helper functions.
'''

# Write to Excel
def create_excel(data, name):
    print('Writing to Excel...')

    df = pd.DataFrame(data)
    
    # Create a Pandas Excel writer using XlsxWriter as the engine
    writer = pd.ExcelWriter('./outputs/{0}.xlsx'.format(name), engine='xlsxwriter')

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
#
