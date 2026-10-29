from fastapi import FastAPI, Path, HTTPException,Query
from generate_answer import get_answer
from agent import agent
from langchain_core.messages import HumanMessage
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://policy-assis.vercel.app"
    ],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "ok"}

@app.get('/response')
def get_response(query: str =Query(..., min_length=2, max_length=900)) ->str:
    try:
        answer = agent.invoke({
            'messages':[
                HumanMessage(query)
            ]
        })
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Something went wrong. Please try again.")

    return answer["messages"][-1].content