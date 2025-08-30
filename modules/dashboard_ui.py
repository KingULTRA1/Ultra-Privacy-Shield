# dashboard_ui.py
# Interactive Python dashboard with logs, privacy score, and gamified interface

import tkinter as tk
from tkinter import ttk
from modules.tracker_scan import scan_trackers
from modules.system_cleaner import clear_temp, clear_browser_cache
from modules.report_generator import generate_pdf

class PrivacyDashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ultra Privacy Shield")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Privacy Score: 100", font=("Arial", 16)).pack(pady=10)
        ttk.Button(self, text="Run Privacy Scan", command=self.run_scan).pack(pady=5)
        ttk.Button(self, text="Clean System", command=self.clean_system).pack(pady=5)
        self.log_box = tk.Text(self, height=20)
        self.log_box.pack(pady=10, fill=tk.BOTH, expand=True)

    def log(self, message):
        self.log_box.insert(tk.END, message + "\n")
        self.log_box.see(tk.END)

    def run_scan(self):
        targets = ["https://example.com"]
        for t in targets:
            trackers = scan_trackers(t)
            self.log(f"{t} - Trackers found: {len(trackers)}")
        generate_pdf({"Scan Results": trackers})
        self.log("PDF report generated.")

    def clean_system(self):
        clear_temp()
        clear_browser_cache()
        self.log("System cleaned successfully.")

if __name__ == "__main__":
    app = PrivacyDashboard()
    app.mainloop()
