import streamlit as st
import sys
import  os
sys.path.append(os.path.join(os.path.dirname(__file__), "agents"))  
from agents.query_agent import QueryAgent
from agents.summarization_agent import SummarizationAgent
sys.path.append(os.path.join(os.path.dirname(__file__), "config"))
from config import GOOGLE_API_KEY

# Initialize the QueryAgent
query_agent = QueryAgent(google_api_key=GOOGLE_API_KEY)

# Streamlit app title
st.title("Legal Chatbot")

# Input text box for user query
user_query = st.text_input("Ask your legal question:")

# Button to submit the query
if st.button("Submit"):
    if not user_query:
        st.error("Please enter a query.")
    else:
        # Generate the answer using the QueryAgent
        answer = query_agent.generate_answer(user_query)
        st.write("Bot:", answer)
'''
def main():
    if not GOOGLE_API_KEY:
        raise ValueError("Google API key not found. Set the GOOGLE_API_KEY environment variable.")
    
    print("Legal Chatbot Ready! Ask your questions:")
    while True:
        user_query = input("You: ")
        if user_query.lower() == "exit":
            break

        query_agent = QueryAgent(google_api_key=GOOGLE_API_KEY)
        answer = query_agent.generate_answer(user_query)
        print("Bot:", answer)

if __name__ == "__main__":
    main()'''
