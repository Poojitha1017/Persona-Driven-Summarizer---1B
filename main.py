import os
from datetime import datetime
from extractor.section_extractor import extract_chunks_from_pdfs
from extractor.semantic_ranker import find_top_k_sections
from extractor.summary_generator import build_output_json
from extractor.utils import load_model

# === Configuration ===
PDF_DIR = "input"
MODEL_PATH = "model/e5-small-v2"
OUTPUT_JSON = "challenge1b_output.json"
TOP_K = 7

if __name__ == "__main__":
    print("🚀 Persona-Driven Document Intelligence (Round 1B)")

    persona = input("👤 Enter the persona description: ").strip()
    job = input("🛠️  Enter the job-to-be-done: ").strip()

    pdfs = [f for f in os.listdir(PDF_DIR) if f.endswith(".pdf")]
    if not pdfs:
        print("⚠️ No PDF files found in 'input/' directory.")
        exit(1)

    print(f"📄 Found {len(pdfs)} PDF(s): {[os.path.basename(p) for p in pdfs]}")

    model = load_model(MODEL_PATH)
    chunks = extract_chunks_from_pdfs(PDF_DIR, pdfs)
    query = f"I am a {persona}. I need to {job}. What sections help me the most?"

    top_sections = find_top_k_sections(model, query, chunks, k=TOP_K)
    timestamp = datetime.now().isoformat()
    build_output_json(pdfs, persona, job, timestamp, top_sections, OUTPUT_JSON)

    print(f"✅ Output written to: {OUTPUT_JSON}")
