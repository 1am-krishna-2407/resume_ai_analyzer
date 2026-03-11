import json
import os

def find_skill_gap(role, skills):
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(BASE_DIR, "data", "job_roles.json")
    with open(file_path,"r") as f:
       
        roles = json.load(f)

    required = roles.get(role, [])
    skills = [s.lower() for s in skills]
    required= [r.lower() for r in required]

    missing = list(set(required) - set(skills))

    return missing
