# src/agents/query_agent.py
from langchain.chains import RetrievalQA
import google.generativeai as genai

class QueryAgent:
    def __init__(self, google_api_key=None, model_name="gemini-1.5-pro-latest"): # google_api_key
        genai.configure(api_key=google_api_key) #configure google ai
        self.model = genai.GenerativeModel(model_name) #select model

    def generate_answer(self, query):
        response = self.model.generate_content(query)
        return response.text
