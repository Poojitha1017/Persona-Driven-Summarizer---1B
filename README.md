# 🧠 Persona-Driven Document Intelligence Backend (Round 1B)

This repository contains the **Dockerized backend solution** for **Round 1B** of the _“Connecting the Dots”_ Challenge. The goal is to build a document analysis engine that extracts and ranks **semantically relevant content** from multiple PDF files based on a **persona's needs and intent**.

---

## 📌 Problem Statement

Participants are required to build a backend system that:

- Accepts **3 to 10 PDF documents**
- Accepts a **persona and job-to-be-done** input
- Outputs a **ranked, structured summary** from the documents based on the persona’s interests

---

## ✅ Key Features

- 🧠 **Embedding-Based Semantic Ranking** using [`intfloat/e5-small-v2`](https://huggingface.co/intfloat/e5-small-v2)
- 📂 Parses both native and scanned PDFs using:
  - **PyMuPDF** for text-based PDFs
  - **Tesseract OCR** for scanned images
- 📊 Ranks extracted chunks for relevance to the persona's task
- 🪄 Outputs `challenge1b_output.json` containing:
  - `title`: Section or content title
  - `summary`: Summarized key points
  - `relevance_score`: Semantic score based on persona
  - `source_filename`: Original PDF file source

---

## 🧱 Tech Stack

| Component           | Tool / Library                                      |
|---------------------|-----------------------------------------------------|
| Programming         | Python 3.10                                         |
| PDF Parsing         | PyMuPDF, pytesseract, Pillow                        |
| Embedding Model     | `intfloat/e5-small-v2` (via Hugging Face Transformers) |
| Semantic Analysis   | Sentence Transformers, Scikit-learn, Torch          |
| Containerization    | Docker (platform: `linux/amd64`)                    |

---

## 📁 Folder Structure

