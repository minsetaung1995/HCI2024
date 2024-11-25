import tkinter as tk
from tkinter import scrolledtext
from speech_to_text import transcribe_speech
import re

class FoodRecommendationChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Food Recommendation Chatbot")
        self.root.geometry("500x500")

        # State to manage the conversation flow
        self.current_stage = "initial"  

        # Conversation area
        self.conversation_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled')
        self.conversation_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Speak button
        self.speak_button = tk.Button(root, text="Speak", command=self.handle_speech_input)
        self.speak_button.pack(pady=10)

        # Food categories and options for specific food types
        self.food_categories = {
            "burger": ["Cheeseburger", "Chicken Burger", "Veggie Burger", "Bacon Burger", "Double Burger"],
            "pizza": ["Margherita Pizza", "Pepperoni Pizza", "Vegetarian Pizza", "Hawaiian Pizza", "BBQ Chicken Pizza"],
            "salad": ["Caesar Salad", "Greek Salad", "Fruit Salad", "Tuna Salad", "Chicken Salad"],
            "dessert": ["Chocolate Cake", "Ice Cream", "Brownie", "Cheesecake", "Pie"]
        }

        # Drink options
        self.drink_options = ["Soda", "Juice", "Water", "Tea", "Coffee", "Milkshake", "Smoothie"]

    def handle_speech_input(self):
        self.conversation_area.config(state='normal')
        # Get speech input from user
        user_text = transcribe_speech()
        if user_text:
            self.conversation_area.insert(tk.END, f"You: {user_text}\n")
            # Determine response based on current conversation stage
            response = self.get_food_recommendation(user_text)
            self.conversation_area.insert(tk.END, f"Bot: {response}\n")

        # Scroll to end of conversation and disable editing
        self.conversation_area.yview(tk.END)
        self.conversation_area.config(state='disabled')

    def get_food_recommendation(self, user_text):
        # Define the conversation flow for food recommendations
        responses = {
            "initial": (
                "What kind of food are you in the mood for? For example, burger, pizza, salad, or dessert."
            ),
            "ask_drink": "Would you like a drink? You can choose from soda, juice, water, tea, coffee, milkshake, or smoothie.",
            "ask_more": "Would you like something else? (Yes/No)",
            "final_response": "Enjoy your meal! If you need anything else, feel free to ask!"
        }

        if self.current_stage == "initial":
            # If the user says "I'm hungry", directly ask what they want to eat
            if "hungry" in user_text.lower():
                return responses["initial"]

            # Check if the user mentioned a valid food category
            category = self.extract_food_category(user_text)
            if category in self.food_categories:
                self.current_stage = "ask_drink"  # Transition to drink asking stage
                return f"How about trying one of these {category} options: " + ", ".join(self.food_categories[category]) + ". {responses['ask_drink']}"
            else:
                # If the bot doesn't recognize the food category, just ask them for food
                return responses["initial"]

        elif self.current_stage == "ask_drink":
            # If the user responds with a drink choice
            drink_choice = self.extract_drink_choice(user_text)
            if drink_choice:
                self.current_stage = "ask_more"
                return f"Great choice! Would you like something else? {responses['ask_more']}"

            # If the user says "no" (they don't want a drink)
            elif "no" in user_text.lower():
                self.current_stage = "ask_more"
                return f"No drink chosen. Would you like something else? {responses['ask_more']}"
            else:
                # If no valid drink choice or "no" detected, keep asking for a drink
                return responses["ask_drink"]

        elif self.current_stage == "ask_more":
            # If the user says "yes," we continue; if "no," we finalize the recommendation
            if "yes" in user_text.lower():
                self.current_stage = "initial"
                return responses["final_response"]
            elif "no" in user_text.lower():
                self.current_stage = "initial"
                return responses["final_response"]
            else:
                return responses["final_response"]

    def extract_food_category(self, user_text):
        """Extract the food category based on user input."""
        user_text = user_text.lower()
        if "burger" in user_text:
            return "burger"
        elif "pizza" in user_text:
            return "pizza"
        elif "salad" in user_text:
            return "salad"
        elif "dessert" in user_text:
            return "dessert"
        else:
            return ""

    def extract_drink_choice(self, user_text):
        """Check if the user mentioned a valid drink choice."""
        user_text = user_text.lower()
        for drink in self.drink_options:
            if drink.lower() in user_text:
                return drink
        return None

# Run the chatbot UI
if __name__ == "__main__":
    root = tk.Tk()
    app = FoodRecommendationChatbot(root)
    root.mainloop()
