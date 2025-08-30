# main.py
# Launches the Ultra Privacy Shield dashboard

from modules.dashboard_ui import PrivacyDashboard

if __name__ == "__main__":
    app = PrivacyDashboard()
    app.mainloop()
