from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/message')
def message():
    return jsonify({
        "status": "success",
        "message": "Hello from Python Backend EC2! veera sir"
    })

@app.route('/')
def home():
    return "Python Backend Running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
