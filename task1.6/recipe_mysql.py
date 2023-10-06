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

