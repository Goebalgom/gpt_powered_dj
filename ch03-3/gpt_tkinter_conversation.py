import tkinter as tk
from os import environ
from dotenv import load_dotenv
from openai import OpenAI
from threading import Thread

load_dotenv()

client = OpenAI(api_key=environ.get('OPENAI_API_KEY'))

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat with Assistant")
        self.root.geometry("600x450")  # 1. 창의 위아래 길이를 1.5배로 길게

        self.message_log = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]

        self.output_text = tk.Text(root, height=10, width=50, state=tk.DISABLED)
        self.output_text.pack(expand=True, fill=tk.BOTH, pady=(10, 5))  # 2. 줄 간격 조절

        self.input_entry = tk.Entry(root, width=50)
        self.input_entry.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, pady=(0, 5))

        self.send_button = tk.Button(root, text="Send", command=self.on_send)
        self.send_button.pack(side=tk.LEFT, pady=(0, 5))

    def on_send(self):
        user_input = self.input_entry.get()
        self.input_entry.delete(0, tk.END)

        if user_input.lower() == "quit":
            self.root.destroy()
        else:
            self.message_log.append({"role": "user", "content": user_input})

            # 팝업 메시지 "생각 중..." 표시
            thinking_popup = tk.Toplevel(self.root)
            thinking_popup.title("Thinking...")
            thinking_popup.geometry("300x200")  # 2. 팝업 크기 3배로 키우기

            # ChatApp 창의 중앙에 위치
            x_position = self.root.winfo_x() + (self.root.winfo_reqwidth() - thinking_popup.winfo_reqwidth()) // 2
            y_position = self.root.winfo_y() + (self.root.winfo_reqheight() - thinking_popup.winfo_reqheight()) // 2
            thinking_popup.geometry(f"+{x_position}+{y_position+100}")

            # Label을 팝업의 가운데에 위치
            label_frame = tk.Frame(thinking_popup)
            label_frame.pack(expand=True, fill=tk.BOTH)
            tk.Label(label_frame, text="생각 중...", padx=20, pady=20).pack(expand=True)

            # 비동기적으로 send_message 호출
            thread = Thread(target=self.send_message_async, args=(user_input, thinking_popup))
            thread.start()

    def send_message_async(self, user_input, thinking_popup):
        response = self.send_message(self.message_log)
        self.message_log.append({"role": "assistant", "content": response})

        # 팝업 메시지 닫기
        thinking_popup.destroy()

        # 응답 표시
        self.output_text.config(state=tk.NORMAL)
        self.output_text.insert(tk.END, f"You: {user_input}\n")
        self.output_text.insert(tk.END, f"Assistant: {response}\n\n")
        self.output_text.config(state=tk.DISABLED)

    def send_message(self, message_log):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=message_log,
            temperature=0.5
        )

        for choice in response.choices:
            if "text" in choice:
                return choice.text

        return response.choices[0].message.content

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
