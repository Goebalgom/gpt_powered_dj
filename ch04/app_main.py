import openai
import tkinter as tk
from tkinter import scrolledtext

def send_message(message_log):
    response = openai.chat.completions.create(
        model="gpt-4o-2024-11-20",
        messages=message_log,
        temperature=0.1
    )
    
    for choice in response.choices:
        if "text" in choice:
            return choice.text
    
    return response.choices[0].message.content

def main():
    message_log=[
        {"role": "developer", 
        "content": '''
            You are a DJ assistant who creates playlists. Your user will be Korean,
            so communicate in Korean, but you must not translate artists" names and song titles into Korean.
            - When you show a playlist, it must contains the title, artist, and
            release year of each song in a list format. You must ask the user if they want to save
            the playlist like this: "이 플레이리스트를 CSV로 저장하시겠습니까?"
            - If they want to save the playlist into CS, show the playlist with a header in CS format,
            separated by ';' and the release year format should be 'YVYY'. The CS format must start with a new line.
            The header of the CSV file must be in English and it should be formatted as follows:
            'Title;Artist;Released'.
        '''
        }
    ]

    def show_popup_message(window, message):
        # 팝업 창 생성 및 타이틀
        popup = tk.Toplevel(window)
        popup.title('GPT Powered DJ')

        # 팝업 창 내용
        label = tk.Label(popup, text=message, font=("맑은 고딕", 12))
        label.pack(expand=True, fill=tk.BOTH)

        # 팝업 창 크기 조절
        popup_width = 400
        popup_height = 100
        popup.geometry(f"{popup_width}x{popup_height}")

        # 팝업 창 중앙에 위치시키기
        window_x = window.winfo_x()
        window_y = window.winfo_y()
        window_width = window.winfo_width()
        window_height = window.winfo_height()

        position_x = window_x + window_width // 2 - popup_width // 2
        position_y = window_y + window_height // 2 - popup_height // 2
        popup.geometry(f"+{position_x}+{position_y}")

        popup.transient(window)
        popup.attributes('-topmost', True)
        popup.update()

        return popup

    def on_send():
        user_input = user_entry.get()
        user_entry.delete(0, tk.END)

        if user_input.lower() == "quit":
            window.destroy()
            return
        
        message_log.append({"role": "user", "content": user_input})

        thinking_popup = show_popup_message(window, "생각 중...")
        window.update_idletasks()

        response = send_message(message_log)
        thinking_popup.destroy()
        message_log.append({"role": "assistant", "content": response})

        # 응답 표시
        conversation.config(state=tk.NORMAL)
        conversation.insert(tk.END, f"You: {user_input}\n", "user")
        conversation.insert(tk.END, f"AI Assistant: {response}\n", "assistant")
        conversation.config(state=tk.DISABLED)
        conversation.see(tk.END)

    window = tk.Tk()
    window.title("AI Assistant")

    font=("맑은 고딕", 10)

    conversation = scrolledtext.ScrolledText(window, wrap=tk.WORD, bg='#f0f0f0', font=font)
    conversation.tag_configure("user", background="#c9daf8")
    conversation.tag_configure("assiatance", background="#e4e4e4")
    conversation.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    input_frame = tk.Frame(window)
    input_frame.pack(fill=tk.X, padx=10, pady=10, side=tk.BOTTOM)

    user_entry = tk.Entry(window)
    user_entry.pack(fill=tk.X, side=tk.LEFT, expand=True)

    send_button = tk.Button(input_frame, text="Send", command=on_send, font=font)
    send_button.pack(side=tk.RIGHT)
    window.bind('<Return>', lambda: on_send)

    window.mainloop()

if __name__ == "__main__":
    main()
