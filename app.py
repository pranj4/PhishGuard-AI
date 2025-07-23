import streamlit as st
import requests

# --- Streamlit Page Config ---
st.set_page_config(page_title="PhishGuard AI", layout="wide")
st.markdown("""
<style>
    .header { color: #ff4b4b; }
    .safe { color: #0f9d58; }
    .warning { color: #f4b400; }
    .danger { color: #db4437; }
    .report-box { 
        border: 1px solid #ddd; 
        border-radius: 10px; 
        padding: 15px; 
        margin-top: 15px;
        background-color: #f9f9f9;
    }
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.title("🛡️ PhishGuard AI")
st.markdown("### AI-Powered Phishing Detection System")

# --- Input Mode Selector ---
mode = st.radio("Choose Input Method:", ["Structured Input", "Paste Full Email"])

# --- Mode 1: Structured Input ---
if mode == "Structured Input":
    st.subheader("Email Details")

    col1, col2 = st.columns(2)
    with col1:
        subject = st.text_input("Subject", placeholder="e.g., Urgent: Verify your account now!")
    with col2:
        sender = st.text_input("Sender", placeholder="e.g., security@b4nk-alert.com")

    body = st.text_area("Email Body", height=200, placeholder="Paste email content here...")

    # Analyze Button
    if st.button("Analyze Email"):
        if not (subject.strip() and sender.strip() and body.strip()):
            st.warning("Please enter complete email details.")
        else:
            with st.spinner("Detecting phishing indicators..."):
                try:
                    # Send to Agent A endpoint
                    response = requests.post(
                        "http://localhost:8000/analyze",
                        json={"subject": subject, "sender": sender, "body": body}
                    )
                    result = response.json()

                    # Display styled results
                    st.markdown('<div class="report-box">', unsafe_allow_html=True)
                    st.markdown("#### **Agent A (Analyzer) Result:**")
                    st.info(result["analysis"])

                    st.markdown("#### **Agent B (Verifier) Result:**")
                    verification_text = result["verification"].lower()

                    if "phishing" in verification_text:
                        st.markdown('<p class="danger">🚨 PHISHING CONFIRMED</p>', unsafe_allow_html=True)
                        st.write(result["verification"])
                    elif "suspicious" in verification_text:
                        st.markdown('<p class="warning">⚠️ SUSPICIOUS</p>', unsafe_allow_html=True)
                        st.write(result["verification"])
                    else:
                        st.markdown('<p class="safe">✅ SAFE</p>', unsafe_allow_html=True)
                        st.write(result["verification"])

                    st.markdown('</div>', unsafe_allow_html=True)

                except Exception as e:
                    st.error(f"Analysis failed: {str(e)}")

# --- Mode 2: Paste Full Email ---
else:
    st.subheader("Paste Full Raw Email")
    full_email = st.text_area("Raw Email Content", height=300, placeholder="Paste the full email text (headers + body)...")

    # Analyze Button
    if st.button("Analyze Raw Email"):
        if not full_email.strip():
            st.warning("Please paste the full email content.")
        else:
            with st.spinner("Analyzing full email..."):
                try:
                    # For now, send entire text as 'body' (no subject/sender separation)
                    response = requests.post(
                        "http://localhost:8000/analyze",
                        json={"subject": "Raw Email", "sender": "unknown", "body": full_email}
                    )
                    result = response.json()

                    # Display styled results
                    st.markdown('<div class="report-box">', unsafe_allow_html=True)
                    st.markdown("#### **Agent A (Analyzer) Result:**")
                    st.info(result["analysis"])

                    st.markdown("#### **Agent B (Verifier) Result:**")
                    verification_text = result["verification"].lower()

                    if "phishing" in verification_text:
                        st.markdown('<p class="danger">🚨 PHISHING CONFIRMED</p>', unsafe_allow_html=True)
                        st.write(result["verification"])
                    elif "suspicious" in verification_text:
                        st.markdown('<p class="warning">⚠️ SUSPICIOUS</p>', unsafe_allow_html=True)
                        st.write(result["verification"])
                    else:
                        st.markdown('<p class="safe">✅ SAFE</p>', unsafe_allow_html=True)
                        st.write(result["verification"])

                    st.markdown('</div>', unsafe_allow_html=True)

                except Exception as e:
                    st.error(f"Analysis failed: {str(e)}")
