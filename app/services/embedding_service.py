import os
import certifi

# ✅ Force correct SSL cert (overwrite broken env)
os.environ["SSL_CERT_FILE"] = certifi.where()

from ollama import Client

# Initialize Ollama client
client = Client(host="http://127.0.0.1:11434")


def get_cv_embedding(text: str):
    try:
        response = client.embeddings(
            model="nomic-embed-text",
            prompt=text
        )

        return response["embedding"]

    except Exception as e:
        print(f"[ERROR] Failed to get embedding: {e}")
        return None