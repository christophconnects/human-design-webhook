from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def home():
    return '✅ Webhook läuft auf Render!'

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return "✅ Webhook erreichbar (GET)", 200

    try:
        data = request.get_json(force=True)

        print("✅ Webhook wurde aufgerufen!")
        print("📦 Rohdaten (JSON):")
        print(json.dumps(data, indent=2))

        # Custom Fields auslesen
        geburtsdatum = data.get("custom_fields", {}).get("geburtsdatum")
        geburtszeit = data.get("custom_fields", {}).get("geburtszeit")
        geburtsort = data.get("custom_fields", {}).get("geburtsort")

        print(f"📅 Geburtsdatum: {geburtsdatum}")
        print(f"🕒 Geburtszeit: {geburtszeit}")
        print(f"📍 Geburtsort: {geburtsort}")

    except Exception as e:
        print("❌ Fehler beim Verarbeiten:", str(e))

    return "OK", 200

app.run(host="0.0.0.0", port=10000)
