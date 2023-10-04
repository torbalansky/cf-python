import pickle

# Function to display a recipe
def display_recipe(recipe):
    print("Recipe Name:", recipe["name"])
    print("Cooking Time (minutes):", recipe["cooking_time"])
    print("Ingredients:", ", ".join(recipe["ingredients"]))
    print("Difficulty:", recipe["difficulty"])
    print() 

# Function to search for an ingredient in the data
def search_ingredient(data):
    # Print all available ingredients 
    print("Available Ingredients:")
    for index, ingredient in enumerate(data["all_ingredients"], 1):
        print(f"{index}. {ingredient}")
    
    try:
        # Prompt user to select an ingredient
        ingredient_index = int(input("Enter the number of the ingredient to search: "))
        
        # Check if the selected index is valid
        if 1 <= ingredient_index <= len(data["all_ingredients"]):
            ingredient_searched = data["all_ingredients"][ingredient_index - 1]
            print(f"Searching for recipes containing '{ingredient_searched}':\n")
            
            # Loop through recipes and display the ones containing the ingredient
            for recipe in data["recipes_list"]:
                if ingredient_searched in recipe["ingredients"]:
                    display_recipe(recipe)
        else:
            print("Invalid input. Please enter a valid ingredient number.")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Main code
filename = input("Enter the filename containing your recipe data: ")

try:
    # Try to open the file for reading using a 'with' statement
    with open(filename, 'rb') as file:
        # Load existing data from the file using pickle
        data = pickle.load(file)
except FileNotFoundError:
    # Handle the case when the file doesn't exist
    print(f"File '{filename}' not found. Please make sure the file exists.")
except Exception as e:
    print(f"An error occurred while opening the file: {e}")
else:
    # Call the search_ingredient function with the loaded data
    search_ingredient(data)
