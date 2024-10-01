from fastapi import FastAPI, UploadFile, File, Form
from .models import TextRequest
from .utils import extract_text_from_pdf, extract_text_from_docx, extract_text_from_url
from .summarizer import summarize_text_chain

app = FastAPI()

# Root route
@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI Summarization API"}

# Endpoint 1: Summarize Text Input
@app.post("/summarize_text/")
async def summarize_text(request: TextRequest):
    text = request.text
    style = request.style
    
    # Call the function to generate the summary using LLM chain
    summary = summarize_text_chain(text, style)
    return {"original_text": text, "summary": summary}

# Endpoint 2: Summarize Uploaded Document (PDF, DOCX)
@app.post("/summarize_document_or_pdf/")
async def summarize_document(file: UploadFile = File(...)):
    file_extension = file.filename.split('.')[-1].lower()
    
    if file_extension == "pdf":
        text = extract_text_from_pdf(file.file)
    elif file_extension == "docx":
        text = extract_text_from_docx(file.file)
    else:
        return {"error": "Unsupported file type."}
    
    # Use the LLM chain to summarize the extracted text
    summary = summarize_text_chain(text, "Normal")
    return {"original_text": text, "summary": summary}

# Endpoint 3: Summarize Text from URL
@app.post("/summarize_url/")
async def summarize_url(url: str = Form(...)):
    text = extract_text_from_url(url)
    
    # Use the LLM chain to summarize the text
    summary = summarize_text_chain(text, "Normal")
    return {"original_text": text, "summary": summary}
