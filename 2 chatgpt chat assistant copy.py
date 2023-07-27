import openai

openai.api_key = "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"

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")

    
    
    #Agradecimientos a Greg Baugues por el codigo! :D