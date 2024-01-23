import tkinter as tk
from os import environ
from dotenv import load_dotenv
from openai import OpenAI

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

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat with Assistant")

        self.message_log = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]

        self.output_text = tk.Text(root, height=10, width=50, state=tk.DISABLED)
        self.output_text.pack(pady=10)

        self.input_entry = tk.Entry(root, width=50)
        self.input_entry.pack(pady=10)

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack()

    def send_message(self):
        user_input = self.input_entry.get()
        self.input_entry.delete(0, tk.END)

        if user_input.lower() == "quit":
            self.root.destroy()
        else:
            self.message_log.append({"role": "user", "content": user_input})
            response = send_message(self.message_log)
            self.message_log.append({"role": "assistant", "content": response})

            self.output_text.config(state=tk.NORMAL)
            self.output_text.insert(tk.END, f"You: {user_input}\n")
            self.output_text.insert(tk.END, f"Assistant: {response}\n\n")
            self.output_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
