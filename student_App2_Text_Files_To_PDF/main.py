from fpdf import FPDF
import pandas as pd
import pyarrow
import glob
from pathlib import Path

# Create a list of text filepaths
filepaths = glob.glob("files/*.txt")

# Create one PDF file
pdf = FPDF(orientation="P", unit="mm", format="a4")

# To go through each textfile
for filepath in filepaths:
    # Add a page to the PDF document for each text file
    pdf.add_page()

    # Get the file name without extension
    # and convert it to the title case(e.g. Cat)
    filename = Path(filepath).stem
    name = filename.title()

    # Add the name to the PDF
    pdf.set_font(family="Times", size=16, style="B",)
    pdf.cell(w=50, h=8, txt=name, ln=1)

# Produce the PDF
pdf.output("output.pdf")
