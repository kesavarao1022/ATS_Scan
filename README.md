# ATS Resume Scanner 🧠📄

An intelligent Applicant Tracking System (ATS) Resume Scanner built using **Tokenization** and **Cosine Similarity** to assess how well a resume matches a given job description. This project aims to automate the resume screening process, helping recruiters and applicants save time and effort.

---

## 🔍 Features

- 🔢 Uses **Tokenization** to preprocess and vectorize text.
- 📈 Applies **Cosine Similarity** to score resume relevance against job descriptions.
- 📄 Upload and scan resumes in `.txt`, `.pdf`, or `.docx` formats.
- 🧪 Clean, testable code with modular functions for easy extension.
- 🧠 Useful for both **recruiters** and **job seekers** to optimize the hiring process.

---

## 🚀 How It Works

1. **Input**: Job Description and Resume(s).
2. **Text Processing**: Tokenization, lowercasing, stopword removal, and vectorization using TF-IDF.
3. **Scoring**: Calculates cosine similarity between job description and each resume.
4. **Output**: Shows similarity scores and highlights the most relevant resumes.

---

## 🛠️ Tech Stack

- Python 🐍
- Scikit-learn
- NLTK / spaCy (for text processing)
- Streamlit (optional UI)
- PyPDF2 / python-docx (for reading various file types)

---

## 📂 Project Structure


---

## ✅ Getting Started

### Prerequisites

- Python 3.7+
- pip

### Installation

```bash
git clone https://github.com/kesavarao1022/ATS_Scan
cd ats-resume-scanner
pip install -r requirements.txt


---

Let me know if you want a version that includes screenshots, Streamlit web interface details, or an example resume/job description.
