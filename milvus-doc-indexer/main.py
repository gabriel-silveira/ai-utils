import os
from src.services.milvus_service import index_in_milvus
from src.services.docling_service import load_documents_with_docling


if __name__ == "__main__":
  document_paths = []
  markdown_dir = "data/bulas"

  # 0. Get all markdown files
  for filename in os.listdir(markdown_dir):
    if filename.endswith('.md'):
      file_path = os.path.join(markdown_dir, filename)

      document_paths.append(file_path)

  # 1. Load Docling documents
  docling_docs = load_documents_with_docling(document_paths)

  # 2. Index in Milvus vector database
  # index_in_milvus(docling_docs)