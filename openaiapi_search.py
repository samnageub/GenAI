import os
from openai import OpenAI

# Retrieve the API key from an environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set the 'OPENAI_API_KEY' environment variable.")

# Create an OpenAI client
client = OpenAI(api_key=api_key)

# Take user input for the question
user_question = input("Enter your question: ")

# Create a chat completion
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "user", "content": user_question}
    ]
)

# Print the response
print("AI Response:", completion.choices[0].message["content"])