from fastapi import FastAPI
from flask import *

import json, time
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

app = FastAPI(title = "Alfredo Fullstack Challenge")


@app.get("/complaints")
async def get_complaints():
    #data_set = {'Page': 'Complaints', 'Message': 'Successfully loaded the Complaints page'}
    #json_dump = json.dumps(data_set)

    #return json_dump
    return []

@app.get('/cancelation_reasons') #, methods = ['GET']
async def cancelation_reasons(time_window = None):

    current_date = date.today()

    if (time_window == "1year"):
        initial_time = current_date - relativedelta(years=1)
    elif (time_window == "1month"):
        initial_time = current_date - relativedelta(months=1)
    elif (time_window == "1week"):
        initial_time = current_date - relativedelta(weeks=1)
    else:
        time_window = "None"
        initial_time = current_date - relativedelta(years=2000)

    data_set = {'Page': 'Cancelation Reasons', 'Message': f'Successfully got the request for {time_window}',
                'Current time' : f'{current_date}', 'Initial Time': f'{initial_time}'}
    json_dump = json.dumps(data_set)

    return json_dump
    #return{"time_window": time_window}