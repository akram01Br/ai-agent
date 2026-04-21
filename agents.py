from openai import OpenAI
from config import API_KEY, MODEL, BASE_URL

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)


def ask(system, user):
    return client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user}
        ]
    ).choices[0].message.content


def research_agent(data):
    return ask("You are a research expert. Extract key points.", data)


def writer_agent(data):
    return ask("You are a professional writer. Write a clear article.", data)


def reviewer_agent(text):
    return ask("You are an editor. Improve clarity and simplicity.", text)