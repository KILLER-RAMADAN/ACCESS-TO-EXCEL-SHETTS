import pandas as pd
# Add some color to the window
# file location..
EXCEL_FILE = 'C:\\Users\\ahmed\\Desktop\\enter data to excel\\ramadan.xlsx'
df = pd.read_excel(EXCEL_FILE)
print(df)
print("#"*50)
print("some information about the file")
for key, name in enumerate(df):
    print(f"{key+1}=>{name}")
