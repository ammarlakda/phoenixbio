import os
import openai
from dotenv import load_dotenv

load_dotenv()

#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"


def summarizer(article):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Summarize this: "+article+"\n",
    temperature=0.7,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=1
    )
    return response["choices"][0]['text']