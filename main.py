import pandas as pd
import glob

# to create python list that contains all filepaths
filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)

# to read each file we initiate for-loop
# we will get dependency warning - Missing optional dependency 'openpyxl'
# install openpyxl from python packages or terminal
# out of code will create df - stores tabular data of all xlsx files
for filepath in filepaths:
	df = pd.read_excel(filepath, sheet_name="Sheet 1")
	print(df)
