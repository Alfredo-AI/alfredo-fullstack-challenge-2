# load the 2 JSON files located in the /data and store them in a local database

import json
import psycopg2
from sqlalchemy import create_engine

def read_json_file(file_path):
    '''Function to read the json files, introduce the file path'''
    with open(file_path, 'r') as data_file:
        data = json.load(data_file)
    return data


def upload_users_to_database(data):
    '''Function to upload data to the local database'''
    insert_sql = """
        INSERT INTO "user" (id, name, email, public_id, phone, account_type, registration_date, status, origin, lang)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    #option 1, for cycle
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


def upload_subscriptions_to_database(data):
    '''Function to upload data to the local database'''
    #option 1, for cycle
    for record in data:
        insert_sql = """
        INSERT INTO subscription (id, description, category, timestamp, public_id, user_id)
        VALUES """
        #cursor.execute(insert_sql, records)

#read JSON files located in the /data directory
subscription = read_json_file('/home/dinis/Desktop/alfredo-fullstack-challenge-2/data/subscriptions.json')
user = read_json_file('/home/dinis/Desktop/alfredo-fullstack-challenge-2/data/users.json')
#print(subscription)


#upload the json files directly to a local database
#POSTGRES_USER=admin -e POSTGRES_PASSWORD=thisisatest -e POSTGRES_DB=alfredo -d postgres
#"postgresql+asyncpg://admin:thisisatest@127.0.0.1:5432/alfredo"

#user_postgres = "admin"
#passworld_postgres = "thisisatest"
#db_postgres = "alfredo"

#conn_string = "postgresql+asyncpg://admin:thisisatest@127.0.0.1:5432/alfredo"
#db = create_engine(conn_string)
#conn = db.connect()



conn = psycopg2.connect("postgresql://admin:thisisatest@127.0.0.1:5432/alfredo")
cursor = conn.cursor()


upload_users_to_database(user)
#upload_subscriptions_to_database(subscription)




conn.close()
#df.to_sql('data', con=conn, if_exists = 'replace', index=False)
#upload_files_to_database('subscriptions', subscription)
#upload_files_to_database('users', user)