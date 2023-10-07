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
        print("Main Menu")
        print("1. Create a new recipe")
        print("2. Search for recipes by ingredients")
        print("3. Update an existing recipe")
        print("4. Delete a recipe")
        print("5. Quit")

        # Prompts the user for their choice
        choice = input("Enter your choice: ")

        # Checks the user's choice and performs the corresponding action
        if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(conn, cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)
        elif choice == "5":
            # If the user selects option 5 (Quit), commit any changes, close the connection, and exit the program
            conn.commit()
            conn.close()
            exit()
        else:
            # Displays an error message for an invalid choice
            print("Invalid choice. Please enter a valid option 1-5.")


def create_recipe(conn, cursor):
    # Recipe details
    name = input("Enter the name of the recipe:")
    cooking_time = int(input("Enter the cooking time in minutes:"))
    ingredients = input("Enter the ingredients (comma-separated): ") .split(", ")

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
