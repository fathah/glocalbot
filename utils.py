import re
from result_fetch import get_result,read_json

def getStudentName(id):
    students = read_json("students.json")
    for student in students['data']:
        if student['id'] == id:
            return student['name']
        else:
            pass

def getProgramName(id):
    program = read_json("programs.json")
    for program in program['data']:
        if program['id'] == id:
            return program['name']
        else:
            pass

def getCampusName(id):
    campuses = read_json("campus.json")
    for campus in campuses['data']:
        if campus['campusId'] == id:
            return campus['name']
        else:
            pass

def remove_symbols(text):
    re.sub(r'[^\w]', ' ', text)