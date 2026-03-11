import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

data = {
"text":[
"python machine learning pandas numpy tensorflow",
"sql tableau data analysis power bi",
"python opencv deep learning computer vision",
"react javascript css html frontend",
"nodejs mongodb backend api development"
],

"role":[
"Data Scientist",
"Data Analyst",
"Computer Vision Engineer",
"Frontend Developer",
"Backend Developer"
]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(df["text"])

model = LogisticRegression()
model.fit(X, df["role"])

pickle.dump((model,vectorizer),open("models/job_model.pkl","wb"))