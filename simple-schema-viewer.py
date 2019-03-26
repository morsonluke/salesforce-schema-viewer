from simple_salesforce import Salesforce
from pprint import pprint as pp
import json
import pandas as pd

sf = Salesforce(username='', 
                password='', 
                security_token='', 
                version='44.0', 
                instance='https://{domain}.salesforce.com'
                )

# Replace Account with the relevant object such as Contact, Lead etc.
data = sf.Account.describe()["fields"]

# Create a pandas DataFrame from a list of dictionaries
df = pd.DataFrame.from_dict(data)
# Outputs the list of fields to a csv called describe.csv
df.to_csv('describe.csv')