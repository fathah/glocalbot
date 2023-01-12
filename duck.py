import requests
import json

def fetch_and_save(query):
    
    q= query.replace(' ','+')
    url = f'http://api.duckduckgo.com/?q={q}&format=json'
    print(f"fetching {q}")
    response = requests.get(url)

    data = response.json()
    print(data)
    data = data['Abstract'].split('.')[0]
    prev_data = read_json("duck.json")
    prev_data['data'].append({"query":query,"answer":data})

    with open("duck.json", 'w') as f:
        json.dump(prev_data, f)

def read_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def duck_search(query):
   
    prev_data = read_json("duck.json")
    if len(prev_data['data'])>0 :
        for data in prev_data['data']:
            if data['query'] == query:
                return data['answer']
            else:
                return fetch_and_save(query)
    else:
        return fetch_and_save(query)
   

