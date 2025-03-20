import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(file):
    pdf = PdfReader(file)
    text = "" 
    for page in pdf.pages:
        text+=page.extract_text()
    return text

def rank_resume(job_description, resumes):
    documents = [job_description]+resumes
    vectorizer = TfidfVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()
    job_description_vector = vectors[0]
    resume_vector = vectors[1:]
    cosine_similarites = cosine_similarity([job_description_vector], resume_vector).flatten()
    return cosine_similarites

#Streamlit
st.title("AI Resume Screening and Ranking System")

st.header("Job Description")

job_description = st.text_area("Enter the Job description") 

st.header("Upload Resumes")

uploaded_files = st.file_uploader("Upload Pdf Files", type=["pdf"], accept_multiple_files = True)

if uploaded_files and job_description:
    st.header("Ranking Resumes")

    resumes =[]
    for file in uploaded_files:
        text = extract_text_from_pdf(file)
        resumes.append(text) 
    scores = rank_resume(job_description, resumes)

    results = pd.DataFrame({"Resume":[file.name for file in uploaded_files],"score":scores})
    
    st.write(results)