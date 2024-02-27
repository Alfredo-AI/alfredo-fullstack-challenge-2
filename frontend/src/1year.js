import React from "react";
import Grid from "@mui/material/Grid";

import { Tooltip, BarChart, XAxis, YAxis, Legend, CartesianGrid, Bar } from "recharts";

import { useState, useEffect } from "react";

const App = () => {
  const url = 'http://localhost:8000/cancellation_reasons?time_window=1year';
  const [data, setData] = useState([])
  const requestOptions = {
    method: 'GET'
  };

  fetch(url, requestOptions, {mode: 'cors'})
  .then(response => { console.log(response)
    return response.json();
    })
  .then(data => {console.log(data)
    setData(data);})
  .then(error => {console.log(error)})

  return (
    <div className="App">
      <h1>Cancellation Reasons</h1>
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
