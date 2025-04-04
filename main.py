from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '✅ Webhook läuft auf Render!'

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    print("✅ Webhook wurde aufgerufen!")

    try:
        # 1. Komplette rohe Anfrage anzeigen (egal welches Format)
        raw_body = request.get_data(as_text=True)
        print("\n📦 ROHDATEN:")
        print(raw_body)

        # 2. Falls Formulardaten vorhanden sind, extra anzeigen
        form_data = request.form.to_dict()
        if form_data:
            print("\n🧾 FORMULARDATEN:")
            for key, value in form_data.items():
                print(f"{key} = {value}")

    except Exception as e:
        print("❌ Fehler beim Verarbeiten:", str(e))

    return "OK", 200

app.run(host="0.0.0.0", port=10000)
