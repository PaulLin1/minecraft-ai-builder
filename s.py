import json
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import JSONLoader, DirectoryLoader
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

json_dir_loader = DirectoryLoader('', glob="**/[!.]*.json", loader_cls=JSONLoader, loader_kwargs={"jq_schema" : ".[]", "text_content" : False},)

documents = json_dir_loader.load()

embeddings = OpenAIEmbeddings()

persist_dir = 'vector.db'

# vectordb = Chroma.from_documents(documents=documents, embedding=embeddings, persist_directory=persist_dir)

# vectordb.persist()