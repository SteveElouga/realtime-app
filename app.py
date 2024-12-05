from flask import Flask, render_template
from flask_cors import CORS
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = '02149e48f1de528608b4bd6035b036f04f1e802f'
cors = CORS(app, resources={r"*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return "CORS Configured!"

@socketio.on("connect")
def handle_connect():
    print("Client connected")

@socketio.on('message')
def handle_message(message):
    print('Received message: ' + message)
    emit('message', message, broadcast=True)
    emit('notification', {'text':'Message envoye avec succes!'}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)