import re

# Basic list of suspicious keywords
SUSPICIOUS_KEYWORDS = [
    "urgent", "verify your account", "reset password",
    "click here", "limited time", "account locked"
]

def contains_suspicious_keywords(text: str) -> bool:
    """Check if email body has common phishing phrases."""
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in SUSPICIOUS_KEYWORDS)


def extract_urls(text: str):
    """Find all URLs in the text using regex."""
    url_pattern = r'(https?://[^\s]+)'
    return re.findall(url_pattern, text)


def is_suspicious_domain(url: str) -> bool:
    """
    Check if URL contains patterns like numbers instead of letters,
    unusual subdomains, or misspellings.
    """
    suspicious_patterns = [r"b[a-z0-9]{1,2}nk", r"paypa1", r"login", r"verify"]
    for pattern in suspicious_patterns:
        if re.search(pattern, url.lower()):
            return True
    return False
