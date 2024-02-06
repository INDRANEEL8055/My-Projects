from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")  # p is portrait.
pdf.set_auto_page_break(auto=False, margin=0)  # pages should not be broken automatically

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # sets the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)  # to set text color to RGB(makes it grey)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)

    for y in range(20,298,10):
        pdf.line(10, y, 200, y)  # for the underline below headers

    # to set footer
    pdf.ln(268)  # size of break-line is 278mm
    pdf.set_font(family="Times", style="I", size=10)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align='R')

    for i in range(row["Pages"]-1):
        pdf.add_page()
        # to set footer
        pdf.ln(278)  # size of break-line is 278mm
        pdf.set_font(family="Times", style="I", size=10)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align='R')

        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)  # for the underline below headers

pdf.output("output.pdf")

# pdf.set_font(family="Times", style="B", size=12)
# pdf.cell(w=0,  # length of cell , x-axis
#          h=12,  # width of cell , y-axis
#          txt="Hello There!",  # it's the text to be added inside the cell
#          align="L",  # align text L= left C= center
#          ln=1,  # it's break-line if its 1 ,nxt cell will go to next line, if 0 next cell wl b added after width(w) ends
#          border=1)  # if border = 0 then there will be no cell borders visible
