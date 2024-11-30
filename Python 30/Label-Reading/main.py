try:
    from PIL import Image
except ImportError:
    import Image # type: ignore

import pytesseract

pytesseract.pytesseract.tesseract_cmd=r'c:\Program Files\Tesseract-OCR\tesseract.exe'

def recText(filename):
    text=pytesseract.image_to_string(Image.open(filename))
    return text

info=recText('Label-Reading/4.jpg')
print(info)

output_file = 'Label-Reading/New.txt'
with open(output_file, "a") as file:
    file.write(info)

print("Written Successfully")