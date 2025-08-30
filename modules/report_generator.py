# report_generator.py
# Generates detailed PDF and HTML privacy reports summarizing scans and system hygiene

from fpdf import FPDF
import os
from datetime import datetime

def generate_pdf(report_data, filename=None):
    """Generates a PDF report from report_data dictionary."""
    if filename is None:
        filename = f"reports/privacy_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, "Ultra Privacy Shield Report", ln=True, align="C")
    pdf.ln(5)
    
    try:
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
        print(f"[INFO] PDF report saved to {filename}")
    except Exception as e:
        print(f"[ERROR] Failed to generate PDF report: {e}")

def generate_html(report_data, filename=None):
    """Generates an HTML report from report_data dictionary."""
    if filename is None:
        filename = f"reports/privacy_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    try:
        html_content = "<html><head><title>Privacy Report</title></head><body>"
        html_content += "<h1>Ultra Privacy Shield Report</h1>"
        
        for section, content in report_data.items():
            html_content += f"<h2>{section}</h2><ul>"
            if isinstance(content, list):
                for item in content:
                    html_content += f"<li>{item}</li>"
            else:
                html_content += f"<li>{content}</li>"
            html_content += "</ul>"
        
        html_content += "</body></html>"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        
        print(f"[INFO] HTML report saved to {filename}")
    except Exception as e:
        print(f"[ERROR] Failed to generate HTML report: {e}")
