from flask import Flask, render_template, request, jsonify
from src.helper import download_hugging_face_embedding
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain_community.vectorstores import Pinecone
from pinecone.grpc import PineconeGRPC
from langchain.chains import RetrievalQA
from src.prompt import prompt_template
import pinecone
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# pinecone_api_key = os.getenv("PINECONE_API_KEY")
# pinecone_host = os.getenv("PINECONE_API_HOST")
# pinecone_index_name = os.getenv("PINECONE_INDEX_NAME")

# embeddings = download_hugging_face_embedding()

# pc = PineconeGRPC(api_key=pinecone_api_key)

# docsearch = Pinecone.from_existing_index(index_name=pinecone_index_name, embedding=embeddings)
# query = "What is the most common side effect of having Tylenol?"
# docs = docsearch.similarity_search(query, k=3)
# print("Result: ", docs)

# PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
# chain_type_kwargs={"prompt": PROMPT}

# llm=CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
#                   model_type="llama",
#                   config={'max_new_tokens':512,
#                           'temperature':0.6})

# qa=RetrievalQA.from_chain_type(
#     llm=llm, 
#     chain_type="stuff", 
#     retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
#     return_source_documents=True, 
#     chain_type_kwargs=chain_type_kwargs)


@app.route("/")
def index():
    return render_template("chat.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)