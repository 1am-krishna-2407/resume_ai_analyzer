import streamlit as st

from modules.parser import extract_text
from modules.skill_extractor import extract_skills
from modules.job_classifier import predict_role
from modules.ats_calculator import ats_score
from modules.skill_gap import find_skill_gap

st.title("AI Resume Analyzer")

resume = st.file_uploader("Upload Resume",type=["pdf"])

job_desc = st.text_area("Paste Job Description")

if resume:

    text = extract_text(resume)

    skills = extract_skills(text)

    st.subheader("Extracted Skills")

    for s in skills:
        st.write("✔",s)

    role = predict_role(skills)

    st.subheader("Predicted Role")

    st.success(role)

    if job_desc:

        score = ats_score(text,job_desc)

        st.subheader("ATS Score")

        st.progress(int(score))

        st.write(score,"% match")

        gaps = find_skill_gap(role,skills)

        st.subheader("Missing Skills")

        for g in gaps:
            st.write("❌",g)