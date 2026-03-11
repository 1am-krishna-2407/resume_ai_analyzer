import pickle
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE_DIR,"models","job_model.pkl")
model, vectorizer = pickle.load(open(path,"rb"))

def predict_role(skills):

    text = " ".join(skills)

    vec = vectorizer.transform([text])

    role = model.predict(vec)[0]

    return role
