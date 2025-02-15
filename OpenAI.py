import openai

# Set your OpenAI API key
api_key = "your-key"

# Initialize OpenAI API client
client = OpenAI(api_key=api_key)

# Request completion
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "write a haiku about AI"}
    ]
)

# Print the completion result
print(completion.choices[0].message.content.strip())