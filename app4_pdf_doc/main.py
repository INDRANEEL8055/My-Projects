from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm",format="A4")  # p is portrait.

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)  # to set text color to RGB(makes it grey)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
    pdf.line(10, 21, 200, 21)  # for the underline below headers

    for i in range(row["Pages"]-1):
        pdf.add_page()


pdf.output("output.pdf")

# pdf.set_font(family="Times", style="B", size=12)
# pdf.cell(w=0,  # length of cell , x-axis
#          h=12,  # width of cell , y-axis
#          txt="Hello There!",  # it's the text to be added inside the cell
#         align="L",  # align text L= left C= center
#         ln=1,  # it's break-line if its 1 ,nxt cell will go to next line, if 0 next cell wl b added after width(w) ends
#         border=1)  # if border = 0 then there will be no cell borders visible
