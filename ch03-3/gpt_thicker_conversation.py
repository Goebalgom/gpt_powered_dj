from os import environ
from dotenv import load_dotenv
from openai import OpenAI
import tkinter as tk

load_dotenv()

client = OpenAI(api_key=environ.get('OPENAI_API_KEY'))

def send_message(message_log):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=message_log,
        temperature=0.5
    )

    for choice in response.choices:
        if "text" in choice:
            return choice.text
        
    return response.choices[0].message.content

def main():
    message_log=[
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    root = tk.Tk()
    root.title("Assistant")

    # Create input box
    input_box = tk.Entry(root)
    input_box.pack()

    def send_message_gui():
        user_input = input_box.get()
        message_log.append({"role": "user", "content": user_input})

        if user_input.lower() == "quit":
            root.destroy()
            return

        response = send_message(message_log)

        message_log.append({"role": "assistant", "content": response})
        print(f"assistant: {response}")

        # Add response to GUI
        response_label = tk.Label(root, text=response)
        response_label.pack()

    # Create send button
    send_button = tk.Button(root, text="Send", command=send_message_gui)
    send_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
