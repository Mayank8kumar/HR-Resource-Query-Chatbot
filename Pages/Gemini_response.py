import os
from dotenv import load_dotenv
import google.generativeai as genai
from Embedding_utils import search_similar_employees

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ✅ Prompt builder
def build_prompt(query, docs):
    doc_text = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an intelligent HR assistant. Based on the following query and employee profiles, suggest the best candidates.

Query: "{query}"

Employee Profiles:
{doc_text}

Your Response:
- List top candidates with short reasoning
- Mention their relevant skills, experience, and availability
- Be concise but informative
"""
    return prompt

# ✅ Call Gemini API to generate response
def generate_response(prompt):
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text

# ✅ Full pipeline: query → vector search → prompt → Gemini → response
def run_pipeline(user_query):
    top_matches = search_similar_employees(user_query, k=3)
    prompt = build_prompt(user_query, top_matches)
    final_response = generate_response(prompt)
    return final_response
