import streamlit as st
import requests
from Gemini_response import run_pipeline

st.set_page_config(page_title="HR Query Chatbot", page_icon="🤖")
st.title("🤖 HR Resource Chatbot")
st.markdown("Ask about employees by skill, project, availability, etc.")

# Text input for the query
user_query = st.text_input("🔍 Enter your query:")

# When the user clicks the button
if st.button("Search Candidates"):
    if user_query.strip() == "":
        st.warning("Please enter a query.")
    else:
        with st.spinner("Talking to Gemini..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/chat",
                    json={"query": user_query}
                )
                if response.status_code == 200:
                    st.subheader("💬 Gemini Suggestion")
                    st.markdown(response.json()["response"])
                else:
                    st.error(f"Error {response.status_code}: {response.json()['detail']}")
            except Exception as e:
                st.error(f"API Call Failed: {e}")

