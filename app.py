import streamlit as st
from parser import extract_text_from_pdf, extract_skills

st.set_page_config(page_title="AI Resume Screener", layout="wide")

st.title("🤖 AI Resume Screening & Ranking System")

job_description = st.text_area("Enter Job Description")

uploaded_files = st.file_uploader(
    "Upload Resumes", type="pdf", accept_multiple_files=True
)

results = []

if uploaded_files and job_description:
    jd_skills = extract_skills(job_description.lower())

    for uploaded_file in uploaded_files:
        text = extract_text_from_pdf(uploaded_file)
        resume_skills = extract_skills(text)

        matched = set(resume_skills).intersection(set(jd_skills))

        if len(jd_skills) > 0:
            match_percent = (len(matched) / len(jd_skills)) * 100
        else:
            match_percent = 0

        results.append({
            "name": uploaded_file.name,
            "match": match_percent,
            "skills": resume_skills,
            "matched": list(matched)
        })

    results = sorted(results, key=lambda x: x["match"], reverse=True)

    st.subheader("Candidate Ranking")

    for i, res in enumerate(results):
        st.write(f"### {i+1}. {res['name']}")
        st.progress(int(res["match"]))
        st.write(f"Match: {res['match']:.2f}%")
        st.write("Matched Skills:", res["matched"])
        st.write("---")