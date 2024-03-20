#best one btw
import requests
import io
import easyocr
import concurrent.futures

# Function to perform OCR on a given URL
def ocr_from_url(url):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(url)
    extracted_text = ''
    for detection in result:
        extracted_text += detection[1] + ' '
    return extracted_text

# Read the file containing URLs
file_path = 'list-of-url.txt'  # Replace with the actual file path
with open(file_path, 'r') as file:
    urls = file.readlines()

# Perform OCR on each URL concurrently and combine the extracted text
combined_text = ''
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(ocr_from_url, urls)
    for result in results:
        combined_text += result + '\n'  # Add a new line after each URL's text

# Print the combined text
print(combined_text)

