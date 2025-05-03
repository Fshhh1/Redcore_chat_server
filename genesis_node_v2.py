
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
peers = []

@app.route('/')
def home():
    return "Genesis Node v2 Online (Render Compatible)"

@app.route('/register', methods=['POST'])
def register():
    node_url = request.json.get('node_url')
    if node_url and node_url not in peers:
        peers.append(node_url)
    return jsonify({"peers": peers})

@app.route('/peers', methods=['GET'])
def get_peers():
    return jsonify({"peers": peers})

@app.route('/ping', methods=['GET'])
def ping():
    return "Pong from Genesis Node v2"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7070))
    app.run(host='0.0.0.0', port=port)
