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

	# create pdf object & add a blank page
	pdf = FPDF(orientation="P", unit="mm", format="A4")
	pdf.add_page()

	# extract filename from pathlib
	filename = Path(filepath).stem
	invoice_nr, date = filename.split("-")

	# create invoice header
	pdf.set_font(family="Times", size=16, style="B")
	pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}", ln=1)

	# create invoice date with header
	pdf.set_font(family="Times", size=16, style="B")
	pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)
	pdf.cell(w=30, h=8, txt="", border=0, ln=1)
	pdf.cell(w=30, h=8, txt="", border=0, ln=1)

	# extract excel data to dataframe object
	df = pd.read_excel(filepath, sheet_name="Sheet 1")

	# create column list from df & convert to title case
	columns_to_list = df.columns
	columns_to_list = [item.replace("_", " ").title()
	                   for item in columns_to_list]

	# create column headers from column list
	pdf.set_font(family="Times", size=10, style="B")
	pdf.set_text_color(80, 80, 80)
	pdf.cell(w=30, h=8, txt=columns_to_list[0], border=1)
	pdf.cell(w=70, h=8, txt=columns_to_list[1], border=1)
	pdf.cell(w=35, h=8, txt=columns_to_list[2], border=1)
	pdf.cell(w=30, h=8, txt=columns_to_list[3], border=1)
	pdf.cell(w=30, h=8, txt=columns_to_list[4], border=1, ln=1)

	# iter rows from df
	for index, row in df.iterrows():
		pdf.set_font(family="Times", size=10)
		pdf.set_text_color(80, 80, 80)
		pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
		pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1)
		pdf.cell(w=35, h=8, txt=str(row["amount_purchased"]), border=1)
		pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
		pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

	# create row for sum of total price
	total_sum = df["total_price"].sum()
	pdf.set_font(family="Times", size=10)
	pdf.set_text_color(80, 80, 80)
	pdf.cell(w=30, h=8, txt="", border=1)
	pdf.cell(w=70, h=8, txt="", border=1)
	pdf.cell(w=35, h=8, txt="", border=1)
	pdf.cell(w=30, h=8, txt="", border=1)
	pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)
	pdf.cell(w=30, h=8, txt="", border=0, ln=1)
	pdf.cell(w=30, h=8, txt="", border=0, ln=1)

	# create total price statement for each invoice pdf
	pdf.set_font(family="Times", size=12, style="IB")
	pdf.cell(w=31, h=9, txt=f"The Total Price is {total_sum}", ln=1)

	# add company name & image for each invoice pdf
	pdf.set_font(family="Times", size=12, style="IB")
	pdf.cell(w=31, h=9, txt=f"Company Name")
	pdf.image("app4-image.png", w=8)

	pdf.output(f"PDFs/{filename}.pdf")
