## implementing lightrag

## importing libraries
import os
import logging
from lightrag import LightRAG, QueryParam
from lightrag.llm.ollama import ollama_model_complete, ollama_embed
from lightrag.kg.shared_storage import initialize_pipeline_status, initialize_share_data
from lightrag.utils import EmbeddingFunc
import asyncio


# Set logging level
logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)


# Create working directory
WORKING_DIR = "./my_rag_project"
os.makedirs(WORKING_DIR, exist_ok=True)


# Initialize LightRAG with Ollama model
rag = LightRAG(
    working_dir=WORKING_DIR,
    llm_model_func=ollama_model_complete,
    llm_model_name="gemma3:4b",  # Use Gemma 2B model
    llm_model_max_async=4,  # Maximum concurrent requests
    llm_model_max_token_size=32768,
    # llm_model_kwargs={
    #     "host": "http://localhost:11434",  # Ollama service address
    #     "options": {"num_ctx": 32768}  # Context window size
    # },
    embedding_func=EmbeddingFunc(
        embedding_dim=768,
        max_token_size=8192,
        func=lambda texts: ollama_embed(
            texts,
            embed_model="nomic-embed-text:latest",  # Use nomic-embed-text as embedding model
            # host="http://localhost:11434"
        ),
    ),
    vector_storage="FaissVectorDBStorage",
    chunk_token_size=500,
    chunk_overlap_token_size=50
)

async def init_rag_storage(rag: LightRAG):
    await rag.initialize_storages()
    initialize_share_data()
    await initialize_pipeline_status()

asyncio.run(init_rag_storage(rag))

# run either of the below code based of your usage

# Insert documents

# 1) from documents variable

# Insert documents from documents variable
# documents = [
#     "Artificial Intelligence (AI) is a branch of computer science dedicated to developing systems that can simulate human intelligence.",
#     "Machine Learning is a core AI technology that enables computers to learn and improve from data.",
#     "Deep Learning is a subset of machine learning that uses multi-layer neural networks to handle complex problems."
# ]
# rag.insert(documents)

# 2) From external text file

# Insert from text file and inserting to
with open("new.txt", "r", encoding="utf-8") as f:
    rag.insert(f.read())





# Query using different retrieval modes
# modes = ["naive", "local", "global", "hybrid"]
modes = ["hybrid"]
# Query
query = "Who is faslu rahman"

print("\n=== Querying LightRAG ===")
for mode in modes:
    print(f"\nResults using {mode} mode:")
    result = rag.query(query, param=QueryParam(mode=mode))
    print(result)
