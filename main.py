from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


@app.get('/health')
def health():
    return jsonify({'ok': True, 'service': 'flask-example'})


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=False, port=int(os.getenv('PORT', '5000')))
