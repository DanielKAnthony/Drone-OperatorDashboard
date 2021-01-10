import React, {useState, useEffect} from 'react';
import DashboardMap from './dashcomps/DashboardMap';
import StatsTable from './dashcomps/StatsTable';

//configure consumer socket
import io from 'socket.io-client';

const conSocket = io("http://127.0.0.1:5000");

export default function DashParent(){

    // droneStates = [id, latitude, longitude, timestamp]
    const [droneData1, setdroneData1] = useState([1, 0, 0, 0]);
    const [droneData2, setdroneData2] = useState([2, 0, 0, 0]);
    const [droneData3, setdroneData3] = useState([3, 0, 0, 0]);
    // counter that changes value after every socket call to ensure useEffect is always called again
    var [ctr, setCtr] = useState(0);

    useEffect(() => {
        conSocket.emit("dronedata")
        updateDrones();        
    }, [ctr]);

    const updateDrones = () => {
        conSocket.on("dronedata", data => {
            try{
                let coords = JSON.parse(data);

                setdroneData1([1, coords['d1Lat'], coords['d1Long'], coords['d1Time']]);
                setdroneData2([2, coords['d2Lat'], coords['d2Long'], coords['d2Time']]);
                setdroneData3([3, coords['d3Lat'], coords['d3Long'], coords['d3Time']]);
            }catch{/* if kafka messages haven't started, prevent droneData from being set to nothing */}

            setCtr(ctr = ctr === 10 ? 0 : ctr + 1);
        });
    };

    return(
        <div style={{height:"50vh",width:"100vw"}}>
            <DashboardMap 
            dronePos={[
                [droneData1[1],droneData1[2]],
                [droneData2[1],droneData2[2]],
                [droneData3[1],droneData3[2]]
            ]}/>
            <div>
                <StatsTable droneOne={droneData1} droneTwo={droneData2} droneThree={droneData3}/>
            </div>
        </div>
    );
}