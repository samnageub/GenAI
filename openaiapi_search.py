from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from openai import OpenAI

# Azure Key Vault details
KEY_VAULT_NAME = "kv-weatherstreamingapp"  # Replace with your Azure Key Vault name
SECRET_NAME = "openaisecret"  # Replace with the name of the secret storing your API key
KV_URI = f"https://{KEY_VAULT_NAME}.vault.azure.net/"

# Authenticate with Azure Key Vault
credential = DefaultAzureCredential()
client = SecretClient(vault_url=KV_URI, credential=credential)

# Retrieve the API key from Azure Key Vault
retrieved_secret = client.get_secret(SECRET_NAME)
api_key = retrieved_secret.value

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
