from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def home():
    return '✅ Webhook läuft auf Render!'

@app.route('/webhook', methods=['POST'])
def webhook():
    print("✅ Webhook wurde aufgerufen!")
    try:
        data = request.get_json(force=True)
        print(json.dumps(data, indent=2))
    except Exception as e:
        print("❌ Fehler beim JSON-Verarbeiten:", str(e))
    return "OK", 200

app.run(host="0.0.0.0", port=10000)

