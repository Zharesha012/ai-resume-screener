import pdfplumber
import spacy
nlp = spacy.load("en_core_web_sm")
SKILLS = [
    "python","java","sql","html","css","javascript",
    "react","node","machine learning","deep learning",
    "aws","docker","kubernetes","git","linux",
    "pandas","numpy","tensorflow","flask","django"
]

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text.lower()

def extract_skills(text):
    found_skills = []
    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)
    return found_skills