import hashlib
from langchain_chroma import Chroma

PERSIST_DIR = "db/chroma_db"


def create_vector_store(chunks, embedding_model, source_name):
    """Build a fresh vector store for one PDF (no duplicate chunks on re-run)."""
    collection = "pdf_" + hashlib.md5(source_name.encode()).hexdigest()[:16]

    # Drop any old collection for this file, then rebuild it
    Chroma(
        collection_name=collection,
        embedding_function=embedding_model,
        persist_directory=PERSIST_DIR,
    ).delete_collection()

    vector_db = Chroma(
        collection_name=collection,
        embedding_function=embedding_model,
        persist_directory=PERSIST_DIR,
    )
    vector_db.add_documents(chunks)
    return vector_db
