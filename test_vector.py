# test_vector.py
import numpy as np
from app.services.embedding_service import get_cv_embedding

# Example job postings
job_postings = [
    "Python developer with Django experience",
    "Frontend React developer"
]

# Candidate CV text
cv_text = "I have experience in Python, Django, and building backend APIs."

# Get embedding for candidate CV
cv_embedding = np.array(get_cv_embedding(cv_text))

# Convert all job embeddings
job_embeddings = [np.array(get_cv_embedding(job)) for job in job_postings]

# Compute cosine similarity
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

similarities = [cosine_similarity(cv_embedding, job_vec) for job_vec in job_embeddings]

# Rank jobs by similarity (higher = better)
top_indices = np.argsort(similarities)[::-1]

print("🔍 Top Matches:\n")
for rank, idx in enumerate(top_indices, start=1):
    print(f"Rank #{rank}")
    print(f"Score: {similarities[idx]:.4f}")  # cosine similarity
    print(f"Job: {job_postings[idx]}")
    print("-" * 40)