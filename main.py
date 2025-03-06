
import argparse
from .pdf_to_images import convert_pdf_to_images, is_text_based
from .preprocessing import preprocess_image
from .ocr_module import perform_ocr
from .table_extraction import structure_table_from_ocr, extract_tables_camelot
from .excel_export import export_to_excel

def process_pdf(pdf_path: str, output_path: str):
    try:
        if is_text_based(pdf_path):
            tables = extract_tables_camelot(pdf_path)
            if tables.n > 0:
                export_to_excel(tables[0].df.values.tolist(), output_path)
                return
        
        images = convert_pdf_to_images(pdf_path)
        all_data = []
        for img in images:
            processed = preprocess_image(img)
            ocr_data = perform_ocr(processed)
            table_data = structure_table_from_ocr(ocr_data)
            all_data.extend(table_data)
        
        export_to_excel(all_data, output_path)
        
    except Exception as e:
        logger.error(f"Processing failed: {e}")
        raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='PDF to Excel Converter')
    parser.add_argument('input', help='Input PDF file path')
    parser.add_argument('output', help='Output Excel file path')
    args = parser.parse_args()
    
    process_pdf(args.input, args.output)