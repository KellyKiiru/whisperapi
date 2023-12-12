from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


completion = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages= [
        {"role": "system", "content": "You are a technical writer"},
        {"role": "user", "content": "In 200 words or less, list the best technical writing sites in terms of pay"}
    ]
)

print(completion.choices[0].message)