# Empty lists storing recipes and ingredients
recipes_list = []         # List to store recipe dictionaries
ingredients_list = []     # List to store ingredients

# Recipe input from the user
def take_recipe(recipe_number):
    name = input(f"Enter the name of recipe {recipe_number}: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = input("Enter ingredients separated by commas (e.g., Eggs, Salt, Pepper): ").split(", ")
    
    recipe = {"name": name, "cooking_time": cooking_time, "ingredients": ingredients}
    recipes_list.append(recipe)
    ingredients_list.extend(ingredients)  # Extend the ingredients_list with the ingredients
    
    return recipe

# Main section

# Ask the user how many recipes they want to enter
n = int(input("How many recipes would you like to enter? "))

# Loop to take input for each recipe
for i in range(1, n + 1):              # Count the number of recipes entered
    recipe = take_recipe(i)            # Call the function to get a recipe

    # Loop to add unique ingredients to ingredients_list
    for ingredient in recipe["ingredients"]:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)

for recipe in recipes_list:
    # Determine the difficulty level based on cooking time and ingredient count
    if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) < 4:
        recipe["difficulty"] = "Easy"
    elif recipe["cooking_time"] < 10 and len(recipe["ingredients"]) >= 4:
        recipe["difficulty"] = "Medium"
    elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) < 4:
        recipe["difficulty"] = "Intermediate"
    else:
        recipe["difficulty"] = "Hard"

    # Print recipe details
    print("=========================")
    print("Recipe Name: ", recipe["name"])
    print("Cooking Time (minutes): ", recipe["cooking_time"])
    print("Ingredients: ", ", ".join(recipe["ingredients"]))
    print("Difficulty level: ", recipe["difficulty"])

# Function to print all ingredients
def print_ingredients():
    # Remove duplicates by converting the list to a set and then back to a sorted list
    sorted_ingredients = sorted(set(ingredients_list))
    print("=========================")
    print("All ingredients available")
    print("-------------------------")

    # Loop to print each ingredient
    for ingredient in sorted_ingredients:
        print(ingredient)

# Call the print_ingredients function to display all ingredients
print_ingredients()
