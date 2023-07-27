import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are Big Boss from metal gear solid series"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Tactical Espionage Pro")

demo.launch(share=True)