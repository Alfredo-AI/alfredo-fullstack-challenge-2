# load the 2 JSON files located in the /data and store them in a local database

import json

def read_json_file(file_path):
    '''Function to read the json files, introduce the file path'''
    with open(file_path, 'r') as data_file:
        data = json.load(data_file)
    return data


def upload_files_to_database(file_name, data):
    '''Function to upload data to the local database'''
    #data.to_sql

#read JSON files located in the /data directory
subscription = read_json_file('/home/dinis/Desktop/alfredo-fullstack-challenge-2/data/subscriptions.json')
user = read_json_file('/home/dinis/Desktop/alfredo-fullstack-challenge-2/data/users.json')

#print(subscription)

#upload the json files directly to a local database


#df.to_sql('data', con=conn, if_exists = 'replace', index=False)
#upload_files_to_database('subscriptions', subscription)
#upload_files_to_database('users', user)