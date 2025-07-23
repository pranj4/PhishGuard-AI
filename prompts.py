EMAIL_ANALYZER_PROMPT = """You are an email analyzer for phishing. Classify the following email into one of three categories:
- SAFE
- SUSPICIOUS
- PHISHING
-Any other category you deem appropriate

Also explain WHY you classified it that way in 2-3 sentences.

Email content:
Subject: {subject}
From: {sender}
Body: {body}
"""