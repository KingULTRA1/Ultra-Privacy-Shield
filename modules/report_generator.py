# report_generator.py
# Generates detailed PDF privacy reports summarizing scans and system hygiene

from fpdf import FPDF
import os

def generate_pdf(report_data, filename="reports/privacy_report.pdf"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, "Ultra Privacy Shield Report", ln=True, align="C")
    pdf.ln(5)
    for section, content in report_data.items():
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, section, ln=True)
        pdf.set_font("Arial", "", 11)
        if isinstance(content, list):
            for item in content:
                pdf.cell(0, 8, f"- {item}", ln=True)
        else:
            pdf.multi_cell(0, 8, str(content))
        pdf.ln(3)
    pdf.output(filename)
    print(f"[INFO] Report saved to {filename}")
