# 🧠 OCR Research with TrOCR

This project uses [Hugging Face's TrOCR](https://huggingface.co/docs/transformers/en/model_doc/trocr#overview) model to extract printed or handwritten text from images and PDFs. Built with modular Python code and a flexible command-line interface, it supports both image files and multi-page PDFs.

---

## 🧰 Tech Stack

- Python 3.9+
- [Transformers](https://huggingface.co/docs/transformers)
- PyTorch
- `pdf2image` for PDF conversion
- `Pillow` for image processing
- CLI built with `argparse`

---

## 🚀 Getting Started (with PyCharm on macOS)

### 1. Clone the Repo

In your terminal:

```bash
git clone https://github.com/andrew-michael-lee/ocr-research.git
cd ocr-research
```

2. Open Project in PyCharm
	•	Open PyCharm.
	•	Go to File > Open and select the ocr-research folder you just cloned.

3. Set Up a Virtual Environment
	1.	Go to PyCharm > Preferences > Project: ocr-research > Python Interpreter.
	2.	Click the ⚙️ icon and select Add….
	3.	Choose Virtualenv Environment:
	•	Select New environment.
	•	Leave the location default (e.g., ocr-research/.venv).
	•	Choose a Python interpreter (e.g., /usr/bin/python3 or one installed with Homebrew).
	4.	Click OK to create and activate the environment.

4. Install Dependencies

In PyCharm’s terminal (or the virtual environment terminal):
```bash
pip install -r requirements.txt
```

📸 Usage

Run the OCR script from the terminal or PyCharm:
```bash
python main.py documents/report.pdf --output-file results/report.txt
```

Options
--handwritten-mode
--output-file output.txt
