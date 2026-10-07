from langchain_openai import ChatOpenAI

import os
from dotenv import load_dotenv

class OpenAILLM:
    def __init__(self):
        load_dotenv()  # Load environment variables from .env file

    def get_llm(self):
        try:
            self.api_key = os.getenv("OPENAI_API_KEY")
            os.environ["OPENAI_API_KEY"] = self.api_key
            llm = ChatOpenAI(api_key=self.api_key, model_name="gpt-4o", temperature=0.0)
            return llm
        except Exception as e:
            raise ValueError(f"Error initializing OpenAI LLM: {e}")
        