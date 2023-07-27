import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me an essay about Penguins"}])
print(completion.choices[0].message.content)