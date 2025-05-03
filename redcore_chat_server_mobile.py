# redcore_chat_server_mobile.py
from flask import Flask, request, jsonify

app = Flask(__name__)

memory_store = {}

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()
    response = generate_response(user_input)
    return jsonify({"response": response})

def generate_response(user_input):
    if "hello" in user_input:
        return "Greetings, Commander."
    elif "pulse" in user_input:
        return "Pulse is stable at 74Hz."
    elif "uptime" in user_input:
        return "Genesis Node running for several cycles."
    else:
        return f"Received: {user_input}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)