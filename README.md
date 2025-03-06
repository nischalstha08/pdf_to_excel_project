# PDF-to-Excel Converter

This project converts image-based PDFs into structured Excel files by leveraging OCR and advanced image preprocessing techniques.

## Features

- Converts multi-page PDFs to images.
- Preprocesses images using OpenCV (grayscale, thresholding, noise removal, etc.).
- Uses Tesseract OCR with optimized settings.
- Extracts tables using Camelot and OpenCV.
- Exports data into a well-formatted Excel file.
- Supports batch processing with multiprocessing.

## How to Use

1. Install dependencies from `requirements.txt`.
2. Run `main.py` to process your PDF.
3. Check the `examples/` folder for sample inputs and outputs.

## Installation

```bash
pip install -r requirements.txt

