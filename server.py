from flask import Flask, request, jsonify, send_from_directory
from twilio.rest import Client
from dotenv import load_dotenv
import os

# Load credentials from .env file
load_dotenv()

app = Flask(__name__)

# ─── Twilio Credentials from .env ───────────────────────────────────────────
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN  = os.getenv("TWILIO_AUTH_TOKEN")
FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER")

# Connect to Twilio API
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# ─── Serve Frontend Files ────────────────────────────────────────────────────
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/style.css')
def css():
    return send_from_directory('.', 'style.css')

@app.route('/app.js')
def js():
    return send_from_directory('.', 'app.js')

# ─── Send Bulk SMS Route ─────────────────────────────────────────────────────
@app.route('/send', methods=['POST'])
def send_messages():
    data    = request.get_json()
    numbers = data.get('numbers', [])
    message = data.get('message', '')

    if not numbers or not message:
        return jsonify({'success': False, 'error': 'Numbers or message missing'}), 400

    sent    = 0
    failed  = 0
    details = []

    for number in numbers:
        try:
            # Send SMS via Twilio API
            msg = client.messages.create(
                body  = message,
                from_ = FROM_NUMBER,
                to    = number
            )

            sent += 1
            details.append({
                'number': number,
                'status': 'sent',
                'sid'   : msg.sid
            })
            print(f"✅ Sent to {number} | SID: {msg.sid}")

        except Exception as e:
            failed += 1
            details.append({
                'number': number,
                'status': 'failed',
                'error' : str(e)
            })
            print(f"❌ Failed {number} | Error: {e}")

    return jsonify({
        'success': True,
        'sent'   : sent,
        'failed' : failed,
        'details': details
    })

# ─── Start Server ────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print("="*45)
    print("  📱 Bulk SMS Sender Server Started!")
    print("  Open browser: http://localhost:5000")
    print("="*45)
    app.run(debug=True, port=5000)
