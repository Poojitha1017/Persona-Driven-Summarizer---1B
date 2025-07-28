import os
import fitz
import pytesseract
from PIL import Image
from extractor.utils import clean_text, smart_chunk

def extract_text_from_page(page):
    text = page.get_text()
    if text.strip():
        return clean_text(text)

    # OCR fallback for scanned/image PDFs
    pix = page.get_pixmap()
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    text = pytesseract.image_to_string(img)
    return clean_text(text)

def extract_chunks_from_pdfs(pdf_dir, filenames, chunk_size=60, stride=30):
    all_chunks = []
    for file in filenames:
        full_path = os.path.join(pdf_dir, file)
        doc = fitz.open(full_path)
        for i, page in enumerate(doc):
            page_text = extract_text_from_page(page)
            for chunk in smart_chunk(page_text, chunk_size, stride):
                all_chunks.append((file, i + 1, chunk))
    return all_chunks
