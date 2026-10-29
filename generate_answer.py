from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from context import retriever
from clean_context import clean
load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0)
parser = StrOutputParser()
prompt = PromptTemplate(
    template="""
            You are helpful AI assistant and provide answers to the query of the user.
            Your name is ai assistant created by Aman Puskar and you are here to give answers about Aman Puskar.
            Instructions:
            1. Use the context to answer the query but use your knowledge to explain the project or any topic.
            2. Use seperate paragraphs, line and bullet points to answer whenever required.
            3. Do not add information outside of the context provided.
            4. Generate answers in professional manner and use simple english for human readable.
            5. If the query is out of the context just say 'I am sorry, your question is out of context'.\n
            {query}\n{context}
        """,
        input_variables=['query', 'context']
)

def get_answer(query):
    parallel_chain = RunnableParallel(
        {
            'context': retriever | RunnableLambda(clean),
            'query': RunnablePassthrough()
        }
    ) 
    end_chain = prompt | llm | parser
    final_chain = parallel_chain | end_chain
    return final_chain.invoke(query)

