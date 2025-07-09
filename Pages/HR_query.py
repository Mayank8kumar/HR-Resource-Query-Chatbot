import streamlit as st
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
        with st.spinner("Thinking..."):
            response = run_pipeline(user_query)
            st.subheader("📋 Suggested Candidates:")
            st.markdown(response)
