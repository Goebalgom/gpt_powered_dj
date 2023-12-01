from os import environ
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=environ.get('OPENAI_API_KEY'))

def ask_to_gpt_35_turbo(user_input):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        top_p=0.1,
        temperature=0.1,
        messages=[
            {
                "role": "system", 
                "content": "You are the mirror of Snow White. " + 
                    "You must pretend like the mirror of the story."
            },
            {
                "role": "user", 
                "content": user_input
            }
        ]
    )

    return completion.choices[0].message.content

users_request = """
거울아! 거울아! 세상에서 누가 제일 예쁘니?
"""

answer = ask_to_gpt_35_turbo(users_request)
print(answer)
