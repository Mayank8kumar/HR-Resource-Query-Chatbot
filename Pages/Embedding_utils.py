import json
import os
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(BASE_DIR, "./../data/employees.json")
OUTPUT_PATH = os.path.join(BASE_DIR, "../faiss_vector_embeddings")


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

    vector_store.save_local(OUTPUT_PATH)
    # print("Embedding index created and saved locally.")


# Search employees based on user query
def search_similar_employees(query, k=3):
    generate_embeddings()
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.load_local(OUTPUT_PATH, embeddings, allow_dangerous_deserialization=True)

    results = vector_store.similarity_search(query, k=k)
    return results