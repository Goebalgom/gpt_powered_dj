from ask_to_gpt import ask_to_gpt_4o

developer_request = """
You are the mirror of Snow White. 
You must pretend like the mirror of the story.
"""

users_request = """
거울아! 거울아! 세상에서 누가 제일 예쁘니?
"""

answer = ask_to_gpt_4o(developer_request, users_request, weight=0.1)

print(answer)
