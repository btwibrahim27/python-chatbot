import tkinter as tk

def get_response(user_input):
    user_input = user_input.lower()
    
    responses = {
        "hi": "Hello! How can I help you?",
        "hello": "Hi there! What can I do for you?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a great day!",
        "your name": "I'm a chatbot created in Python!",
    }
    
    for key in responses:
        if key in user_input:
            return responses[key]
    
    return "I'm not sure how to respond to that."

def send_message():
    user_input = user_entry.get()
    if user_input.strip():
        chat_history.insert(tk.END, "You: " + user_input + "\n", "user")
        user_entry.delete(0, tk.END)
        
        bot_response = get_response(user_input)
        chat_history.insert(tk.END, "Bot: " + bot_response + "\n", "bot")
        chat_history.see(tk.END)

# GUI Setup
root = tk.Tk()
root.title("Chatbot")
root.geometry("500x500")

chat_history = tk.Text(root, wrap=tk.WORD, font=("Arial", 12))
chat_history.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
chat_history.tag_config("user", foreground="blue")
chat_history.tag_config("bot", foreground="green")

user_entry = tk.Entry(root, font=("Arial", 12))
user_entry.pack(pady=5, padx=10, fill=tk.X)

send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 12))
send_button.pack(pady=5)

root.mainloop()
