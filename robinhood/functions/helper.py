import json

'''

~/robinhood/functions/helper.py
@description:
    Generic helper functions

'''

# Pretty print JSON
def pprint(data):
    print(json.dumps(data, indent=4))
#
