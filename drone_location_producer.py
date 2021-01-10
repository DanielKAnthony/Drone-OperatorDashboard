from pykafka import KafkaClient
from datetime import datetime
import json
import time

print("Initializing producer... ", end="", flush=True)

# process json data for each drone
drone1_input = open('./tempDroneData/drone1.json')
d1_json = json.load(drone1_input)
d1_coords = d1_json['features'][0]['geometry']['coordinates']

drone2_input = open('./tempDroneData/drone2.json')
d2_json = json.load(drone2_input)
d2_coords = d2_json['features'][0]['geometry']['coordinates']

drone3_input = open('./tempDroneData/drone3.json')
d3_json = json.load(drone3_input)
d3_coords = d3_json['features'][0]['geometry']['coordinates']

# Establish kafka connection
client = KafkaClient(hosts="localhost:9092")
topic = client.topics['droneBusData']
producer = topic.get_sync_producer()

print("Done")

# Empty kafka message to be populated and produced
drone_data = {}

i = j = k = 0
while i < len(d1_coords):
    # Construct dictionary and produce json message to kafka 
    drone_data['d1Time'] = str(datetime.utcnow())
    drone_data['d1Lat'] = d1_coords[i][1]
    drone_data['d1Long'] = d1_coords[i][0]

    drone_data['d2Time'] = str(datetime.utcnow())
    drone_data['d2Lat'] = d2_coords[i][1]
    drone_data['d2Long'] = d2_coords[i][0]

    drone_data['d3Time'] = str(datetime.utcnow())
    drone_data['d3Lat'] = d3_coords[i][1]
    drone_data['d3Long'] = d3_coords[i][0]

    msg = json.dumps(drone_data)
    producer.produce(msg.encode('ascii'))

    # Infinitely loop for now to show continuous path
    i = 0 if i == len(d1_coords) - 1 else i + 1
    j = 0 if j == len(d2_coords) - 1 else j + 1
    k = 0 if k == len(d3_coords) - 1 else k + 1
    # Going at full speed causes backlog -- limit production to every half second
    time.sleep(0.5)