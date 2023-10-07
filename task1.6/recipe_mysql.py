# Imports MySQL connector
import mysql.connector

# Initializes connection to the MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="cf-python",
    passwd="password"
)

# Initializes the cursor object from the connection
cursor = conn.cursor()

# Creates the database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

# Connects to the database using the USE statement
cursor.execute("USE task_database")

# Creates the Recipes table with specified columns
cursor.execute("CREATE TABLE IF NOT EXISTS Recipes ("
               "id INT AUTO_INCREMENT PRIMARY KEY,"
               "name VARCHAR(50),"
               "ingredients VARCHAR(255),"
               "cooking_time INT,"
               "difficulty VARCHAR(20)"
               ")")

def main_menu(conn, cursor):
    while True:
        # Displays the main menu options to the user
        print("\n==========================================")
        print("Main Menu")
        print("1. Create a new recipe")
        print("2. Search for recipes by ingredients")
        print("3. Update an existing recipe")
        print("4. Delete a recipe")
        print("5. Display available recipes")
        print("6. Quit")
        print("===========================================\n")

        # Prompts the user for their choice
        choice = input("Enter your choice: ")

        # Checks the user's choice and performs the corresponding action
        if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)
        elif choice == "5":
            display_recipes(cursor)
        elif choice == "6":
            # If the user selects option 6 (Quit), commit any changes, close the connection, and exit the program
            conn.commit()
            conn.close()
            exit()
        else:
            # Displays an error message for an invalid choice
            print("Invalid choice. Please enter a valid option 1-6.")

#Function to calculare recipe difficulty
def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
            return "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        return "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        return "Intermediate"
    else:
        return "Hard"

def create_recipe(conn, cursor):
    # Recipe details
    name = input("Enter the name of the recipe:")
    cooking_time = int(input("Enter the cooking time in minutes:"))
    ingredients = input("Enter the ingredients (comma-separated): ") .split(", ")
 
    # Calculates difficulty
    difficulty = calculate_difficulty(cooking_time, ingredients)

    # Converts ingredients list to a comma-separated str
    ingredients_str = ", ".join(ingredients)

    # Builds the SQL query
    query = "INSERT INTO Recipes (name, cooking_time, ingredients, difficulty) VALUES (%s, %s, %s, %s)"
      
    # Executes the query
    cursor.execute(query, (name, cooking_time, ingredients_str, difficulty))

    # Commits the changes to the DB
    conn.commit()

    print(f"Recipe '{name}' added successfully")

def search_recipe(cursor):
    # Retrieves a list of all unique ingredients from the Recipes table
    cursor.execute("SELECT DISTINCT ingredients FROM Recipes")
    results = cursor.fetchall()
    all_ingredients = []

    # Extracts unique ingredients
    for row in results:
        ingredients_str = row[0]
        ingredients_list = ingredients_str.split(", ")

        # Adds unique ingredients to the ingredient list
        for ingredient in ingredients_list:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)

    # Displays all ingredients to the user
    print("Available ingredients:")
    for index, ingredient in enumerate(all_ingredients, start=1):
        print(str(index) + ". " + ingredient)

    # Prompt the user to select an ingredient to search for
    try:
        choice = int(input("Enter the number of the ingredient to search for: "))

        if 1 <= choice <= len(all_ingredients):
            search_ingredient = all_ingredients[choice - 1]
            
            # Build the SQL query for searching recipes containing the chosen ingredient
            query = "SELECT name FROM Recipes WHERE ingredients LIKE '%" + search_ingredient + "%'"
            cursor.execute(query)

            # Fetches and displays the results
            search_results = cursor.fetchall()

            if search_results:
                print("Recipes containing '" + search_ingredient + "':")
                for row in search_results:
                    print(row[0])
            
            else:
                print("No recipes found containing '" + search_ingredient + "':")
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def update_recipe(conn, cursor):
    # Fetches and displays all the recipes to the user
    cursor.execute("SELECT id, name, cooking_time, ingredients FROM Recipes")
    recipes = cursor.fetchall()

    print("Recipes available for update:")
    for recipe in recipes:
        print(f"{recipe[0]}. {recipe[1]}")

    # Prompts the user to select a recipe
    try:
        recipe_id = int(input("Enter the ID of the recipe to update: "))
    except ValueError:
        print("Invalid input. Please enter a valid recipe ID.")
        return

    # Find the selected recipe in the list of recipes
    selected_recipe = None
    for recipe in recipes:
        if recipe[0] == recipe_id:
            selected_recipe = recipe
            break

    if selected_recipe is None:
        print("Recipe not found.")
        return

    name, _, cooking_time, ingredients_str = selected_recipe

    # Prompts the user to select the column to update
    print("Columns available for update:")
    print("1. Name")
    print("2. Cooking time")
    print("3. Ingredients")

    try:
        column_choice = int(input("Enter the number of the column to update: "))
    except ValueError:
        print("Invalid input. Please enter a valid column number.")
        return

    # Prompts the user for a new value
    new_value = input("Enter the new value: ")

    if column_choice == 1:
        # Update the name column
        update_query = f"UPDATE Recipes SET name = '{new_value}' WHERE id = {recipe_id}"
    elif column_choice == 2:
        # Update the cooking_time column
        try:
            new_cooking_time = int(new_value)
            new_difficulty = calculate_difficulty(new_cooking_time, ingredients_str.split(", "))
            update_query = f"UPDATE Recipes SET cooking_time = {new_cooking_time}, difficulty = '{new_difficulty}' WHERE id = {recipe_id}"
        except ValueError:
            print("Invalid input for cooking time. Please enter a valid number.")
            return
    elif column_choice == 3:
        # Update the ingredients column
        # Here, you may also want to split the input by commas and format it as needed
        new_ingredients = new_value
        new_difficulty = calculate_difficulty(cooking_time, new_ingredients.split(", "))
        update_query = f"UPDATE Recipes SET ingredients = '{new_ingredients}', difficulty = '{new_difficulty}' WHERE id = {recipe_id}"
    else:
        print("Invalid column choice. No updates were introduced.")
        return

    try:
        # Executes the update query
        cursor.execute(update_query)
        # Commits the changes to the DB
        conn.commit()
        print("Recipe with ID " + str(recipe_id) + " updated successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def delete_recipe(conn, cursor):
    #Fetches and Displays all recipes to the user
    cursor.execute("SELECT id, name FROM Recipes")
    recipes = cursor.fetchall()

    print("Recipes available to delete")
    for recipe in recipes:
        print(f"{recipe[0]}. {recipe[1]}")

    # Prompts the user to select a recipe by ID for deletion
    try:
        recipe_id = int(input("Enter the ID of the recipe to be deleted: "))
    except ValueError:
        print("Invalid input. Please enter a valid recipe ID.")
        return
    
    # Builds the SQL query for deleting the selected recipe
    delete_query = f"DELETE FROM Recipes WHERE id = {recipe_id}"
    
    cursor.execute(delete_query)
    conn.commit()

    print("Recipe with ID " + str(recipe_id).strip() + " deleted successfully!")

# Displays all recipes available
def display_recipes(cursor):
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()

    if not results:
        print("\nNo recipes were found.")
    else:
        for row in results:
            print("\nName:", row[1])
            print("Ingredients:", row[2])
            print("Cooking time:", row[3], "minutes")
            print("Difficulty:", row[4])

main_menu(conn, cursor)