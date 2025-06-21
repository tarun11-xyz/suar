from openai import OpenAI

client = OpenAI(
    api_key="API_KEY",
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system","content": "You are a helpful assistant named Suar."},
        {"role": "user","content": "Hello, what is coding?"}
    ]
)
print(completion.choices[0].message)