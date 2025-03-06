# PDF to Excel Converter

A robust Python tool for converting both text-based and scanned PDF tables to Excel files with high accuracy using OCR and advanced image processing.

## Features

- **Dual PDF Support:** Handles both text-based and image-based PDFs.
- **Advanced Image Preprocessing:** Utilizes OpenCV for noise removal and enhanced OCR performance.
- **Optimized OCR:** Leverages Tesseract OCR with optimized settings.
- **Table Extraction:** Integrates Camelot for text-based tables.
- **Excel Export:** Automatically adjusts column widths for clarity.
- **Batch Processing:** Supports converting multiple PDFs in one go.
- **Robust Logging:** Detailed logging and error handling for easier troubleshooting.

## Prerequisites

- Python 3.8+
- Tesseract OCR Engine
- Poppler Utils (for PDF-to-image conversion)

## System Dependencies

### Windows

1. **Install Tesseract OCR:**  
   [Tesseract OCR for Windows](https://github.com/UB-Mannheim/tesseract/wiki)

2. **Install Poppler:**  
   [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases/)

### Mac (using Homebrew)


`brew install tesseract poppler`

### Linux (Debian/Ubuntu)

`sudo apt-get install tesseract-ocr poppler-utils`


### Installation

Clone the repository and install the Python dependencies:
```
git clone https://github.com/yourusername/pdf-to-excel-converter.git
cd pdf-to-excel-converter
pip install -r requirements.txt
```

### Usage

Run the converter from the command line by specifying the input PDF and output Excel file:

`python main.py input.pdf output.xlsx`

## Examples

### Convert a Text-Based PDF

`python main.py examples/text_table.pdf text_output.xlsx`

### Convert a Scanned PDF

`python main.py examples/scanned_table.pdf image_output.xlsx`

### Batch Processing

`Use a shell loop to process multiple PDFs:`

```
for pdf in inputs/*.pdf; do
    python main.py "$pdf" "outputs/$(basename "$pdf" .pdf).xlsx"
done
```

### Configuration
Customize processing parameters in the following files:
- `preprocessing.py` : Adjust image processing settings.
- `ocr_module.py`: Tweak OCR engine parameters.
- `table_extraction.py`: Modify table detection thresholds.

## Troubleshooting

### Common Issues
1. Tesseract Not Found Error:
  Ensure that Tesseract is installed and its path is added to the system PATH environment variable.

2. PDF Conversion Errors:
  Verify that Poppler utils are installed and that the PDF file permissions are correct.

3. Missing Dependencies:
  Reinstall requirements by running:
  `pip install -r requirements.txt`

## Contributing
Contributions are welcome! Follow these steps to contribute:
1. Fork the Repository.
2. Create a Feature Branch:
  `git checkout -b feature/your-feature`
3. Commit Your Changes:
   `git commit -m "Add some feature"`
4. Push to Your Branch:
   `git push origin feature/your-feature`
5. Open a Pull Request.




