# JAMZ Operator Dashboard
So far, dashboard is capable of rendering real-time coordinates of drones along with a timestamp of when the coordinates were produced to the Apache Kafka pipeline.

## Apache Kafka Producer (Python Script)
Messages are produced by executing `drone_location_producer.py`, which parses the JSON files found in `./tempDroneData`. The content in these files were generated by manually drawing routes on geojson.io.

After parsing the files and extracting the coordiantes, a while loop infinitely produces a new message every half-second to the `droneBusData` Kafka topic I created locally.

This file could later be a Flask app itself that connects to the Raspberry Pi chips and generates its messages from there instead of the JSON files.

## Apache Kafka Consumer (Flask App)
On initialization, the consumer app sets up a web socket to emit Kakfa messages to the React app.

The `index` function acts as a listener to the `droneBusData` topic. In order for it to listen, the app needs to be open in a browser, not just running in a CMD which is a drawback that should be watched for now.

The `sendMessage` function with a SocketIO annotation runs every time the equivalent `socketIO.on()` method gets called in React.

## React App
All relevant state variables for now are stored in `DashParent.js` and passed as props to the map and table components accordingly. Putting all this processing power in the parent component takes a toll on the front-end performance, and these socket tasks can be delegated to subcomponents later on to make it run smoothly. 

Since the `useEffect` hook merges the previous functionality of `componentDidMount` and `componentDidUpdate`, a counter state variable was made just to always make sure SocketIO call is made, even if drone data values don't change between two calls.

Leflet was used for map (for now). This can be changed to Google Maps; I'm currently working on another project right now where Leaflet is used, so I could develop it faster as it's fresh.

## Reproducing the Current Functionality
These are the steps you need to take if you wish to get it up and running on your own computer. You need Kafka installed and if you're on a Mac, you'll need to figure out what the equivalents are to the `batch` files that are run in this procedure.

1. Open CMD and go the path where you put the Kafka folder. Then get zookeeper up and running with `./bin/windows/zookeeper-server-start.bat ../../config/zookeeper.properties`

2. Open a new CMD, go to the same path and get the Kafak server running with `kafka-server-start.bat ../../config/server.properties`

3. Open new CMD -> same path, then create a topic called `droneBusData` with the command `kafka-topics.bat --zookeeper 0.0.0.0:2181 --topic droneBusData --create --partitions 1 --replication-factor 1`

4. Start the React development server (can be done at any point)

5. Open another CMD and run `drone_location_producer.py` (keep it running)

6. Start `consumer_app.py` Flask app. Leave it on localhost:5000 to avoid having to change any code. Make sure you open a window in your browser at localhost:5000 as well.

7. React's values and map points should be changing!
