# __init__.py inside app/

from .utils import extract_text_from_pdf, extract_text_from_docx, extract_text_from_url
from .summarizer import summarize_text_chain
from .models import TextRequest
