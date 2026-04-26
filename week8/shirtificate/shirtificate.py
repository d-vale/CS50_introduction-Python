from fpdf import FPDF


def main():
    name = input("Name: ")

    pdf = FPDF(orientation="portrait", format="A4")
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 36)
    pdf.cell(0, 50, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

    img_w = 190
    img_x = (210 - img_w) / 2
    y_before = pdf.get_y()
    pdf.image("shirtificate.png", x=img_x, y=y_before, w=img_w)

    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(0, y_before + 140)
    pdf.cell(210, 0, f"{name} took CS50P!", align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
