import ssl
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context

sheet_id = '1wz9Hcp_vssiFbRHv7lDrW3RzFWefTdtXTXeA-pICSv8'

sheet_name = 'CFB'

url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'


df = pd.read_csv(url)

# Step 4: Clean column names to remove extra spaces, lowercase and replace spaces with underscores
df.columns = df.columns.str.strip().str.lower().str.replace('_', ' ')

# Step 5: Add the "Five_Start_recruits" column
df['Five_Start_recruits'] = 0  # You can change the value (0) to whatever you'd like, or leave it as is

# Step 6: Preview the updated DataFrame (including the new 'Five_Start_recruits' column)
print(df.head())