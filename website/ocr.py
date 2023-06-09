import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"


def extract_text(img):
    text = pytesseract.image_to_string(
        img, lang="tur", config='--psm 6 -c tessedit_char_whitelist=0123456789 --oem 3 -l tur')
    return text
