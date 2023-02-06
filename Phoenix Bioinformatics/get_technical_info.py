import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def info_extracter(article):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Extract important information from this article:\n"+article+"\n",
    temperature=0,
    max_tokens=64,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
    return response["choices"][0]['text']