===============================================
   📱 BULK SMS SENDER - PROJECT README
===============================================

FOLDER STRUCTURE:
-----------------
bulk_sms_project/
│
├── .env          ← Your secret API credentials
├── server.py     ← Python backend (Flask + Twilio)
├── index.html    ← Web page (frontend)
├── style.css     ← Design/styling
├── app.js        ← JavaScript logic
└── README.txt    ← This file

===============================================
STEP 1: INSTALL REQUIRED LIBRARIES
===============================================

Open terminal/command prompt and type:

    pip install flask twilio python-dotenv

===============================================
STEP 2: CHECK YOUR .env FILE
===============================================

Open .env file and confirm your credentials:

    TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxx
    TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    TWILIO_FROM_NUMBER=+19789513604

⚠️  WARNING: Never share .env file with anyone!

===============================================
STEP 3: RUN THE SERVER
===============================================

In terminal, go to this folder and type:

    python server.py

You will see:
    =============================================
      📱 Bulk SMS Sender Server Started!
      Open browser: http://localhost:5000
    =============================================

===============================================
STEP 4: USE THE APP
===============================================

1. Open browser
2. Go to: http://localhost:5000
3. Type your message
4. Click "Send to All 5 Numbers"
5. Wait for the result report

===============================================
FIXED PHONE NUMBERS (5 numbers):
===============================================

+9779800000001
+9779800000002
+9779800000003
+9779800000004
+9779800000005

To change numbers → edit app.js file
Look for: const FIXED_NUMBERS = [...]

===============================================
OFFLINE MESSAGE DELIVERY:
===============================================

If a phone is OFFLINE when you send:
- Twilio sends to mobile network carrier
- Carrier STORES the message
- When phone comes back ONLINE → message delivered
- This happens AUTOMATICALLY, no extra code needed!

===============================================
COMMON ERRORS:
===============================================

Error: "AuthenticationError"
→ Fix: Check Account SID and Auth Token in .env

Error: "Unverified number" (Free Trial)
→ Fix: Go to twilio.com → Verified Caller IDs
       → Add and verify the number first

Error: "Cannot connect to server"
→ Fix: Make sure server.py is running first!

===============================================
