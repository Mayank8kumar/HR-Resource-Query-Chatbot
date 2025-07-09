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
You are an intelligent HR assistant. Based on the following query and employee profiles, suggest the best candidates. If something outside the scope of candidate matching is asked, politely respond that you're designed to assist only with talent matching based on provided data.

Query: "{query}"

Employee Profiles:
{doc_text}

Your Response:

--List top candidates with short reasoning
--Mention their relevant skills, experience, and availability
--Be concise but informative
--If no suitable candidates are found, clearly state that and optionally suggest the closest match or recommend expanding the criteria
--If profiles are missing key data (e.g., availability or project names), note it transparently in your reasoning

Example:
User: "I need someone experienced with machine learning for a healthcare project"

Response:
"Based on your requirements for ML expertise in healthcare, I found 2 excellent candidates:

Dr. Sarah Chen would be perfect for this role. She has 6 years of ML experience and specifically worked on the 'Medical Diagnosis Platform' project where she implemented computer vision for X-ray analysis. Her skills include TensorFlow, PyTorch, and medical data processing. She's currently available and has published 3 papers on healthcare AI.

Michael Rodriguez is another strong candidate with 4 years of ML experience. He built the 'Patient Risk Prediction System' using ensemble methods and has experience with HIPAA compliance for healthcare data. He knows scikit-learn, pandas, and has worked with electronic health records.

Both have the technical depth and domain expertise you need. Would you like me to provide more details about their specific healthcare projects or check their availability for meetings?"

If no match found:
"Unfortunately, based on the current profiles, there are no candidates with direct experience in machine learning for healthcare. However, I found [Name], who has general ML experience and may be a fit with some onboarding. Would you like to consider this profile or broaden the search criteria?"

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
