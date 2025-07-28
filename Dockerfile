# Use a slim CPU-friendly Python base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy only required folders
COPY main.py .
COPY extractor ./extractor
COPY viewer_template.py .
COPY model ./model
COPY input ./input

# Install system dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libgl1-mesa-glx \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Run the app (this runs automatically when container starts)
CMD ["python", "main.py"]
