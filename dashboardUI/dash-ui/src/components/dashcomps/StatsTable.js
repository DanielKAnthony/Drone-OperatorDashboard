export default function StatsTable(props){
    return(
        <table border={1}>
            <th>Drone Id</th>
            <th>Latitude</th>
            <th>Longitude</th>
            <th>TimeStamp</th>
            <tr>
                <td>{props.droneOne[0]}</td>
                <td>{props.droneOne[1]}</td>
                <td>{props.droneOne[2]}</td>
                <td>{props.droneOne[3]}</td>
            </tr>

            <tr>
                <td>{props.droneTwo[0]}</td>
                <td>{props.droneTwo[1]}</td>
                <td>{props.droneTwo[2]}</td>
                <td>{props.droneTwo[3]}</td>
            </tr>

            <tr>
                <td>{props.droneThree[0]}</td>
                <td>{props.droneThree[1]}</td>
                <td>{props.droneThree[2]}</td>
                <td>{props.droneThree[3]}</td>
            </tr>
        </table>
    )
}