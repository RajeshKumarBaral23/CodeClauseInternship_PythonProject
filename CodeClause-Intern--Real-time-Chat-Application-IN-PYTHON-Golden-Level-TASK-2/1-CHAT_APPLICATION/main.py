import os
from flask import Flask, render_template
from flask_socketio import SocketIO, send

# Set Flask environment to development
os.environ['FLASK_ENV'] = 'development'

# Initialize Flask app and SocketIO
app = Flask(__name__)
app.config['SECRET_KEY'] = "secret!123"
socketio = SocketIO(app, cors_allowed_origins='*', async_mode='threading')

@socketio.on('message')
def handle_message(message):
    print("Received message:", message)  # Debug print to console
    if message != "User connected!":
        send(message, broadcast=True)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True, use_reloader=False, allow_unsafe_werkzeug=True)
