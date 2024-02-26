import React from "react";
import Grid from "@mui/material/Grid";

//import { PieChatrt, Pie, Sector, Cell, Tooltip, BarChart, XAxis, YAxis, Legend, CartesianGrid, Bar } from "recharts";

import { useState, useEffect } from "react";
//import { ThemeContext } from "@emotion/react";

// urls to access the data 

//const url_1week = 'http://localhost:8000/cancellation_reasons?time_window=1week';
//const url_1month = 'http://localhost:8000/cancellation_reasons?time_window=1month';
//const url_1year = 'http://localhost:8000/cancellation_reasons?time_window=1year';


//let url_aux = 'http://localhost:8000/cancellation_reasons?time_window';

//let params = (new URL(url_aux)).searchParams //gets values in front of "?"


const App = () => {
  const url = 'http://localhost:8000/cancellation_reasons';
  
  const requestOptions = {
    method: 'GET'
  };

  fetch(url, requestOptions, {mode: 'cors'})
  .then(response => { console.log(response)
    return response.json();
    })
  .then(data => {console.log(data)})
  .then(error => {console.log(error)})
};

/*const DataFetcher = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);


useEffect(() => {
  fetchData();
}, []);

  const fetchData = async () => {
    try {
      const response = await fetch('http://localhost:8000/cancellation_reasons');
      if (!response.ok) {
        throw new Error('Network response was not ok.');
      }
      const data = await response.json();
      setData(data);
      setLoading(false);
    } catch (error) {
      setError(error.message);
      setLoading(false);
    }
  };

return (
  <div>
    {loading ? (
      <p>Loading...</p>
    ) : error ? (
      <p>Error: {error}</p>
    ) : (
      <ul>
        {data.map((item) => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    )}
  </div>
);
};*/

/*const App = () => {
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
};*/


export default App;
