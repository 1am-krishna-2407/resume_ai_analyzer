from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def ats_score(resume_text, job_description):

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform([resume_text, job_description])

    similarity = cosine_similarity(vectors)[0][1]

    return round(similarity * 100, 2)