from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '✅ Webhook läuft auf Render!'

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return "✅ Webhook erreichbar (GET)", 200

    print("✅ Webhook wurde aufgerufen!")

    try:
        # Formulardaten (klassisch übermitteltes Format von Digistore)
        form_data = request.form.to_dict()
        print("📦 Formulardaten (Digistore):")
        for key, value in form_data.items():
            print(f"{key} = {value}")

        # Custom Fields einzeln extrahieren
        geburtsdatum = form_data.get("custom_fields[geburtsdatum]", "nicht angegeben")
        geburtszeit = form_data.get("custom_fields[geburtszeit]", "nicht angegeben")
        geburtsort = form_data.get("custom_fields[geburtsort]", "nicht angegeben")

        print(f"\n📅 Geburtsdatum: {geburtsdatum}")
        print(f"🕒 Geburtszeit: {geburtszeit}")
        print(f"📍 Geburtsort: {geburtsort}")

    except Exception as e:
        print("❌ Fehler beim Verarbeiten:", str(e))

    return "OK", 200

app.run(host="0.0.0.0", port=10000)
