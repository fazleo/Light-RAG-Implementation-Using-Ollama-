```markdown
# 🔦 LightRAG Ollama RAG Pipeline (uv + FAISS + Ollama)

This project sets up a **Retrieval-Augmented Generation (RAG)** system using:

- ⚡ [LightRAG-HKU](https://github.com/light-research/lightrag)
- 🧠 Local LLMs via [Ollama](https://ollama.com)
- 📐 Embeddings via `nomic-embed-text`
- 📦 Vector store: `FAISS`
- 🧰 Environment & dependency management: [`uv`](https://github.com/astral-sh/uv)

---

## 📁 Project Overview

- 🔍 Ingests plain text documents
- 🧠 Retrieves answers using hybrid/local/global/naive RAG modes
- ✅ Runs completely offline with local models
- 🐍 Structured for reproducible builds with `uv`

---

## 📦 Requirements

- Python 3.10+
- [`uv`](https://github.com/astral-sh/uv)
- [Ollama installed and running](https://ollama.com/download)
- Pulled models:
  ```bash
  ollama pull gemma3:4b
  ollama pull nomic-embed-text:latest
  ```

---

## 🚀 Quickstart

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/lightrag-ollama-demo.git
cd lightrag-ollama-demo
```

### 2. Set up environment with `uv`

```bash
uv init
uv venv
source .venv/bin/activate
```

### 3. Add dependencies

If you have `requirements.txt`:

```bash
uv add -r requirements.txt
```

Or add manually:

```bash
uv add lightrag-hku python-dotenv pytest ollama faiss-cpu pymupdf
```

---

## 🧠 Running the RAG Pipeline

Make sure you have a text file (`new.txt`) with content to ingest.

Run the main script:

```bash
uv run main.py
```

This will:
- Initialize vector storage
- Insert contents of `new.txt`
- Query using LightRAG with hybrid mode

---

## 🧪 Example Query Output

```text
=== Querying LightRAG ===

Results using hybrid mode:
Gemma says: Faslu Rahman is mentioned in the document...
```

---

## 📄 requirements.txt

```txt
lightrag-hku
python-dotenv
pytest
ollama
faiss-cpu
pymupdf
```

---

## 🗂 Project Structure

```
lightrag-ollama-demo/
├── main.py              # Main script using LightRAG
├── new.txt              # Input text file for ingestion
├── requirements.txt     # Package list for uv
└── README.md            # Project documentation
```


---

## 🙌 Credits

- [LightRAG-HKU](https://github.com/light-research/lightrag)
- [Ollama](https://ollama.com)
- [Nomic Embeddings](https://embed.nomic.ai)
- [uv](https://github.com/astral-sh/uv)
```
