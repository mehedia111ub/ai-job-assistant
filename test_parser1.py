from app.services.cv_parser import parse_cv
from app.services.embedding_service import get_cv_embedding


if __name__ == "__main__":
    sample_text = """
    John Doe is a software engineer with experience in Python,
    machine learning, and web development.
    """

    # Test embedding directly
    embedding = get_cv_embedding(sample_text)

    if embedding:
        print("✅ Embedding generated successfully")
        print("Embedding length:", len(embedding))
        print("First 5 values:", embedding[:5])
    else:
        print("❌ Embedding failed")