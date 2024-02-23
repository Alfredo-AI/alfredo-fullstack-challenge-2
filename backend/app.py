from fastapi import FastAPI
from flask import *
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

import json, time
import psycopg2

app = FastAPI(title = "Alfredo Fullstack Challenge")

conn = psycopg2.connect("postgresql://admin:thisisatest@127.0.0.1:5432/alfredo")
cursor = conn.cursor()

insert_sql = """
    SELECT reason, COUNT(status) FROM "subscription" 
    WHERE status = 'canceled' 
    GROUP BY reason"""
cursor.execute(insert_sql)


@app.get("/complaints")
async def get_complaints():
    #data_set = {'Page': 'Complaints', 'Message': 'Successfully loaded the Complaints page'}
    #json_dump = json.dumps(data_set)

    #return json_dump
    return []

@app.get('/cancellation_reasons') #, methods = ['GET']
async def cancellation_reasons(time_window = None):

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

    data_set = {'Page': 'Cancellation Reasons', 'Message': f'Successfully got the request for {time_window}',
                'Current time' : f'{current_date}', 'Initial Time': f'{initial_time}'}
    
    user_table = cursor.fetchall()
    json_dump = json.dumps(data_set)


    return json_dump, user_table
    #return{"time_window": time_window}
