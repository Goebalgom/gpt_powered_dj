from os import environ
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=environ.get('OPENAI_API_KEY'))

def ask_to_gpt_35_turbo(user_input):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        top_p=0.5,
        temperature=0.5,
        messages=[
            {
                "role": "system", 
                "content": "You are the Joker of Batman comics. " + 
                    "You must pretend like Joker of the story. " +
                    "When you speak in korean, you must use in 반말."
            },
            {
                "role": "user", 
                "content": user_input
            }
        ]
    )

    return completion.choices[0].message.content

users_request = "I'm the Batman"

answer = ask_to_gpt_35_turbo(users_request)
print(answer)
