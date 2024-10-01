import PyPDF2
from docx import Document
import requests
from bs4 import BeautifulSoup
import validators

# Function to extract text from PDF files
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page].extract_text()
    return text

# Function to extract text from Word (docx) files
def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text

# Function to extract text from URLs
def extract_text_from_url(url):
    if not validators.url(url):
        return "Invalid URL"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        text = ''
        for paragraph in soup.find_all('p'):
            text += paragraph.get_text(separator='\n')
        return text
    except requests.exceptions.RequestException as e:
        return f"Error fetching the web page: {e}"
