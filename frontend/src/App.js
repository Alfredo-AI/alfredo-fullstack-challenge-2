import React from "react";
import Grid from "@mui/material/Grid";

import { PieChatrt, Pie, Sector, Cell, Tooltip, BarChart, XAxis, YAxis, Legend, CartesianGrid, Bar } from "recharts";

import { useState, useEffect } from "react";
import { ThemeContext } from "@emotion/react";

// urls to access the data 

const url_1week = 'http://localhost:8000/cancellation_reasons?time_window=1week';
const url_1month = 'http://localhost:8000/cancellation_reasons?time_window=1month';
const url_1year = 'http://localhost:8000/cancellation_reasons?time_window=1year';


let url_aux = 'http://localhost:8000/cancellation_reasons?time_window';

let params = (new URL(url_aux)).searchParams //gets values in front of "?"


/*const App = () => {
  const url = 'http://localhost:8000/cancellation_reasons?time_window';
  const [data, setData] = useState([])
  
  fetch(url)
  .then(response => {
    return response.json();
    })
  .then(data => {console.log(data)})
};*/

const App = () => {
  const data = [
    {name: "reason 1", value: 293},
    {name: "reason 2", value: 389},
    {name: "reason 3", value: 94},
  ];

  return (
    <div className="App">
      <h1>Cancellation Reasons</h1>
      <BarChart
          width={500}
          height={300}
          data={data}
          margin={{
            top: 5,
            right: 30,
            left: 20,
            bottom: 5,
          }}
          barSize={20}
        >
          <XAxis dataKey="name" scale="point" padding={{ left: 10, right: 10 }} />
          <YAxis />
          <Tooltip />
          <Legend />
          <CartesianGrid strokeDasharray="3 3" />
          <Bar dataKey="value" fill="#8884d8" background={{ fill: '#eee' }} />
        </BarChart>
    </div>
    
  );
};


export default App;
