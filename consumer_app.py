from flask import Flask, Response
from flask_socketio import SocketIO, send, emit
from pykafka import KafkaClient
import json
# gevent is broken somehow -- this is the fix
from gevent import monkey
monkey.patch_all()

# Intiialize app and socket
app = Flask(__name__)
socketIO = SocketIO(app, cors_allowed_origins="http://localhost:3000")

app.debug = True
app.host = 'localhost'

newMsg = "test" # variable which will hold newest kafka message

# Init kafka client
client = KafkaClient(hosts="localhost:9092")
topic = client.topics['droneBusData']

# Serve kafka data through socket
@socketIO.on("dronedata")
def sendMessage():
    global newMsg
    emit("dronedata", newMsg, broadcast=True)
    return None

# set newMsg to new kafka message so SocketIO above can access it
# You need to have localhost:5000 (or wherever this app is running open in your browser for it to work)
@app.route("/")
def index():
    # print("HERE")
    def events():
        for i in topic.get_simple_consumer():
            global newMsg
            newMsg = "{0}".format(i.value.decode()) # needs to be in string form to work
            # print(newMsg)
            yield newMsg
    return Response(events(), mimetype="text/event-stream")

if __name__ == '__main__':
    socketIO.run(app)