import os
def load_skills():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    skills_path = os.path.join(BASE_DIR,"data", "skills.txt")
    
    with open(skills_path,"r") as f:
        skills = f.read().splitlines()

    return skills


def extract_skills(text):

    skills = load_skills()

    found = []

    for skill in skills:
        if skill in text:
            found.append(skill)

    return list(set(found))
