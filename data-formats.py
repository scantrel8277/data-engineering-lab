import piplite
await piplite.install(['seaborn', 'lxml', 'openpyxl'])

import pandas as pd

from pyodide.http import pyfetch

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

await download(filename, "addresses.csv")

df = pd.read_csv("addresses.csv", header=None)

df

df.columns =['First Name', 'Last Name', 'Location ', 'City','State','Area Code']

df

df = df[['First Name', 'Last Name', 'Location ', 'City','State','Area Code']]
df

# To select the first row
df.loc[0]

# To select the 0th,1st and 2nd row of "First Name" column only
df.loc[[0,1,2], "First Name" ]

# To select the 0th,1st and 2nd row of "First Name" column only
df.iloc[[0,1,2], 0]


