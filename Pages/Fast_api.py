from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from Embedding_utils import load_employees
from Gemini_response import run_pipeline

app = FastAPI(title="HR Chatbot API", description="RAG-powered HR query backend")

# Request schema for chat
class ChatRequest(BaseModel):
    query: str

# Response schema
class ChatResponse(BaseModel):
    response: str

# Search endpoint query params
@app.get("/employees/search", summary="Search employees by skill, experience, availability")
def search_employees(
    skill: Optional[str] = None,
    min_experience: Optional[int] = None,
    available: Optional[bool] = None
):
    employees = load_employees()

    # Apply filters
    if skill:
        employees = [e for e in employees if skill in e["skills"]]
    if min_experience is not None:
        employees = [e for e in employees if e["experience_years"] >= min_experience]
    if available is not None:
        avail_value = "available" if available else "not available"
        employees = [e for e in employees if e["availability"] == avail_value]

    return employees

# POST /chat endpoint
@app.post("/chat", response_model=ChatResponse, summary="Ask HR chatbot a query")
def chat_endpoint(payload: ChatRequest):
    try:
        print(type(payload.query),payload.query)
        response = run_pipeline(payload.query)
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
