import requests

# Create a function to search recipes
def search_recipes(ingredient, meal_of_the_day, cuisine_type):
    # Register to get an APP ID and KEY
    app_id = '5996ea62'
    app_key = 'c7763bf09a34803ce73ec09c145f587b'

    url = 'https://api.edamam.com/search'
    params = {
        'q': ingredient,
        'app_id': app_id,
        'app_key': app_key,
        'mealType': meal_of_the_day,
        'cuisineType': cuisine_type
    }

    result = requests.get(url, params=params)

    if result.status_code == 200:
        data = result.json()
        return data['hits']
    else:
        print(f"Error: {result.status_code}")
        return []

def run():
    type_of_meal = ["Breakfast", "Brunch", "Lunch", "Dinner", "Snack"]
    cuisine_type_list = ["American", "Asian", "British", "Chinese", "French", "Italian", "Japanese"]

    meal_of_the_day = input('Which meal type do you want? \n {}: '.format(type_of_meal))
    while meal_of_the_day.capitalize() not in [meal.capitalize() for meal in type_of_meal]:
        meal_of_the_day = input(
            "Unknown meal type. Please choose from one of the listed meal types: \n {}: ".format(type_of_meal))

    cuisine = input('Which cuisine are you seeking after? \n {}: '.format(cuisine_type_list))
    while cuisine.capitalize() not in [cuisine.capitalize() for cuisine in cuisine_type_list]:
        cuisine = input("Unknown cuisine. Please choose from one of the listed cuisines: \n {}: ".format(cuisine_type_list))

    # Normalize inputs to match the required format for the API
    meal_of_the_day = meal_of_the_day.capitalize()
    cuisine = cuisine.capitalize()

    ingredient = input('Enter an ingredient: ')
    results = search_recipes(ingredient, meal_of_the_day, cuisine)

    # Display the recipes for the search result
    if results:
        for result in results:
            recipe = result['recipe']
            print(f"Recipe: {recipe['label']}")
            print(f"Source: {recipe['source']}")
            print(f"URL:    {recipe['url']}")
            print('---')
    else:
        print(f"No recipes found for {ingredient}")

run()
