import os 
import json
from langchain.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings


DATA_PATH = "data/employees.json"


# Load the data 
def load_employees():
    with open(DATA_PATH, "r") as f:
        data = json.load(f)
    return data["employees"]


def prepare_employee_text(emp):
    return f"""
    Name: {emp['name']}
    Skills: {', '.join(emp['skills'])}
    Experience: {emp['experience_years']} years
    Projects: {', '.join(emp['projects'])}
    Availability: {emp['availability']}
    """

# Generate and store embeddings
def generate_embeddings():
    employees = load_employees()
    employee_texts = [prepare_employee_text(emp) for emp in employees]

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(employee_texts, embedding=embeddings)

    vector_store.save_local("faiss_vector_embeddings")
    # print("Embedding index created and saved locally.")


# Search employees based on user query
def search_similar_employees(query, k=3):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.load_local("faiss_vector_embeddings", embeddings, allow_dangerous_deserialization=True)

    results = vector_store.similarity_search(query, k=k)
    return results