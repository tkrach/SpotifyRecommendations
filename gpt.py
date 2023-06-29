import openai
import config

openai.api_key = config.api_key

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible.\nKnowledge cutoff: 2021-09-01\nCurrent date: 2023-03-02"},
        {"role": "user", "content": "How are you?"},
        {"role": "assistant", "content": "I am doing well"},
        {"role": "user", "content": "What is the mission of the company OpenAI?"}
    ]
)

assistant_message = completion.choices[0].message['content']
print("Assistant's response:", assistant_message)
