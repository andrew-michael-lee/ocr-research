# utils/ocr_utils.py

from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
from pdf2image import convert_from_path
import os

# Load models
_processors = {
    'printed': TrOCRProcessor.from_pretrained('microsoft/trocr-base-stage1'),
    'handwritten': TrOCRProcessor.from_pretrained('microsoft/trocr-large-handwritten')
}
_models = {
    'printed': VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-stage1'),
    'handwritten': VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-large-handwritten')
}

def extract_text_from_image(image_path: str, handwritten: bool = False) -> str:
    mode = 'handwritten' if handwritten else 'printed'
    processor = _processors[mode]
    model = _models[mode]

    image = Image.open(image_path).convert("RGB")
    pixel_values = processor(images=image, return_tensors="pt").pixel_values
    generated_ids = model.generate(pixel_values)
    return processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

def extract_text_from_pdf(pdf_path: str, handwritten: bool = False, dpi: int = 300) -> str:
    """Convert PDF pages to images and extract text from each."""
    mode = 'handwritten' if handwritten else 'printed'
    processor = _processors[mode]
    model = _models[mode]

    pages = convert_from_path(pdf_path, dpi=dpi)
    all_text = []

    for i, page in enumerate(pages):
        print(f"🔍 Processing page {i+1}/{len(pages)}...")
        pixel_values = processor(images=page.convert("RGB"), return_tensors="pt").pixel_values
        generated_ids = model.generate(pixel_values)
        text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        all_text.append(text)

    return "\n\n".join(all_text)