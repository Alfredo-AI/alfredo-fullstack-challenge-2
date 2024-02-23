from fastapi import FastAPI
from flask import *

import json

app = FastAPI(title = "Alfredo Fullstack Challenge")


@app.get("/complaints")
async def get_complaints():
    #data_set = {'Page': 'Complaints', 'Message': 'Successfully loaded the Complaints page'}
    #json_dump = json.dumps(data_set)

    #return json_dump
    return []

@app.get('/cancelation_reasons') #, methods = ['GET']
async def cancelation_reasons(time_window = None):
    if (time_window == "1year"):
        time_window = "ONE YEAR"
    elif (time_window == "1month"):
        time_window = "ONE MONTH"
    elif (time_window == "1week"):
        time_window = "ONE WEEK"
    else:
        time_window = "None"

    data_set = {'Page': 'Cancelation Reasons', 'Message': f'Successfully got the request for {time_window}'}
    json_dump = json.dumps(data_set)

    return json_dump
    #return{"time_window": time_window}