from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models.openai import ChatOpenAI
from langchain.utilities import GoogleSearchAPIWrapper
from langchain.retrievers.web_research import WebResearchRetriever
from langchain.chains import RetrievalQAWithSourcesChain

import logging

# Vectorstore
vectorstore = Chroma(embedding_function=OpenAIEmbeddings(),persist_directory="./chroma_db_oai")
# LLM
llm = ChatOpenAI(temperature=0)
# Search 
search = GoogleSearchAPIWrapper()

# Initialize
web_research_retriever = WebResearchRetriever.from_llm(
    vectorstore=vectorstore,
    llm=llm, 
    search=search)

# Run
logging.basicConfig()
logging.getLogger("langchain.retrievers.web_research").setLevel(logging.INFO)
user_input = "How do LLM Powered Autonomous Agents work?"
qa_chain = RetrievalQAWithSourcesChain.from_chain_type(llm,retriever=web_research_retriever)
result = qa_chain({"question": user_input})
result