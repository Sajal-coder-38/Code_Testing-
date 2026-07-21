from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []  # temporary in-memory storage

@app.route('/')
def home():
    return "Task Manager API is running!"

if __name__ == '__main__':
    app.run(debug=True)
