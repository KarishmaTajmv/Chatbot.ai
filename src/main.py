# src/main.py
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.agents.query_agent import QueryAgent
from src.agents.summarization_agent import SummarizationAgent
from src.config import GOOGLE_API_KEY

def main():
    # Initialize Agents
    if not GOOGLE_API_KEY:
        raise ValueError("Google API key not found. Set the GOOGLE_API_KEY environment variable.")

    query_agent = QueryAgent(google_api_key=GOOGLE_API_KEY)
    summarization_agent = SummarizationAgent(google_api_key=GOOGLE_API_KEY)

    print("Legal Chatbot Ready! Ask your questions:")

    while True:
        user_query = input("You: ")
        if user_query.lower() == "exit":
            break

        answer = query_agent.generate_answer(user_query)
        print("Bot:", answer)

if __name__ == "__main__":
    main()
