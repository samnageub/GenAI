
# Import the OpenAI class from the openai module
from openai import OpenAI
# Create a client
#https://platform.openai.com/welcome?step=try
client = OpenAI(
  api_key="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"
)
# Create a chat completion
completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "What is 2 + 7?"}
  ]
)
# Print the response
print(completion.choices[0].message);