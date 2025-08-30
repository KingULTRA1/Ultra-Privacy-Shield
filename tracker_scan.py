# tracker_scan.py
# Scans websites for trackers, analytics, and third-party scripts

import requests
from bs4 import BeautifulSoup

def scan_trackers(url):
    """Return a list of third-party trackers found on a website."""
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        scripts = soup.find_all("script")
        trackers = [s.get("src") for s in scripts if s.get("src") and "analytics" in s.get("src")]
        return trackers
    except Exception as e:
        return {"error": str(e)}
