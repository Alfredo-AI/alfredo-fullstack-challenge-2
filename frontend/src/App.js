import React from "react";
import { Tooltip, BarChart, XAxis, YAxis, Legend, CartesianGrid, Bar } from "recharts";
import { useState, useEffect } from "react";

const App = () => {
    const [data, setData] = useState([])
    const [selected, setSelected] = useState('') 
    const handleChange=(e)=>{
      console.log(e.target.value)
      setSelected(e.target.value)
    }
  
    useEffect(() => {
      fetch(`http://localhost:8000/cancellation_reasons?time_window=${selected}`, {method: 'GET'}, {mode: 'cors'})
    .then(response => { console.log(response)
      return response.json();
      })
    .then(data => {console.log(data)
      setData(data);})
    .then(error => {console.log(error)})
    },[selected])
  
    return (
      <div className="App">
        <h3>Select the desired time window:</h3>
        <select value={selected} onChange={(e)=>handleChange(e)}>
        <option>default</option>
        <option>1year</option>
        <option>1month</option>
        <option>1week</option>
        </select>
        <h1>Subscription Cancellation Reasons</h1>
        <BarChart
            width={1000}
            height={500}
            data={data}
            margin={{
              top: 5,
              right: 30,
              left: 20,
              bottom: 5,
            }}
            barSize={20}
          >
            <XAxis dataKey="cancellationReason" scale="point" padding={{ left: 10, right: 10 }} />
            <YAxis />
            <Tooltip />
            <Legend />
            <CartesianGrid strokeDasharray="3 3" />
            <Bar dataKey="userCount" fill="#8884d8" background={{ fill: '#eee' }} />
          </BarChart>
      </div>
    );
  };

  export default App;
