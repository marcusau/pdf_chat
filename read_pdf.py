import os
from pathlib import Path
import pymupdf
from typing import List,Dict,Union

current_dir = Path.cwd()
print(f"Current directory: {current_dir}")

pdf_filename='2024111300327.pdf'
pdf_path = current_dir / pdf_filename
print(f"PDF file path: {pdf_path}")


def read_pdf(pdf_path:Union[Path,str])->List[str]:
    doc_list=[]
    with  pymupdf.open(pdf_path) as f :
        for page_num in range(len(f)):
            page = f[page_num]  # Load the page
            text = page.get_text()  # Extract text from the page
            #print(f"Page {page_num + 1}:\n{text}\n")
            doc_list.append(text)
    return doc_list