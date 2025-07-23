import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Step 1: Load documents from local folder
loader = DirectoryLoader('./legal_docs', glob="**/*.txt")
documents = loader.load()

# Step 2: Split documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)

# Step 3: Generate vector embeddings
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
vectorstore = FAISS.from_documents(texts, embeddings)

# Step 4: Set up the RAG pipeline
retriever = vectorstore.as_retriever()
llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# Step 5: Ask questions
while True:
    query = input("\nAsk a legal question (or type 'exit' to quit): ")
    if query.lower() == 'exit':
        break
    result = qa_chain.run(query)
    print(f"\n🔍 Answer: {result}")