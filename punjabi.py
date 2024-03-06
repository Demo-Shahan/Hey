# @title Default title text

# import gdown
# file_id = '1BP4hHb3WnyjpcFpAJXaT7UQcMzPMk9Zb'
# output_path = '/'
# url = f'https://drive.google.com/uc?id={file_id}'
# gdown.download(url, output_path, quiet=True)




from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader, PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from langchain.vectorstores import Chroma, Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
import langchain_pinecone
import os

load_dotenv()



# Embeddings

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
embeddings = OpenAIEmbeddings(openai_api_key= OPENAI_API_KEY )

vectorstore = langchain_pinecone.PineconeVectorStore.from_existing_index(index_name= 'langcahin1', embedding = embeddings)

from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain

llm = ChatOpenAI(temperature=0.5, openai_api_key=OPENAI_API_KEY)
chain = load_qa_chain(llm, chain_type="stuff")


def reply(query):
    docs = vectorstore.similarity_search(query)

    query2 = f"""  

    "As an AI assistant you provide answers based on the given context, ensuring accuracy and brifness.You always follow these guidelines: 
    If the answer isn't available within the context, just say that you don't know. Otherwise, answer to your best capability, refering to source of documents provided. 
    Only use examples if explicitly requested. Do not introduce examples outside of the context. Do not answer if context is absent. 
    Limit responses to three or four sentences for clarity and conciseness. Make sure to reply in the same language font of user uses to ask below question. 

    Question: {query}

    """
    try:
        rep = chain.run(input_documents=docs, question=query2)
    except Exception as e:
        rep = 'ExceptionError: Looks like invalid api-key'
    return rep
    

    
