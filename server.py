import streamlit as st
from twilio.rest import Client
import os
from dotenv import load_dotenv

# ── Load Credentials ────────────────────────────────
try:
    ACCOUNT_SID = st.secrets["TWILIO_ACCOUNT_SID"]
    AUTH_TOKEN  = st.secrets["TWILIO_AUTH_TOKEN"]
    FROM_NUMBER = st.secrets["TWILIO_FROM_NUMBER"]
except Exception:
    load_dotenv()
    ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    AUTH_TOKEN  = os.getenv("TWILIO_AUTH_TOKEN")
    FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER")

st.title("📱 Bulk SMS Sender")

# ── DEBUG SECTION - shows what is loaded ────────────
st.warning("🔍 DEBUG INFO:")
st.write("SID:", ACCOUNT_SID)
st.write("Token:", AUTH_TOKEN)
st.write("From:", FROM_NUMBER)