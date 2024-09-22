from src.helper import load_pdf, text_split, download_hugging_face_embedding
from langchain_community.vectorstores import Pinecone
from pinecone.grpc import PineconeGRPC
from dotenv import load_dotenv
import os

load_dotenv()

pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone_host = os.getenv("PINECONE_API_HOST")
pinecone_index_name = os.getenv("PINECONE_INDEX_NAME")

extracted_data = load_pdf("data/")

text_chunks = text_split(extracted_data)

embeddings = download_hugging_face_embedding()

pc = PineconeGRPC(api_key=pinecone_api_key)

docsearch = Pinecone.from_texts([t.page_content for t in text_chunks], index_name=pinecone_index_name, embedding=embeddings)

