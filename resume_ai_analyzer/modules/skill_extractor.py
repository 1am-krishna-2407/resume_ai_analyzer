import os
def load_skills():
    path = os.path.join("data", "skills.txt")
    
    with open(path) as f:
        skills = f.read().splitlines()

    return skills


def extract_skills(text):

    skills = load_skills()

    found = []

    for skill in skills:
        if skill in text:
            found.append(skill)

    return list(set(found))
