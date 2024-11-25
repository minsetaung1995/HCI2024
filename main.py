# app.py
from chatbot_ui import FoodRecommendationChatbot

if __name__ == "__main__":
    import tkinter as tk
    root = tk.Tk()
    chatbot = FoodRecommendationChatbot(root)
    root.mainloop()
