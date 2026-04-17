import os
from dotenv import load_dotenv
import requests

load_dotenv()

class Astro:
    def __init__(self,params):

        self.url = os.environ.get("URL")
        self.api_key = os.environ.get("KEY")

        API_KEY = os.environ.get("KEY")
        self.header = {
            "noobcoder_learning": "application/PythonProject13",
            "x-api-key": API_KEY,
        }
        self.params = params
    def make_call(self):
        try:
            response = requests.post(self.url, headers=self.header, json=self.params, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return {"error": "API request failed"}




