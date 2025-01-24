from openai import OpenAI

client = OpenAI()

def ask_to_gpt_4o(developer_request, user_input, weight=0.5):
    completion = client.chat.completions.create(
        model="gpt-4o-2024-11-20",
        top_p=weight,
        temperature=weight,
        messages=[
            {"role": "system", "content": developer_request},
            {"role": "user", "content": user_input}
        ]
    )

    return completion.choices[0].message.content
