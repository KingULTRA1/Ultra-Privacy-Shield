# unsafe_domains.py
# Checks URLs against known malicious and phishing domains

THREAT_LIST = ["malwaredomain.com", "phishingsite.net", "suspiciousdomain.org"]

def check_domain(domain):
    """Return True if the domain is known to be unsafe."""
    return domain.lower() in THREAT_LIST
