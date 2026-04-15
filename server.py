import streamlit as st
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

# ── Twilio Credentials ──────────────────────────────
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN  = os.getenv("TWILIO_AUTH_TOKEN")
FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER")

# ── Page Config ─────────────────────────────────────
st.set_page_config(page_title="Bulk SMS Sender", page_icon="📱")
st.title("📱 Bulk Message Sender")

# ── Input Fields ─────────────────────────────────────
numbers_input = st.text_area(
    "Phone Numbers (one per line, with country code)",
    placeholder="+9779800000001\n+9779800000002\n+9779800000003",
    height=150
)

message_input = st.text_area(
    "Your Message",
    placeholder="Type your message here...",
    height=120
)

# ── Send Button ───────────────────────────────────────
if st.button("Send to All"):
    numbers = [n.strip() for n in numbers_input.split('\n') if n.strip()]

    if not numbers or not message_input.strip():
        st.error("❌ Please enter phone numbers and a message.")
    else:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        sent   = 0
        failed = 0

        with st.spinner(f"Sending to {len(numbers)} numbers..."):
            for number in numbers:
                try:
                    msg = client.messages.create(
                        body  = message_input,
                        from_ = FROM_NUMBER,
                        to    = number
                    )
                    sent += 1
                    st.success(f"✅ Sent to {number} | SID: {msg.sid}")

                except Exception as e:
                    failed += 1
                    st.error(f"❌ Failed {number} | Error: {e}")

        st.info(f"📊 Done! Success: {sent}, Failed: {failed}")