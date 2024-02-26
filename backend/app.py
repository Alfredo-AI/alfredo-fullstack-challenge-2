from fastapi import FastAPI
from flask import *
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

import json, time
import psycopg2

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title = "Alfredo Fullstack Challenge")

origins = [
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost:3000/",
    "http://localhost:8000/cancellation_reasons?time_window",
    "http://localhost:8000/cancellation_reasons?time_window=1year",
    "http://localhost:8000/",
    "http://localhost:8000/cancellation_reasons",
    "http://localhost:8000/cancellation_reasons/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
conn = psycopg2.connect("postgresql://admin:thisisatest@127.0.0.1:5432/alfredo")
cursor = conn.cursor()

#var express = require('express')
#var cors = require('cors')
#var app = express()

#app.use(cors())

@app.get("/complaints")
async def get_complaints():
    return []

@app.get('/cancellation_reasons')
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

    # display an informative message
    #data_set = {'Message': f'Successfully got the request for time_window={time_window}',
                #'Current time' : f'{current_date}', 'Initial Time': f'{initial_time}'}

    user_table = cursor.fetchall()
    test_schema=[]

    # assign the cancellation reason; 
    # this can also be done using a dictionary with the possible cancellation reasons
    for key, user_count in user_table:
        if key == "card":
            reason = "Problemas ao renovar/atualizar"
        elif key == "features":
            reason = "Falta de features"
        elif key == "competitor":
            reason = "Prefiro outras soluções disponíveis no mercado"
        elif key == "price":
            reason = "O preço é demasiado alto"
        elif key == "value":
            reason = "Não vejo valor suficiente pelo preço"
        elif key == "avm":
            reason = "Pouca precisão nas avaliações de imóveis"
        elif key == "metasearch":
            reason = "Cobertura insuficiente no metasearch"
        elif key == "customization":
            reason = "Poucas opções de personalização"
        elif key == "team":
            reason = "A equipa não utiliza a plataforma"
        elif key == "closing":
            reason = "Mudança de atividade/fecho de empresa"
        elif key == "sold":
            reason = "Não ter acesso a dados de transação"
        else:
            reason = "Outra"

        test_schema += {f'"cancellationReason": {reason}, "userCount": {user_count}'}

    #json_dump = json.dumps(data_set)

    return test_schema # json_dump,  # returning test_schema instead of user_table
