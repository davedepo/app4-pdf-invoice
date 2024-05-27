import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# to create python list that contains all filepaths
filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)

# to read each file we initiate for-loop
# we will get dependency warning - Missing optional dependency 'openpyxl'
# install openpyxl from python packages or terminal
for filepath in filepaths:
	df = pd.read_excel(filepath, sheet_name="Sheet 1")
	pdf = FPDF(orientation="P", unit="mm", format="A4")
	pdf.add_page()
	filename = Path(filepath).stem
	invoice_nr = filename.split("-")[0]
	pdf.set_font(family="Times", size=16, style="B")
	pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}")
	pdf.output(f"PDFs/{filename}.pdf")