import json
import os


def list_task():
    if not os.path.isfile('data.json'):
        with open('data.json', 'w') as f:
            json.dump([], f)
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data



#def add():

#def update():

#def delete():

#def mark_in_progress():

#def mark_done():



#def list done():

#def list todo():