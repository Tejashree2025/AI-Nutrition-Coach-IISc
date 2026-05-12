
# =========================
# FILE: backend/pdf_report.py
# =========================

from fpdf import FPDF
import os
import re

# =========================
# CLEAN TEXT
# =========================

def clean_text(text):

    # remove emojis / unicode
    text = text.encode(
        "latin-1",
        "ignore"
    ).decode(
        "latin-1"
    )

    # remove extra spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text

# =========================
# EXPORT PDF
# =========================

def export_diet_pdf(

    content,

    filename="generated_diet_plan.pdf"
):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_auto_page_break(
        auto=True,
        margin=15
    )

    pdf.set_font(
        "Arial",
        size=12
    )

    # =========================
    # CLEAN CONTENT
    # =========================

    content = clean_text(
        content
    )

    # =========================
    # WRITE LINES
    # =========================

    for line in content.split("\n"):

        pdf.multi_cell(

            0,

            10,

            line
        )

    # =========================
    # SAVE
    # =========================

    output_path = os.path.join(

        os.getcwd(),

        filename
    )

    pdf.output(
        output_path
    )

    return output_path

