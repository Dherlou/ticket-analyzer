import yaml
from openai import OpenAI
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class LLM:
    def __init__(self):
        with open("settings.yml", "r") as file:
           meta_data = yaml.safe_load(file)
           self.api_key = meta_data['api_key']
           self.base_url = meta_data['base_url']
           self.model_name = meta_data['model']

           # Start OpenAI client
           self.client = OpenAI(
               api_key=self.api_key,
               base_url=self.base_url
           )

        with open("systemprompt.txt", 'r') as prompt:
            self.prompt = prompt.read()

    def analyze_ticket(self, ticket):
        chat_completion = self.client.chat.completions.create(
            messages = [
                        {"role":"system",
                                 "content": self.prompt},
                         {"role":"user",
                                 "content": ticket}
                        ],
            model = self.model_name,
        )

        return chat_completion