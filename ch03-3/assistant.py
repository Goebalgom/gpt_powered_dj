from openai import OpenAI

client = OpenAI()

def send_message(message_log):
    response = client.chat.completions.create(
        model="gpt-4o-2024-11-20",
        messages=message_log,
        temperature=0.5
    )

    for choice in response.choices:
        if "text" in choice:
            return choice.text
        
    return response.choices[0].message.content
