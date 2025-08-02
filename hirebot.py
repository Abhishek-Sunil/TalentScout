import streamlit as st





st.header("TalentScout Hiring Bot")

with st.sidebar:
    st.title("model training pdf")
    file=st.file_uploader("Upload PDF", type=["pdf"], key="pdf_uploader")
    
