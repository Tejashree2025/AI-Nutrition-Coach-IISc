from fpdf import FPDF

# =========================
# PDF REPORT
# =========================

def generate_pdf_report(
    username,
    summary
):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font(
        "Arial",
        size=14
    )

    pdf.cell(
        200,
        10,
        txt="AI Nutrition Report",
        ln=True
    )

    pdf.set_font(
        "Arial",
        size=11
    )

    for key, value in summary.items():

        pdf.multi_cell(
            0,
            10,
            txt=f"{key}: {value}"
        )

    path = f"reports/{username}_report.pdf"

    pdf.output(path)

    return path