# load the 2 JSON files located in the /data and store them in a local database

import json
import psycopg2
from sqlalchemy import create_engine
import uuid

def read_json_file(file_path):
    '''Function to read the json files, introduce the file path'''
    with open(file_path, 'r') as data_file:
        data = json.load(data_file)
    return data


def upload_users_to_database(data, cursor, conn):
    '''Function to upload users to the local database'''
    insert_sql = """
        INSERT INTO "user" (id, name, email, public_id, phone, account_type, registration_date, status, origin, lang)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    for record in data:
        values = (
            record.get('id', None),
            record.get('name', None),
            record.get('email', None),
            record.get('public_id', None),
            record.get('phone', None),
            record.get('account_type', None),
            record.get('registration_date', None),
            record.get('status', None),
            record.get('origin', None),
            record.get('lang', None)
        )
    
        cursor.execute(insert_sql, values)
    conn.commit()


def upload_subscriptions_to_database(data, cursor, conn):
    '''Function to upload subscriptions to the local database'''
    insert_sql = """
        INSERT INTO "subscription" (id, description, category, timestamp, public_id, user_id)
        VALUES (%s, %s, %s, %s, %s, %s)"""
    #public_id_default = uuid.uuid4().hex
    for record in data:
        values = (
            record.get('id', None),
            record.get('description', None),
            record.get('category', None),
            record.get('timestamp', None),
            record.get('public_id', uuid.uuid4().hex),
            record.get('user_id', None)
        )
    
        cursor.execute(insert_sql, values)
    conn.commit()

#read JSON files located in the /data directory
subscription = read_json_file('/home/dinis/Desktop/alfredo-fullstack-challenge-2/data/subscriptions.json')
user = read_json_file('/home/dinis/Desktop/alfredo-fullstack-challenge-2/data/users.json')
#print(subscription)


#upload the json files directly to a local database
#POSTGRES_USER=admin -e POSTGRES_PASSWORD=thisisatest -e POSTGRES_DB=alfredo -d postgres
#"postgresql+asyncpg://admin:thisisatest@127.0.0.1:5432/alfredo"


#conn_string = "postgresql+asyncpg://admin:thisisatest@127.0.0.1:5432/alfredo"
#db = create_engine(conn_string)
#conn = db.connect()

conn = psycopg2.connect("postgresql://admin:thisisatest@127.0.0.1:5432/alfredo")
cursor = conn.cursor()

upload_subscriptions_to_database(subscription, cursor, conn)

upload_users_to_database(user, cursor, conn)

conn.close()
#df.to_sql('data', con=conn, if_exists = 'replace', index=False)
#upload_files_to_database('subscriptions', subscription)
#upload_files_to_database('users', user)