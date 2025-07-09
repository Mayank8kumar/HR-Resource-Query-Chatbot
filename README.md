# HR Resource Query Chatbot

A smart HR assistant that helps recruiters quickly find the most relevant employees based on skillset, experience, and availability. It uses Gemini 2.5 Flash for language understanding and FAISS-based vector search for profile matching.

## Overview

This application is built using:

* Streamlit for the frontend
* FastAPI for the backend API
* Google Gemini API for response generation
* LangChain + FAISS for semantic employee search

Recruiters can ask natural-language queries like:

"Who has React Native experience and has worked on mobile apps?"

The system returns top-matched employees with reasoning.

## Features

* Semantic employee search using FAISS + embeddings
* Gemini-powered reasoning and response generation
* REST API using FastAPI (/chat, /employees/search)
* Streamlit interface to input queries and display results
* JSON-based employee database
* Built-in validation and error handling

## Architecture

```
HR_CHATBOT/
|
├── data/
│   └── employees.json              # Sample employee dataset (20 profiles)
|
├── faiss_vector_embeddings/       # FAISS index folder (created at runtime)
|
├── Pages/                         # All logic modules
│   ├── __init__.py
│   ├── Embedding_utils.py         # Embedding generation + semantic search
│   ├── Gemini_response.py         # Prompt building + Gemini API logic
│   ├── Fast_api.py                # FastAPI backend for /chat & /search
│   └── HR_query.py                # Streamlit frontend
|
├── .env                           # Gemini API Key (not shared)
├── requirements.txt               # Project dependencies
└── README.md                      # This file
```

## Setup & Installation

### 1. Clone the project

```bash
git clone https://github.com/yourname/hr-chatbot.git
cd hr-chatbot
```

### 2. Setup virtual environment

```bash
python -m venv env
env\Scripts\activate
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

### 4. Add your Gemini API key to .env

```
GOOGLE_API_KEY=your_gemini_api_key
```

## Running the App

### Step 1: Navigate into Pages directory

```bash
cd Pages
```

### Step 2: Start the FastAPI backend

```bash
uvicorn Fast_api:app --reload
```

* Test at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Step 3: In a separate terminal, run the Streamlit frontend

```bash
cd Pages
streamlit run HR_query.py
```

* UI opens at: [http://localhost:8501](http://localhost:8501)

## API Documentation

### POST /chat

* Input:

```json
{
  "query": "Suggest people with React Native experience"
}
```

* Output:

```json
{
  "response": "Here are the top candidates..."
}
```

### GET /employees/search

Query parameters:

* skill: e.g., Python
* min\_experience: e.g., 3
* available: true or false

Example:

```
/employees/search?skill=React%20Native&min_experience=2&available=true
```

## AI Development Process

### AI Tools Used

* ChatGPT: Architecture planning, prompt design, error debugging
* LangChain + Gemini: For embedding + language understanding

### How AI Helped in different phases

* Code generation (40%)
* Prompt refinement for Gemini
* Employee dataset creation
* Structuring the modular backend-frontend system

### Manual Work

* Error debugging
* UI design (Streamlit)
* API integration logic
* Debugging FastAPI path, embedding deserialization, and runtime config

### When AI Fell Short

* FAISS deserialization error needed manual fix (allow\_dangerous\_deserialization=True)
* Import path issues and module naming with Pages/ structure had to be debugged step-by-step
* FastAPI path debugging and runtime config

## Technical Decisions

| Decision             | Reason                                          |
| -------------------- | ----------------------------------------------- |
| Google Gemini API    | Free-tier, fast responses, accurate instruction |
| FAISS + LangChain    | Lightweight semantic search engine              |
| Streamlit            | Rapid UI prototyping                            |
| FastAPI              | Modern backend with Swagger, async-ready        |
| JSON for employee DB | Simple, human-readable, no DB needed            |

## Future Improvements

* Pagination and filtering on frontend
* Upload new employee profiles
* Add memory-based chat
* Integrate calendar for scheduling interviews
* Authentication for recruiters

## Demo

* [https://drive.google.com/file/d/17\_vZXdreh45shOQ02tpD6aIQvGuV3rUg/view?usp=sharing](https://drive.google.com/file/d/17_vZXdreh45shOQ02tpD6aIQvGuV3rUg/view?usp=sharing)
* [https://drive.google.com/file/d/1VbBk-SdSFX1vxtIKUBANfrNmZeuaKCA0/view?usp=drive\_link](https://drive.google.com/file/d/1VbBk-SdSFX1vxtIKUBANfrNmZeuaKCA0/view?usp=drive_link)

Feel free to use or contribute to this project.
