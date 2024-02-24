from fastapi import FastAPI
from flask import *
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

import json, time
import psycopg2

app = FastAPI(title = "Alfredo Fullstack Challenge")


conn = psycopg2.connect("postgresql://admin:thisisatest@127.0.0.1:5432/alfredo")
cursor = conn.cursor()


@app.get("/complaints")
async def get_complaints():
    #data_set = {'Page': 'Complaints', 'Message': 'Successfully loaded the Complaints page'}
    #json_dump = json.dumps(data_set)

    #return json_dump
    return []

@app.get('/cancellation_reasons') #, methods = ['GET']
async def cancellation_reasons(time_window = None):

    current_date = date.today()
    #calculate the initial time based on time_window
    if (time_window == "1year"):
        initial_time = current_date - relativedelta(years=1)
    elif (time_window == "1month"):
        initial_time = current_date - relativedelta(months=1)
    elif (time_window == "1week"):
        initial_time = current_date - relativedelta(weeks=1)
    else:
        # set initial_time to a date very far back when no window is provided
        time_window = "None"
        initial_time = current_date - relativedelta(years=2000) 
    
    insert_sql = """
        SELECT reason, COUNT(status) FROM "subscription" 
        WHERE status = 'canceled' AND 
        date_end < current_date AND date_end > %s
        GROUP BY reason"""
    start_time = (initial_time, )
    cursor.execute(insert_sql, start_time)

    data_set = {'Page': 'Cancellation Reasons', 'Message': f'Successfully got the request for {time_window}',
                'Current time' : f'{current_date}', 'Initial Time': f'{initial_time}'}

    user_table = cursor.fetchall()
    test_schema=[]

    for key, value in user_table:
        test_schema += {f"cancellationReason: {key}, userCount: {value}"}
        #aux += {'cancelationReason': f'{key}', 'userCount': f'{value}'}
    json_dump = json.dumps(data_set)

    return json_dump, test_schema
    #return{"time_window": time_window}
