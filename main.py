# main.py

import argparse
import os
from utils.ocr_utils import extract_text_from_image, extract_text_from_pdf

VALID_IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff'}
VALID_PDF_EXTENSION = '.pdf'


def validate_input_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ File not found: {file_path}")

    ext = os.path.splitext(file_path)[1].lower()
    if ext not in VALID_IMAGE_EXTENSIONS and ext != VALID_PDF_EXTENSION:
        raise ValueError(
            f"❌ Unsupported file format. Must be one of: {', '.join(VALID_IMAGE_EXTENSIONS | {VALID_PDF_EXTENSION})}")


def main():
    parser = argparse.ArgumentParser(description="Extract text from an image or PDF using TrOCR.")
    parser.add_argument("input_path", type=str, help="Path to the input image or PDF.")
    parser.add_argument("--output-file", type=str, help="Path to save the extracted text")
    parser.add_argument("--handwritten-mode", action="store_true", help="Use the TrOCR model for handwritten text")

    args = parser.parse_args()

    try:
        validate_input_file(args.input_path)

        ext = os.path.splitext(args.input_path)[1].lower()
        if ext == VALID_PDF_EXTENSION:
            extracted_text = extract_text_from_pdf(args.input_path, handwritten=args.handwritten_mode)
        else:
            extracted_text = extract_text_from_image(args.input_path, handwritten=args.handwritten_mode)

        print("\n📄 OCR Result:\n")
        print(extracted_text)

        if args.output_file:
            with open(args.output_file, 'w') as f:
                f.write(extracted_text)
            print(f"\n✅ Output saved to: {args.output_file}")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()