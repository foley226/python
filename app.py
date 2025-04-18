import ssl
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context

sheet_id = '1wz9Hcp_vssiFbRHv7lDrW3RzFWefTdtXTXeA-pICSv8'

sheet_name = 'CFB'

url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'


df = pd.read_csv(url)
print(df.head())
