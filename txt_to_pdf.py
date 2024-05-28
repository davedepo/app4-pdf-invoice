import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob(r"TXTs/*.txt")
print(filepaths)

# to create one file with multiple pages we move pdf object outside loop
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
	# to add blank pg in PDF for each txt file
	pdf.add_page()

	# to extract filename from pathlib for each txt file
	filename = Path(filepath).stem
	# print(filename) test output

	# to create headers from each .txt filename
	pdf.set_font(family="Times", style="B", size=16)
	pdf.cell(w=50, h=8, txt=f"{filename.capitalize()}", ln=1)
	pdf.line(10, 20, 200, 20)
	pdf.cell(w=50, h=4, txt="", ln=1)

	# to open and read .txt files from filepath
	with open(filepath, "r") as file:
		content = file.read()

	# to set pg font, execute multi-cell output from each .txt
	pdf.set_font(family="Times", size=12)
	pdf.multi_cell(w=0, h=6, txt=content)

# creat 1 single PDF output from multiple txt file (Out-side loop)
pdf.output("PDFs/txt_to_pdf.pdf")
