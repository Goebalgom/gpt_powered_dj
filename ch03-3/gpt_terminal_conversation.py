from assistant import send_message

def main():
    message_log=[
        {"role": "developer", "content": "You are a helpful assistant."}
    ]

    while True:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        message_log.append({"role": "user", "content": user_input})

        response = send_message(message_log)

        message_log.append({"role": "assistant", "content": response})
        print(f"assistant: {response}")

if __name__ == "__main__":
    main()
