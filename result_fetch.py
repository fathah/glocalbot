import requests
import json

def fetch_and_save(url, filename):
    response = requests.get(url)
    data = response.json()
    with open(filename, 'w') as f:
        json.dump(data, f)

def read_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def get_result():
    prListUrl = 'https://api.jamiamadeenathunnoor.org/rendezvous/participation/get.php'
    programsUrl = 'https://api.jamiamadeenathunnoor.org/rendezvous/programs/get.php'
    studentsUrl = 'https://api.jamiamadeenathunnoor.org/rendezvous/students/get.php'
    campusUrl = 'https://api.jamiamadeenathunnoor.org/rendezvous/campus/get.php'

    fetch_and_save(prListUrl, "prList.json")
    fetch_and_save(programsUrl, "programs.json")
    fetch_and_save(studentsUrl, "students.json")
    fetch_and_save(campusUrl, "campus.json")


    return True