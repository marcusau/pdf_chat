from langchain_ollama import OllamaEmbeddings
import numpy as np

# Initialize the Ollama embeddings model
embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")

# Example text to embed
text = "LangChain is a framework for developing applications powered by language models."

# Generate embeddings
embedding_vector = embeddings.embed_query(text)  # Changed from embed() to embed_query()

# Print vector dimensions and size
print(f"Vector dimensions: {len(embedding_vector)}")
print(f"Vector shape: {np.array(embedding_vector).shape}")
print(f"Sample of vector values:")
#print(embedding_vector[:5])  # Print first 5 values as sample