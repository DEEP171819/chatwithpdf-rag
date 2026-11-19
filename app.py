import os
import streamlit as st
from src.utils import create_directories
from src.pdf_loader import load_pdf
from src.text_splitter import split_text
from src.embeddings import get_embedding_model
from src.vector_store import create_vector_store
from src.rag_chain import get_qa_chain

create_directories()

st.set_page_config(page_title="Chat with PDF", layout="wide")
st.title("📄 Chat with PDF using RAG")
st.markdown("---")


@st.cache_resource
def cached_embedding_model():
    return get_embedding_model()


uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file:
    safe_name = os.path.basename(uploaded_file.name)
    file_path = f"data/uploaded_pdfs/{safe_name}"
    file_key = f"{safe_name}-{uploaded_file.size}"

    # Process the PDF only once per file, not on every Streamlit rerun
    if st.session_state.get("file_key") != file_key:
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner("Processing PDF..."):
            documents = load_pdf(file_path)
            if not documents:
                st.error("Could not read any text from this PDF.")
                st.stop()
            chunks = split_text(documents)
            vector_db = create_vector_store(
                chunks, cached_embedding_model(), file_key
            )
            retriever = vector_db.as_retriever(search_kwargs={"k": 4})
            st.session_state["qa_chain"] = get_qa_chain(retriever)
            st.session_state["file_key"] = file_key
        st.success("PDF processed successfully!")

    question = st.text_input("Ask a question from the PDF")

    if question:
        with st.spinner("Thinking..."):
            try:
                response = st.session_state["qa_chain"].invoke(question)
                st.subheader("Answer")
                st.write(response)
            except Exception as e:
                st.error(f"Error: {e}")
