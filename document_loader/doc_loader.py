import openai
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone
import pinecone
from langchain.llms import OpenAI
from regex import R



# loading pdf files from a directory
def read_file_from_directory(directory_path):
    loader = PyPDFDirectoryLoader(directory_path)
    documents = loader.load()
    return documents

# splitting the documents into smaller chunks
def split_documents(documents, chunk_size=1000, chunk_overlap=50):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    doc = text_splitter.split_documents(documents)
    return doc 

embeddings = OpenAIEmbeddings()
pinecone.init(api_key="pcsk_58ybMT_PNF5UafLF2eUJN614JWqGPtoD4JERU8UcxmmMjDFhr5RxiNwcW1DdPFDZFVHG6P",)

index_name="langchainvector"




document = read_file_from_directory("document_loader\document")
split_docs = split_documents(document)

