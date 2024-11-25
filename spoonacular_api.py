# spoonacular_api.py
import requests

API_KEY = '66c8aa3e391949179fa0d22af8d3d7ca'  

def recommend_food(ingredients):
    url = f"https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        'ingredients': ingredients,
        'number': 3,  # Number of recommendations
        'apiKey': API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200 and data:
        recommendations = [f"{recipe['title']}" for recipe in data]
        return "\n".join(recommendations)
    else:
        return "No recommendations found. Please try different ingredients."
