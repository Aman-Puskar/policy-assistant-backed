from langchain_classic.tools import tool
from clean_context import clean
from context import  retriever
from langchain_community.utilities import GoogleSerperAPIWrapper
from dotenv import load_dotenv
from clean_context import clean_search_tool_result
load_dotenv()


@tool
def get_relevent_info(query: str) ->str:
    """This function gives the appropriate context of the query which has been asked from the user and return plain string of the text"""
    docs = retriever.invoke(query)
    clean_text = clean(docs=docs)
    return clean_text


@tool
def search_tool_for_government_schemes(query: str) ->str:
    """This function will give current information for the user's query using google search"""
    search = GoogleSerperAPIWrapper(k=5,gl="in",hl="en")

    results = search.results(query)
    return clean_search_tool_result(results=results)

tools = [get_relevent_info, search_tool_for_government_schemes]