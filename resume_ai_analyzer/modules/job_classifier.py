import pickle
import os
path = os.path.join("models","job_model.pkl")
model, vectorizer = pickle.load(open(path,"rb"))

def predict_role(skills):

    text = " ".join(skills)

    vec = vectorizer.transform([text])

    role = model.predict(vec)[0]

    return role