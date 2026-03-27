# vector_store.py
import numpy as np
from app.services.embedding_service import get_cv_embedding

class VectorStore:
    def __init__(self):
        self.job_postings = []
        self.job_embeddings = []

    def add_job(self, job_text):
        """Add a job posting and its embedding."""
        embedding = np.array(get_cv_embedding(job_text))
        self.job_postings.append(job_text)
        self.job_embeddings.append(embedding)

    def cosine_similarity(self, vec1, vec2):
        """Compute cosine similarity between two vectors."""
        return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

    def rank_jobs(self, cv_text, top_k=None):
        """Rank jobs by similarity to the candidate CV."""
        cv_embedding = np.array(get_cv_embedding(cv_text))
        similarities = [self.cosine_similarity(cv_embedding, job_vec) for job_vec in self.job_embeddings]

        # Sort indices by similarity descending
        sorted_indices = np.argsort(similarities)[::-1]

        # Limit top_k if specified
        if top_k:
            sorted_indices = sorted_indices[:top_k]

        results = []
        for rank, idx in enumerate(sorted_indices, start=1):
            results.append({
                "rank": rank,
                "score": similarities[idx],
                "job": self.job_postings[idx]
            })
        return results

# Create a reusable instance
vector_store = VectorStore()