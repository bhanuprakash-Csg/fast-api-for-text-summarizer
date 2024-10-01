from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Create the ChatOllama instance
llm = ChatOllama(
    model="llama2:7b",
    temperature=0.5,
    n_gpu_layers=50,
    n_batch=4096,
    n_ctx=4096,
    max_tokens=4096,
    top_p=1,
    verbose=True
)

# Define prompt templates
prompt_templates = {
    "Creative": """
    Be creative and provide a summary for the following text using your unique writing style.
    {text}
    CREATIVE SUMMARY:
    """,
    "Normal": """
    Write a concise summary of the following text delimited by triple backticks in a single line.
    {text}
    CONCISE SUMMARY:
    """,
    "Academic": """
    Summarize the text in an academic style using proper language and structure.
    {text}
    ACADEMIC SUMMARY:
    """
}

# Function to summarize the text using LLM chain
def summarize_text_chain(text: str, style: str) -> str:
    # Get the prompt template based on the selected style
    template = prompt_templates.get(style, prompt_templates["Normal"])
    prompt = PromptTemplate(template=template, input_variables=["text"])
    llm_chain = prompt | llm 
    
    # Invoke the LLM chain to get the summary
    result = llm_chain.invoke({"text": text})
    
    return result.content
