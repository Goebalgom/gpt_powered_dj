from ask_to_gpt import ask_to_gpt_4o

developer_request = "You are a helpful assistant."

users_request = "최근 가장 인기 있는 프로그래밍 언어를 비교해 줘."

answer = ask_to_gpt_4o(developer_request, users_request, weight=0.1)

print(answer)
