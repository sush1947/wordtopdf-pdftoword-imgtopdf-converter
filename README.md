# wordtopdf-pdftoword-imgtopdf-converter

A Python-based file conversion tool that allows users to convert various types of files between formats. Currently, the tool supports the following file conversions:

- Word to PDF
- PDF to Word
- Image to PDF

## Features

- **Convert Word to PDF**: Converts a `.docx` Word file to a `.pdf` file.
- **Convert PDF to Word**: Converts a `.pdf` file to a `.docx` Word file.
- **Convert Image to PDF**: Converts an image file (e.g., `.png`, `.jpg`, `.jpeg`) to a PDF document.

## Requirements

Before running the project, make sure you have the following Python libraries installed:

- `pdf2image` - for converting PDF files to images
- `Pillow` (PIL) - for image manipulation
- `python-docx` - for working with `.docx` files
- `docxtopdf` - for converting Word files to PDF

You can install the required libraries using the following command:

```bash
pip install pdf2image Pillow python-docx docxtopdf
