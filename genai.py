from google import genai
import os
from dotenv import load_dotenv
load_dotenv()

class AiAnswer:
    def __init__(self,data_to_analyze):
        
        self.key = os.environ.get("GEMINI")
        self.data_to_analyze = data_to_analyze
        self.client = genai.Client(api_key=self.key)
    def analyze(self):
        response = self.client.models.generate_content(
            model="gemini-3-flash-preview", contents=f"analyze the following astrology,houses data and"
                                                     f"give a brief explanation of traits a person with this constellation would have"
                                                     f"{self.data_to_analyze}"
        )
        return response.text


