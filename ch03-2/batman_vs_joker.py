from ask_to_gpt import ask_to_gpt_4o

developer_request = """
You are the Joker of Batman comics. 
You must pretend like Joker of the story. 
When you speak in korean, you must use in 반말.
"""

users_request = "I'm the Batman"

answer = ask_to_gpt_4o(developer_request, users_request)

print(answer)
