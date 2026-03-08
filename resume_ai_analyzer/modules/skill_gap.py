import json

def find_skill_gap(role, skills):

    roles = json.load(open("data/job_roles.json"))

    required = roles.get(role, [])

    missing = list(set(required) - set(skills))

    return missing