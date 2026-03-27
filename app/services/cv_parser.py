from app.services.embedding_service import get_cv_embedding
import fitz
import docx
import spacy
import re

nlp = spacy.load("en_core_web_trf")


def extract_text_from_pdf(file_path):
    text = ""
    doc = fitz.open(file_path)
    for page in doc:
        text += page.get_text()
    return text


def extract_email(text):
    match = re.search(r"[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+", text)
    return match.group(0) if match else None


def extract_skills(text):
    skills_db = ["python", "fastapi", "docker", "sql"]
    text_lower = text.lower()
    return [s for s in skills_db if s in text_lower]


def parse_cv(file_path):
    text = extract_text_from_pdf(file_path)
    doc = nlp(text)

    return {
        "name": next((ent.text for ent in doc.ents if ent.label_ == "PERSON"), None),
        "email": extract_email(text),
        "skills": extract_skills(text),
        "raw_text": text[:500]
    }

def parse_cv_with_embedding(file_path: str):
    parsed = parse_cv(file_path)  # existing parser
    embedding = get_cv_embedding(parsed["raw_text"])
    parsed["embedding"] = embedding
    return parsed