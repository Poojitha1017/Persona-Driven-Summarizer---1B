import json

def build_output_json(documents, persona, job, timestamp, top_sections, output_path):
    extracted = []
    refined = []

    for section in top_sections:
        extracted.append({
            "document": section["document"],
            "importance_rank": section["importance_rank"],
            "section_title": section["section_title"],
            "page_number": section["page_number"]
        })
        refined.append({
            "document": section["document"],
            "importance_rank": section["importance_rank"],
            "refined_text": section["refined_text"],
            "page_number": section["page_number"]
        })

    result = {
        "metadata": {
            "input_documents": documents,
            "persona": persona,
            "job_to_be_done": job,
            "processing_timestamp": timestamp
        },
        "extracted_sections": extracted,
        "subsection_analysis": refined
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
