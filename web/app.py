from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Route halaman beranda
@app.route('/')
def beranda():
    return render_template('beranda.html')

# Route halaman chat
@app.route('/chat')
def chat():
    return render_template('chat.html')

# Endpoint untuk chatbot
@app.route('/get_weather', methods=['POST'])
def get_weather():
    user_message = request.json.get("message")
    rasa_response = requests.post(
        "http://localhost:5005/webhooks/rest/webhook",  # Endpoint Rasa
        json={"sender": "user", "message": user_message},
    )
    bot_response = rasa_response.json()
    return jsonify(bot_response)

if __name__ == "__main__":
    app.run(debug=True)
