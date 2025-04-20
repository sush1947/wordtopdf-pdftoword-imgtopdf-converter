from PIL import Image
from docx2pdf import convert as docx_to_pdf
from pdf2docx import Converter
import os

# Create a menu
print("Select an option:")
print("1. Convert Word file to PDF")
print("2. Convert PDF file to Word")
print("3. Convert Image to PDF")

# Get the user's choice
choice = input("Enter your choice: ")

# Convert Word file to PDF
if choice == "1":
    input_file = input("Enter the full path of the input Word file: ")
    output_file = input("Enter the full path of the output PDF file: ")

    # Convert using docx2pdf (only works on Windows)
    try:
        docx_to_pdf(input_file, output_file)
        print("Word file converted to PDF successfully!")
    except Exception as e:
        print("Error:", e)

# Convert PDF file to Word
elif choice == "2":
    input_file = input("Enter the full path of the input PDF file: ")
    output_file = input("Enter the full path of the output Word file: ")

    try:
        cv = Converter(input_file)
        cv.convert(output_file, start=0, end=None)
        cv.close()
        print("PDF file converted to Word successfully!")
    except Exception as e:
        print("Error:", e)

# Convert Image to PDF
elif choice == "3":
    input_file = input("Enter the full path of the input image file: ")
    output_file = input("Enter the full path of the output PDF file: ")

    try:
        image = Image.open(input_file)
        # Convert to RGB if it's PNG or has transparency
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")
        image.save(output_file, "PDF")
        print("Image converted to PDF successfully!")
    except Exception as e:
        print("Error:", e)

else:
    print("Invalid choice!")
