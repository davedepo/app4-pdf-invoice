import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob(r"TXTs/*.txt")
print(filepaths)

# to create one file with multiple pages we move pdf object outside loop
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
	pdf.add_page()
	filename = Path(filepath).stem
	print(filename)
	pdf.set_font(family="Times", style="B", size=16)
	pdf.cell(w=50, h=8, txt=f"{filename.capitalize()}")

pdf.output(f"PDFs/txt_to_pdf.pdf")
