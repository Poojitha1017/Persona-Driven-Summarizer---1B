# 📄 Approach Explanation – Persona-Driven Document Intelligence (Round 1B)

This submission outlines the methodology adopted to solve the persona-driven document understanding challenge. The goal was to extract and rank semantically relevant information from multiple PDF documents based on a given persona's intent and job-to-be-done.

## 📚 Input Processing

The system begins by reading all the PDFs from the `/input` folder. These documents may be in native text format or scanned images. To handle this variability:
- **Text-based PDFs** are processed using **PyMuPDF** to extract text and metadata.
- **Scanned/image-based PDFs** are processed using **Tesseract OCR**, enabling the system to extract textual content via image-to-text conversion.

Each page is split into smaller **semantic chunks** for better granularity during ranking.

## 🧠 Semantic Embedding with Persona Intent

The core of our approach lies in **semantic matching** between document content and persona intent. We utilize the Hugging Face transformer model [`intfloat/e5-small-v2`] for encoding:
- The **persona's task and need** (combined into a single prompt)
- Each document chunk extracted from the PDFs

The embeddings are generated using the `sentence-transformers` library to maintain consistency in vector space.

## 🧮 Relevance Scoring

We compute **cosine similarity** between the persona embedding and each chunk embedding to determine relevance. The top-ranked chunks are selected based on this similarity score.

These relevant chunks are then sorted and grouped by:
- `title` (when available or inferred)
- `summary` (condensed version of content)
- `relevance_score` (cosine similarity)
- `source_filename` (to trace the origin)

All results are compiled into the required format and saved as `challenge1b_output.json`.

## ⚙️ Modular & Dockerized Backend

The backend has been **modularized** into:
- `extractor/` for OCR and text extraction
- `model/` for embedding and similarity logic
- `main.py` for orchestration

A working **Dockerfile** has been provided to enable consistent execution across environments.

## ✅ Outcome

The system is robust against PDF variety and can semantically understand and rank sections relevant to user personas. It maintains offline capability, minimal dependencies, and follows the challenge guidelines strictly.

