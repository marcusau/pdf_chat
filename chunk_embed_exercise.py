import os
from pathlib import Path
import pymupdf
from typing import List,Dict,Union
# pip install langchain-text-splitters
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

current_dir = Path.cwd()
print(f"Current directory: {current_dir}")

# Initialize the Ollama embeddings model
embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")

pdf_filename='2024111300327.pdf'
pdf_path = current_dir / pdf_filename
print(f"PDF file path: {pdf_path}")


def read_pdf(pdf_path:Union[Path,str])->List[Document]:
    doc_list=[]
    with  pymupdf.open(pdf_path) as f :
        for page_num in range(len(f)):
            page = f[page_num]  # Load the page
            text = page.get_text()  # Extract text from the page
            #print(f"Page {page_num + 1}:\n{text}\n")
            doc_list.append(Document(page_content=text))
    return doc_list

doc_list = read_pdf(pdf_path)
print(f"Number of pages: {len(doc_list)}")

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(doc_list)
print(f"Number of chunks: {len(splits)}")


# Create a directory for storing the vector database
persist_directory = current_dir / "chroma_db"
# Create the vectorstore and persist it to disk
vectorstore = Chroma.from_documents(
    documents=splits, 
    embedding=embeddings,
    persist_directory=str(persist_directory)
)
# Persist the database to disk
vectorstore.persist()
