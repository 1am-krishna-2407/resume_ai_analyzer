# AI Resume Analyzer 🚀

## Overview

The **AI Resume Analyzer** is a machine learning–powered application that analyzes resumes and evaluates how well they match job requirements. The system extracts skills from a candidate’s resume, predicts the most suitable job role, calculates an **ATS (Applicant Tracking System) compatibility score**, and identifies **skill gaps** compared to job descriptions.
Working Link: [https://resumeaianalyzer-2.streamlit.app/](https://resumeaianalyzer-2.streamlit.app/)

This project demonstrates the practical integration of:

* **Natural Language Processing (NLP)**
* **Machine Learning**
* **Resume Parsing**
* **Skill Extraction**
* **Job Role Prediction**
* **ATS Compatibility Evaluation**

The application is built using **Python, Streamlit, and Scikit-Learn**, making it easy to run locally or deploy on the web.

---

# Key Features ✨

### 1. Resume Parsing

The system extracts text from uploaded resumes (PDF format) using **PyPDF2**.

Capabilities:

* Extracts raw textual content from resumes
* Prepares data for further NLP analysis
* Supports multi-page resumes

---

### 2. Skill Extraction

The system identifies relevant skills from the resume text by comparing it with a predefined skill dataset.

Process:

1. Load skill list from `skills.txt`
2. Scan the resume text
3. Match detected keywords
4. Return unique extracted skills

Example extracted skills:

```
Python
Machine Learning
TensorFlow
SQL
Data Analysis
```

---

### 3. Job Role Prediction

The system predicts the **most suitable job role** for the candidate based on the extracted skills.

Method:

* Skills are converted into text features
* A trained **machine learning classifier** predicts the role

Example predictions:

```
Data Scientist
Machine Learning Engineer
Data Analyst
Backend Developer
AI Engineer
```

The trained model is stored in:

```
models/job_model.pkl
```

---

### 4. ATS Score Calculation

Most companies use **Applicant Tracking Systems (ATS)** to filter resumes. This module evaluates how closely the resume matches the job description.

Method Used:

* **TF-IDF Vectorization**
* **Cosine Similarity**

Formula:

```
ATS Score = CosineSimilarity(Resume, JobDescription) × 100
```

Example Output:

```
ATS Score: 78.5%
```

A higher score indicates a stronger match between the resume and the job description.

---

### 5. Skill Gap Analysis

This module identifies **missing skills** required for a specific job role.

Steps:

1. Load required skills from `job_roles.json`
2. Compare them with extracted resume skills
3. Display missing skills

Example:

```
Required Skills: Python, SQL, Machine Learning, Deep Learning
Resume Skills: Python, SQL

Missing Skills:
Deep Learning
Machine Learning
```

This helps candidates improve their resumes.

---

# System Architecture 🧠

```
             +----------------------+
             |   Upload Resume PDF  |
             +----------+-----------+
                        |
                        v
                Resume Parser
                        |
                        v
               Text Extraction
                        |
                        v
                Skill Extractor
                        |
                        v
              Extracted Skills List
                        |
          +-------------+-------------+
          |                           |
          v                           v
   Job Role Prediction        ATS Score Calculator
          |                           |
          v                           v
   Predicted Role            Resume vs Job Description
          |
          v
     Skill Gap Analyzer
          |
          v
  Missing Skills Recommendation
```

---

# Project Structure 📁

```
resume_ai_analyzer/
│
├── app.py
│
├── modules/
│   ├── parser.py
│   ├── skill_extractor.py
│   ├── ats_calculator.py
│   ├── job_classifier.py
│   └── skill_gap.py
│
├── data/
│   ├── skills.txt
│   └── job_roles.json
│
├── models/
│   └── job_model.pkl
│
├── train_model.py
│
└── requirements.txt
```

---

# Module Explanation 🔎

## 1. app.py

Main Streamlit application.

Responsibilities:

* User interface
* File upload
* Display results

Workflow:

```
Upload Resume → Extract Skills → Predict Role → Calculate ATS → Skill Gap
```

---

## 2. parser.py

Extracts text from PDF resumes.

Function:

```
extract_text(file)
```

Library Used:

```
PyPDF2
```

---

## 3. skill_extractor.py

Extracts skills using keyword matching.

Functions:

```
load_skills()
extract_skills(text)
```

Input:

```
Resume Text
```

Output:

```
List of detected skills
```

---

## 4. job_classifier.py

Predicts the job role based on extracted skills.

Model Type:

```
Machine Learning Classifier
```

Process:

```
Skills → Vectorizer → ML Model → Predicted Role
```

---

## 5. ats_calculator.py

Calculates resume compatibility score with the job description.

Algorithm:

```
TF-IDF + Cosine Similarity
```

Function:

```
ats_score(resume_text, job_description)
```

---

## 6. skill_gap.py

Identifies missing skills required for a role.

Function:

```
find_skill_gap(role, skills)
```

Dataset used:

```
data/job_roles.json
```

---

# Installation Guide ⚙️

## Step 1 — Clone the Repository

```
git clone https://github.com/yourusername/resume-ai-analyzer.git
cd resume-ai-analyzer
```

---

## Step 2 — Create Virtual Environment

Linux / Mac:

```
python3 -m venv venv
source venv/bin/activate
```

Windows:

```
python -m venv venv
venv\Scripts\activate
```

---

## Step 3 — Install Dependencies

```
pip install -r requirements.txt
```

---

## Step 4 — Run the Application

```
streamlit run app.py
```

Open browser:

```
http://localhost:8501
```

---

# Example Workflow 🧪

1️⃣ Upload Resume (PDF)

2️⃣ System extracts:

```
Python
Machine Learning
Pandas
NumPy
SQL
```

3️⃣ Model predicts:

```
Data Scientist
```

4️⃣ User enters Job Description

5️⃣ System outputs:

```
ATS Score: 82.4%
```

6️⃣ Missing skills:

```
Deep Learning
TensorFlow
```

---

# Technologies Used 💻

| Technology        | Purpose               |
| ----------------- | --------------------- |
| Python            | Core programming      |
| Streamlit         | Web interface         |
| Scikit-Learn      | Machine learning      |
| PyPDF2            | PDF parsing           |
| TF-IDF            | Text vectorization    |
| Cosine Similarity | ATS score calculation |

---

# Future Improvements 🚀

Potential enhancements:

* Deep learning–based skill extraction
* Named Entity Recognition (NER)
* Resume ranking system
* Multiple resume comparison
* GPT-based resume feedback
* LinkedIn profile analyzer
* Resume improvement suggestions
* Support for DOCX resumes

---

# Use Cases 📊

* Job seekers improving resumes
* ATS optimization
* Career guidance platforms
* HR resume screening
* Recruitment automation tools

---

# Limitations ⚠️

* Works only with **PDF resumes**
* Skill extraction relies on **keyword matching**
* ATS score is based on **text similarity only**
* Job prediction depends on the training dataset

---

# Author

AI Resume Analyzer Project

Developed as a **Machine Learning + NLP portfolio project** demonstrating practical implementation of resume intelligence systems.

---

# License

This project is open-source and available under the **MIT License**.

---

