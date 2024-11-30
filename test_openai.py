import openai

openai.api_key = "your_openai_api_key_here"

try:
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a kind and encouraging assistant."},
            {"role": "user", "content": "Generate a positive message for Sera."}
        ],
        max_tokens=150,
        temperature=0.7
    )
    print("API Response:", response["choices"][0]["message"]["content"])
except Exception as e:
    print("Error:", e)
