import pandas as pd
import pyarrow # always import this when you are using pandas to import multiple files
import openpyxl  # required by pandas to open Excel files
import glob

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)
