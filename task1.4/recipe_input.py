import pickle

# Initialize empty lists
recipes_list = []        
ingredients_list = []    

# Function to input a recipe from the user
def take_recipe(recipe_number):
    name = input(f"Enter the name of recipe {recipe_number}: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = input("Enter ingredients separated by commas (e.g., Eggs, Salt, Pepper): ").split(", ")
    
    recipe = {"name": name, "cooking_time": cooking_time, "ingredients": ingredients}
    recipes_list.append(recipe)
    
    # Add ingredients to the ingredients list, avoiding duplicates
    for ingredient in ingredients:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    
    return recipe

# Function to calculate the difficulty of a recipe
def calculate_difficulty(recipe):
    if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) < 4:
        recipe["difficulty"] = "Easy"
    elif recipe["cooking_time"] < 10 and len(recipe["ingredients"]) >= 4:
        recipe["difficulty"] = "Medium"
    elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) < 4:
        recipe["difficulty"] = "Intermediate"
    else:
        recipe["difficulty"] = "Hard"

    return recipe

# Main code
filename = input("Enter the filename to save your recipe data: ")

try:
    # Try to open the file for reading
    with open(filename, 'rb') as file:
        # Load existing data from the file using pickle
        data = pickle.load(file)
        recipes_list = data.get("recipes_list", [])            
        ingredients_list = data.get("all_ingredients", [])      

except FileNotFoundError:
    # Handle the case when the file doesn't exist
    print(f"File '{filename}' not found. Initializing new data.")
    data = {"recipes_list": recipes_list, "all_ingredients": ingredients_list}

# Extract values from the dictionary
recipes_list = data["recipes_list"]
ingredients_list = data["all_ingredients"]

# Ask the user how many recipes they want to enter
num_recipes = int(input("How many recipes would you like to enter? "))

# Loop to take recipes from the user
for i in range(1, num_recipes + 1):
    recipe = take_recipe(i)
    # Calculate difficulty for the current recipe
    calculate_difficulty(recipe)  

# Update the data dictionary with the new lists
data["recipes_list"] = recipes_list
data["all_ingredients"] = ingredients_list

# Open the file and write the updated data using pickle
with open(filename, 'wb') as file:
    pickle.dump(data, file)

print(f"Recipe data saved to '{filename}'.")
