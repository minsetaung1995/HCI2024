# scripts/recommend_food.py
import json
import random

def load_data(business_file, reviews_file):
    """Load food recommendation data from JSON files."""
    with open(business_file, 'r') as f:
        businesses = json.load(f)
    
    with open(reviews_file, 'r') as f:
        reviews = json.load(f)
    
    return businesses, reviews

def recommend_food(user_input, businesses, reviews):
    """Recommend food based on user input."""
    # Filter businesses based on user input
    matching_businesses = [biz for biz in businesses if user_input.lower() in biz['name'].lower()]

    if matching_businesses:
        selected_business = random.choice(matching_businesses)
        return f"How about trying {selected_business['name']}? It's rated {selected_business['rating']} stars."
    else:
        return "No recommendations found for that input."
