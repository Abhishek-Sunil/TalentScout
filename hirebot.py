import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter





st.header("TalentScout Hiring Bot")

with st.sidebar:
    st.title("model training pdf")
    file=st.file_uploader("Upload PDF", type=["pdf"], key="pdf_uploader")
    
#To extract text from the pdf file 
if file is not None:
    pdf_page= PdfReader(file)
    text=""
    for page in pdf_page.pages:
        text += page.extract_text()
        # st.write(text)
        
    #break the text to chunks
    text_splitter= RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size=1000, 
        chunk_overlap=150,
        length_function=len
    )
    chunks= text_splitter.split_text(text)
    # st.write(chunks)
# Embedding the text chunks
