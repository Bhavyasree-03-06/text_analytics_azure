# 4. Use AzureOpenAI client
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version="2024-12-01-preview"  # Use a recent stable API version
)

# 5. Call the model (model parameter uses deployment name)
response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "you are a key phrase extraction assistant.Extract 3-5 phrases"},
        {"role": "user", "content": "Azure AI foundry provides a unified platform for developers to build ,evaluate"}
    ]
)

print(response.choices[0].message.content)
