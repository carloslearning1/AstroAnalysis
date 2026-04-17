import os
from dotenv import load_dotenv
import requests

load_dotenv()

class Astro:
    def __init__(self,params):

        self.url = os.environ.get("URL")
        API_KEY = os.environ.get("KEY")
        self.header = {
            "learning": "application/PythonProjectX",
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




