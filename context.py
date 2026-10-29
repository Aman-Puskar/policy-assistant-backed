from langchain_community.retrievers import PineconeHybridSearchRetriever
from pinecone import Pinecone
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from pinecone_text.sparse import BM25Encoder

load_dotenv()

pc = Pinecone()
index = pc.Index("government-schemesdb")

bm25_encoder = BM25Encoder().load("bm25_values.json")

embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

retriever = PineconeHybridSearchRetriever(
    embeddings=embedding,
    sparse_encoder=bm25_encoder,
    index=index,
)