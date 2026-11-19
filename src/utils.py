import os

def create_directories():

    directories = [
        "data/uploaded_pdfs",
        "db/chroma_db"
    ]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)