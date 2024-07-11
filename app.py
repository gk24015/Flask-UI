from flask import Flask, render_template, jsonify, request
import logging

app = Flask(__name__)

# Configure the logger to only log the messages from our logger and not the Flask or other module logs
logger = logging.getLogger('appLogger')
logger.setLevel(logging.INFO)
handler = logging.FileHandler('app.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Remove the default Flask logger handlers to avoid duplicating logs
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Global variable to store the percentage
current_percentage = 0

@app.route('/')
def index():
    return "Welcome to the logging dashboard!"

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/logs')
def get_logs():
    logs = []
    with open('app.log', 'r') as f:
        for line in f.readlines():
            parts = line.split(' - ', 2)
            if len(parts) == 3:
                timestamp, level, message = parts
                logs.append({
                    'timestamp': timestamp,
                    'level': level,
                    'message': message.strip()
                })
    return jsonify(logs)

@app.route('/<username>', methods=['POST'])
def receive_data(username):
    global current_percentage
    data = request
    current_percentage = 93
    logger.info(f"Data received from {username}: {current_percentage}%")
    print("Received")
    return jsonify("sent")

@app.route('/percentage')
def get_percentage():
    global current_percentage
    return jsonify({'percentage': current_percentage})

if __name__ == '__main__':
    app.run(debug=True)
