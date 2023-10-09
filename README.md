# Table of Content

1. [Exercise 1](#exercise-1)
2. [Exercise 2](#exercise-2)
3. [Exercise 3](#exercise-3)
4. [Exercise 4](#exercise-4)
5. [Exercise 5](#exercise-5)
6. [Exercise 6](#exercise-6)
7. [Exercise 7](#exercise-7)

# Exercise 1 Setting Up Python Development Environment

## Table of Contents
1. [Installing Python](#installing-python)
2. [Creating a Virtual Environment](#creating-a-virtual-environment)
3. [Creating a Python Script](#creating-a-python-script)
4. [Setting Up IPython Shell](#setting-up-ipython-shell)
5. [Exporting a Requirements File](#exporting-a-requirements-file)

### 1. Installing Python

Begin by installing Python version 3.8.7 on your system. To confirm your Python version, execute the command `python --version` in your terminal.

![Step 1](./task1.1/Step_1.png)

### 2. Creating a Virtual Environment

Create a new virtual environment named "cf-python-base." 

![Step 2](./task1.1/Step_2.png)

### Creating a Python Script

Install a text editor like Visual Studio Code or any other of your preference. Create a Python script named "add.py." This script will take two user-input numbers, add them, and display the result. Below is a template for your Python script:

```python
# Get input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Add the numbers
c = a + b

# Print the result
print("The sum of {} and {} is: {}".format(a, b, c))
```

![Step 3](./task1.1/Step_3.png)

### Setting Up IPython Shell

Establish an IPython shell within the "cf-python-base" virtual environment. IPython provides a more feature-rich Python interactive shell, including syntax highlighting, auto-indentation, and advanced auto-complete features. 

![Step 4](./task1.1/step_4.png)

### Exporting a Requirements File

Generate a "requirements.txt" file from your current environment, listing all the installed packages and their versions. Then, create a new environment named "cf-python-copy" and install the packages from the "requirements.txt" file.

![Step 5](./task1.1/step_5.png)

# Exercise 2

## Table of Contents

1. [Create the Data Structure](#create-the-data-structure)
2. [Create `recipe_1`](#create-recipe_1)
3. [Create Outer Structure](#create-outer-structure)
4. [Create 4 More Recipes](#create-4-more-recipes)
5. [Print Ingredient Lists](#print-ingredient-lists)

### Create the Data Structure

```python
# Define the structure for `recipe_1`
recipe_1 = {
    'name': 'Recipe 1',
    'cooking_time': 45,  # Replace with the actual cooking time
    'ingredients': ['Ingredient 1', 'Ingredient 2', 'Ingredient 3']  # Replace with actual ingredients
}
```

![step 1](./taks1.2/step_1.png)

A dictionary is chosen for its key-value structure, aligning with the need to associate attributes with the recipe. It allows easy access to information via keys and accommodates various data types. This structure fosters organization and consistency, ideal for storing multiple recipes in a list, simplifying data manipulation and analysis.

### Create `recipe_1`

![step 2](./taks1.2/step_2.png)

### Create Outer Structure

Create an outer structure called all_recipes.

![step 3](./taks1.2/step_3.png)

Using a list provides a sequential and dynamic structure, allowing easy modification and retrieval of recipes based on their order. Lists support iteration and indexing, enabling convenient operations on individual recipes or the entire collection. The versatility of lists accommodates recipes of varying lengths and complexities, making it suitable for a diverse range of recipe structures. Overall, a list provides the flexibility, scalability, and ease of access required for managing and modifying multiple recipes.

### Create 4 More Recipes

Generate 4 more recipes as `recipe_2`, `recipe_3`, `recipe_4`, and `recipe_5`, and add them to `all_recipes`.

![step 4](./taks1.2/step_4.png)

### Print Ingredient Lists

Print the ingredients of each recipe.

![step 5](./taks1.2/step_5.png)
or
![step 5](./taks1.2/step_5b.png)

# Exercise 3

## Table of Contents
1. [Create a New Python Script](#create-a-new-python-script)
2. [Initialize Two Empty Lists](#initialize-two-empty-lists)
3. [Define a Function](#define-a-function)
4. [Get The Number of New Recipes](#get-the-number-of-new-recipes)
5. [Check Ingredients and Add Recipes](#check-ingredients-and-add-recipes)
6. [Assign Difficulty Levels and Display Recipes](#assign-difficulty-levels-and-display-recipes)
7. [Display All Ingredients](#display-all-ingredients)
8. [Output](#output)

### Create a New Python Script
Open a Python script in an editor of your choice and name it "exercise_1.3.py".

### Initialize Two Empty Lists
Begin by initializing two empty lists: `recipes_list` and `ingredients_list`.

```python

#Empty lists storing recipes and ingredients
recipes_list = [] # List to store recipe dictionaries
ingredients_list = [] # List to store ingredients
```

### Define a Function
Create a function called `take_recipe` that takes user input for the following variables:
- `name` (str): Stores the name of the recipe.
- `cooking_time` (int): Stores the cooking time (in minutes).
- `ingredients` (list): A list to store ingredients, each of the string data type.
- `recipe` (dictionary): Store the `name`, `cooking_time`, and `ingredients` variables in a dictionary (e.g., `recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}`).

```python
# Recipe input from the user
def take_recipe(recipe_number):
    name = input(f"Enter the name of recipe {recipe_number}: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = input("Enter ingredients separated by commas (e.g., Eggs, Salt, Pepper): ").split(", ")
    
    recipe = {"name": name, "cooking_time": cooking_time, "ingredients": ingredients}
    recipes_list.append(recipe)
    ingredients_list.extend(ingredients)  # Extend the ingredients_list with the ingredients
    
    return recipe
```

### Get the Number of New Recipes
Ask the user how many recipes they would like to enter, and store their response in a variable called `n`.

```python
n = int(input("How many recipes would you like to enter? "))
```

### Check Ingredients and Add Recipes
Run a for loop, which runs `n` times to perform the following steps:
- Run `take_recipe()` and store its return output (a dictionary) in a variable called `recipe`.
- Run another for loop inside this loop, which iterates through `recipe`'s ingredients list. It picks out elements one-by-one as `ingredient`. Inside this loop, check if the chosen ingredient isn't present in `ingredients_set`, and if not, add it to this set.
- Once finished adding ingredients, append `recipe` to `recipes_list`.

```python
# Loop to take input for each recipe
for i in range(1, n + 1):              # Count the number of recipes entered
    recipe = take_recipe(i)            # Call the function to get a recipe

    # Loop to add unique ingredients to ingredients_list
    for ingredient in recipe["ingredients"]:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
```

### Assign Difficulty Levels and Display Recipes
Run another for loop that iterates through `recipes_list` and assigns a difficulty level based on the following criteria:
- If `cooking_time` is less than 10 minutes and the number of ingredients is less than 4, set a variable called `difficulty` to the value of **Easy**.
- If `cooking_time` is less than 10 minutes and the number of ingredients is greater than or equal to 4, set a variable called `difficulty` to the value of **Medium**.
- If `cooking_time` is greater than or equal to 10 minutes and the number of ingredients is less than 4, set a variable called `difficulty` to the value of **Intermediate**.
- If `cooking_time` is greater than or equal to 10 minutes and the number of ingredients is greater than or equal to 4, set a variable called `difficulty` to the value of **Hard**.

Display each recipe with the following details:
- Recipe:
- Cooking Time (minutes):
- Ingredients:
- Difficulty level:

```python
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
```

### Display All Ingredients
Display all the ingredients that you've come across so far in all of the recipes that you've entered.
```python
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
```

### Output

![Output](./task1.3/task_output.png)

# Exercise 4 

## Part 1

### Table of Contents

1. [Importing the Pickle Module](#importing-the-pickle-module)
2. [Defining the 'take_recipe' Function](#defining-the-take-recipe-function)
3. [Defining the 'calculate_difficulty' Function](#defining-the-calc-difficulty-function)
4. [Attempting to Open a File](#attempting-to-open-a-file)
5. [Taking Additional Recipes](#taking-additional-recipes)
6. [Creating the Data Dictionary](#creating-the-data-dictionary)
7. [Saving Data to a File](#saving-data-to-a-file)

### Importing the Pickle Module

```python
import pickle
```

### Defining the 'take_recipe' Function

Define a function called `take_recipe()` to receive recipes from the user. This function performs the following tasks:

```python
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
```

### Defining the 'calculate_difficulty' Function

Define the function `calculate_difficulty()`, which determines the recipe's difficulty based on specific criteria:

- If cooking time is less than 10 minutes and ingredients are less than 4, set difficulty to 'Easy'.
- If cooking time is less than 10 minutes and ingredients are 4 or more, set difficulty to 'Medium'.
- If cooking time is 10 minutes or more and ingredients are less than 4, set difficulty to 'Intermediate'.
- If cooking time is 10 minutes or more and ingredients are 4 or more, set difficulty to 'Hard'.

```python
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
```

### Attempting to Open a File

```python
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
```

### Taking Additional Recipes

Ask the user how many recipes they want to enter and use a loop to call the take_recipe() function for each recipe.

```python
# Ask the user how many recipes they want to enter
num_recipes = int(input("How many recipes would you like to enter? "))

# Loop to take recipes from the user
for i in range(1, num_recipes + 1):
    recipe = take_recipe(i)
    # Calculate difficulty for the current recipe
    calculate_difficulty(recipe)  
```

### Creating the Data Dictionary

Gather the updated `recipes_list` and `all_ingredients` into a dictionary called `data`.

```python
# Update the data dictionary with the new lists
data["recipes_list"] = recipes_list
data["all_ingredients"] = ingredients_list
```

### Saving Data to a File

Open a user-defined binary file and save the `data` using the Pickle module.

```python
# Open the file and write the updated data using pickle
with open(filename, 'wb') as file:
    pickle.dump(data, file)

print(f"Recipe data saved to '{filename}'.")
```

## Part 2

### Table of Contents

1. [Importing the Pickle Module](#importing-the-pickle-module)
2. [Defining the 'Display Recipe' Function](#defining-the-display-recipe-function)
3. [Defining the 'Search Ingredient' Function](#defining-the-search-ingredient-function)
4. [Asking User for Recipe File](#asking-user-for-recipe-file)
5. [Attempting to Open User File](#attempting-to-open-user-file)
6. [Creating the Except Block](#creating-the-except-block)
7. [Creating the Else Block](#creating-the-else-block)

### Importing the Pickle Module

```python
import pickle
```

### Defining the 'Display Recipe' Function

Define a function that takes a recipe dictionary as an argument and displays its attributes, including name, cooking time, ingredients, and difficulty.

```python
# Function to display a recipe
def display_recipe(recipe):
    print("Recipe Name:", recipe["name"])
    print("Cooking Time (minutes):", recipe["cooking_time"])
    print("Ingredients:", ", ".join(recipe["ingredients"]))
    print("Difficulty:", recipe["difficulty"])
    print() 
```

### Defining the 'Search Ingredient' Function

Define a function that takes a data dictionary as an argument.

```python
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
```

### Asking User for Recipe File

Prompt the user for the filename containing recipe data.

```python
# Main code
filename = input("Enter the filename containing your recipe data: ")
```

### Attempting to Open User File

Implement a try block to open the user-specified file and extract its contents into `data` using the Pickle module.

```python
try:
    # Try to open the file for reading using a 'with' statement
    with open(filename, 'rb') as file:
        # Load existing data from the file using pickle
        data = pickle.load(file)
```

### Creating the Except Block

Handle exceptions if the try block fails and inform the user that the file was not found.

```python
except FileNotFoundError:
    # Handle the case when the file doesn't exist
    print(f"File '{filename}' not found. Please make sure the file exists.")
except Exception as e:
    print(f"An error occurred while opening the file: {e}")
```

### Creating the Else Block

Define an else block that calls the `search_ingredient()` function, passing `data` as an argument.

```python
else:
    # Call the search_ingredient function with the loaded data
    search_ingredient(data)
```

## Part 3

### Running the Input Script

Execute "recipe_input.py" and enter sample recipes. Ensure that the script can generate a binary file upon execution.

![Input](./task1.4/input.png)

### Running the Search Script

Execute "recipe_search.py," enter the ingredient to be searched for, and verify that it produces the desired output with relevant recipes.

![Search](./task1.4/search.png)

# Exercise 5

### Table of Contents

1. [Define Recipe Class](#define-recipe-class)
2. [Define Methods](#define-methods)
3. [Create Recipe Search Method](#create-recipe-search-method)
4. [Create Objects](#create-object)
5. [Create Recipes List](#create-recipes-list)
6. [Search and display Recipes](#search-and-display-recipes)
7. [Run the Script](#run-the-script)

### Define Recipe Class

Define a class called `Recipe`, which represents recipes with attributes like name, ingredients, cooking time, and difficulty.

```python
# Define a class - recipe
class Recipe:
    def __init__(self, name, cooking_time):
        self.name = name
        self.ingredients = []
        self.cooking_time = cooking_time
        self.difficulty = None

    # Class variable to keep track of all ingredients
    all_ingredients = set()
```

### Define Methods

Define various methods within the `Recipe` class for getting and setting attributes, adding ingredients, and calculating difficulty.

```python
   # Get and set methods for name and cooking_time
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_cooking_time(self):
        return self.cooking_time
    
    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

    # Method to add ingredients
    def add_ingredients(self, *ingredients):
        self.ingredients.extend(ingredients)
        self.update_all_ingredients()

    # Get method for ingredients
    def get_ingredients(self):
        return self.ingredients
    
    # Method to calculate difficulty based on cooking time and number of ingredients
    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

    # Get method for difficulty
    def get_difficulty(self):
        if not self.difficulty:
            self.calculate_difficulty()
        return self.difficulty
    
    # Search for a specific ingredient in the recipe's ingredients
    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients

    # Update the class-level set variable with all unique ingredients across recipes
    def update_all_ingredients(self):
        Recipe.all_ingredients.update(self.ingredients)

    ## String representation of the recipe
    def __str__(self):
        ingredients_str = ", ".join(self.ingredients)
        return "Recipe: " + self.name + "\nIngredients: " + ingredients_str + "\nCooking time: " + str(self.cooking_time) + " minutes\nDifficulty: " + self.get_difficulty()
```

### Create Recipe Search Method

Implement a `recipe_search()` method that allows searching for recipes based on specific ingredients.

```python
    # Method to search for recipes by searching for a specific ingredient
    def recipe_search(data, search_item):
        found_recipes = []
        for recipe in data:
            if recipe.search_ingredient(search_item):
                found_recipes.append(recipe)
        return found_recipes
```

### Create recipes objects

Create instances of the `Recipe` class for different recipes like tea, coffee, cake, etc.

```python
# Create recipe objects
tea = Recipe('Tea', 5)
tea.add_ingredients('Tea Leaves', 'Milk', 'Water')

coffee = Recipe('Coffee', 5)
coffee.add_ingredients('Coffee', 'Sugar', 'Water')

cake = Recipe('Cake', 50)
cake.add_ingredients('Sugar', 'Butter', 'Eggs', 'Vanilla Essence', 'Flour', 'Baking Powder', 'Milk')

banana_smoothie = Recipe('Banana Smoothie', 5)
banana_smoothie.add_ingredients('Bananas', 'Milk', 'Peanut Butter', 'Sugar', 'Ice Cubes')

musaka = Recipe('Musaka', 60)
musaka.add_ingredients('Potatoes', 'Chopped pork', 'Eggs', 'Sour Milk', 'Flour', 'Salt', 'Pepper', 'Tomato paste', 'Onion')
```

### Create Recipes List

Wrap the recipes into a list called `recipes_list`.

```python
# Create a list of recipes
recipes_list = [tea, coffee, cake, banana_smoothie, musaka]
```
### Search for Recipes and siplay all recipes, as well as recipes based on ingredients

Utilize the `recipe_search()` method to search for recipes containing specific ingredients like Water, Sugar, Bananas, and Potatoes. Then display the recipes found, as well as all recipes.

```python
# Search for recipes containing specific ingredients
water_recipes = recipe_search(recipes_list, 'Water')
sugar_recipes = recipe_search(recipes_list, 'Sugar')
banana_recipes = recipe_search(recipes_list, 'Bananas')
potato_recipes = recipe_search(recipes_list, 'Potatoes')

# Display the str representation of each recipe
for recipe in recipes_list:
    print(recipe)
    print()

# Display recipes containing specific ingredients
print("Recipes containing Water:")
for recipe in water_recipes:
    print(recipe)
    print()

print("Recipes containing Sugar:")
for recipe in sugar_recipes:
    print(recipe)
    print()

print("Recipes containing Bananas:")
for recipe in banana_recipes:
    print(recipe)
    print()

print("Recipes containing Potatoes:")
for recipe in potato_recipes:
    print(recipe)
    print()
```
### Run the Script

Run “recipe_oop.py”.

![output](./task1.5/output.png)

# Exercise 6

## Part 1

### Import MySQL Connector

- Import the `mysql` module to enable database operations.

```python
# Imports MySQL connector
import mysql.connector
```

### Initialize Connection Object

- Initialize a connection object to establish a connection to the MySQL server. Use the following parameters:

- Hostname: localhost
- Username: cf-python
- Password: password

```python
# Initializes connection to the MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="cf-python",
    passwd="password"
)
```

### Create a Cursor

- Create a cursor object to interact with the database.

```python 
# Initializes the cursor object from the connection
cursor = conn.cursor()
```

### Create a Database

- Create a database named `task_database` if it doesn't already exist.
```python 
# Creates the database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
```

### Use the Database

- Connect to the `task_database` using the `USE` statement to specify the database for operations.
```python 
# Connects to the database using the USE statement
cursor.execute("USE task_database")
```

### Create a Table

- Create a table named `Recipes` with specific columns:

- id: INT AUTO_INCREMENT PRIMARY KEY
- name: VARCHAR(50)
- ingredients: VARCHAR(255)
- cooking_time: INT
- difficulty: VARCHAR(20)

```python
# Creates the Recipes table with specified columns
cursor.execute("CREATE TABLE IF NOT EXISTS Recipes ("
               "id INT AUTO_INCREMENT PRIMARY KEY,"
               "name VARCHAR(50),"
               "ingredients VARCHAR(255),"
               "cooking_time INT,"
               "difficulty VARCHAR(20)"
               ")")
```

## Part 2

### Create the Main Menu

- Define the function for the main menu

```python 
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
            search_recipe(conn, cursor)
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
```

## Part 3

- Start the Create Recipe Function

```python 
def create_recipe(conn, cursor):
    # Recipe details
    name = input("Enter the name of the recipe:")
    cooking_time = int(input("Enter the cooking time in minutes:"))
    ingredients = input("Enter the ingredients (comma-separated): ") .split(", ")

```

- Call the calculate_difficulty() function with cooking_time and ingredients as arguments to calculate the recipe's difficulty and store the result in a variable called difficulty.

```python 
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
```
- Generate an SQL query to insert the recipe into the Recipes table in your database. Convert the ingredients list into a comma-separated string, as MySQL doesn't fully support arrays.

```python 
# Converts ingredients list to a comma-separated str
    ingredients_str = ", ".join(ingredients)

    # Builds the SQL query
    query = "INSERT INTO Recipes (name, cooking_time, ingredients, difficulty) VALUES (%s, %s, %s, %s)"
      
    # Executes the query
    cursor.execute(query, (name, cooking_time, ingredients_str, difficulty))

    # Commits the changes to the DB
    conn.commit()

    print(f"Recipe '{name}' added successfully")
```

## Part 4

### Retrieve Unique Ingredients
- To initiate this process, the first step is to obtain a comprehensive list of ingredients available in the Recipes table. This is accomplished by executing a SQL SELECT query solely on the ingredients column of your table. The resulting data is stored in a variable named results.

```python 
# Retrieves a list of all unique ingredients from the Recipes table
    cursor.execute("SELECT DISTINCT ingredients FROM Recipes")
    results = cursor.fetchall()
    all_ingredients = []
```

### Extract Unique Ingredients
- After obtaining the list of ingredients, you proceed to extract the unique ingredients from the results variable. Each row of the results is processed, and the ingredients are split into a list. Unique ingredients are added to the all_ingredients list, ensuring that duplicates are not included.

```python 
# Extracts unique ingredients
    for row in results:
        ingredients_str = row[0]
        ingredients_list = ingredients_str.split(", ")

        # Adds unique ingredients to the ingredient list
        for ingredient in ingredients_list:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)
```

### Display Available Ingredients
- This section is responsible for displaying all available ingredients to the user. It iterates through the all_ingredients list, presenting each ingredient along with a corresponding number for user reference.

```python 
# Displays all ingredients to the user
    print("Available ingredients:")
    for index, ingredient in enumerate(all_ingredients, start=1):
        print(str(index) + ". " + ingredient)
```

### Prompt User for Ingredient Selection
- Here, the code prompts the user to select an ingredient they want to search for. It takes user input as a number corresponding to the ingredient they wish to search for. The input is validated to ensure it falls within the valid range of available ingredients.

```python 
# Prompt the user to select an ingredient to search for
    try:
        choice = int(input("Enter the number of the ingredient to search for: "))

        if 1 <= choice <= len(all_ingredients):
            search_ingredient = all_ingredients[choice - 1]
```

### Build SQL Query for Ingredient Search
- After the user selects an ingredient, this section constructs an SQL query for searching recipes containing the chosen ingredient. It uses the LIKE operator with wildcard '%' to perform a partial match search within the 'ingredients' column of the Recipes table.

```python 
# Build the SQL query for searching recipes containing the chosen ingredient
            query = "SELECT name FROM Recipes WHERE ingredients LIKE '%" + search_ingredient + "%'"
            cursor.execute(query)
```

### Fetch and Display Search Results
- Finally, the code fetches and displays the search results. If recipes containing the chosen ingredient are found in the database, they are printed to the console. If no matching recipes are found, a message indicating so is displayed.

```python 
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
```

## Part 5

### Define the Update Recipe Function:
  - Retrieve all existing recipes from the database and present them to the user.
  - Allow the user to choose a recipe for updates by specifying its corresponding ID.
  - Prompt the user to specify the column they want to update for the selected recipe. Available columns for modification include name, cooking_time, and ingredients.

```python 
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
```

### Collect the New Value From User:
  - Once the user selects the column requiring an update, gather the new value from the user.
  - Note that if the user updates either cooking_time or ingredients, the script will also recalculate the recipe's difficulty and update that column accordingly.

```python 
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
```

### Build Queries:
  - Construct a query in the form of a string to update an entry in the table, considering the provided ID, column, and the updated value.
  - Execute the constructed query and commit the changes to the database table.

```python 
    try:
        # Executes the update query
        cursor.execute(update_query)
        # Commits the changes to the DB
        conn.commit()
        print("Recipe with ID " + str(recipe_id) + " updated successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
```

## Part 6

### Define the Delete Recipe Function:
  - Display all recipes stored in your database table to the user.
  - Enable the user to select a recipe for deletion by specifying its ID.

```python 
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
```

### Build Query:
  - Construct a query using the DELETE statement to remove the chosen recipe from the table. Identify the row to delete based on the provided ID.
```python 
# Builds the SQL query for deleting the selected recipe
    delete_query = f"DELETE FROM Recipes WHERE id = {recipe_id}"
    
    cursor.execute(delete_query)
    conn.commit()

    print("Recipe with ID " + str(recipe_id).strip() + " deleted successfully!")
```

## Part 7

### Display all Available Recipes:
  - Show a list of all available recipes, including details such as name, cooking_time, ingredients, and difficulty.

```python 
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
```
## Part 8

### Run Script
 - Ensure that your MySQL server is running on your system. Thereafter, run your script.
![step 1](./task1.6/part8_step1_main_menu.png)
### Add Recipes
 - Create recipe/s of your choice using the first option in your menu.
![step 2](./task1.6/part8_step2_create.png)
### Run a Search
 - Run a search by selecting the ingredient to search for.
![step 3](./task1.6/part8_step3_search.png)
### Update a Recipe
 - Change a few values in some of your recipes.
![step 4](./task1.6/part8_step4_update.png)

### Delete a Recipe (Display the remaining recipes - Optional)
![step 5](./task1.6/part8_step5_delete.png)
### Exit
![step 6](./task1.6/exit.png)

# Exercise 7

## Part 1

- Create Recipe App
  - In a file called recipe_app.py import all the packages and methods necessary to build the recipe application.

```python 
# Displays all recipes available
# Import necessary modules from SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, or_, and_
from sqlalchemy.orm import sessionmaker, declarative_base
```

- Create an engine
  
```python 
# Create an SQLAlchemy engine to connect to the MySQL DB
engine = create_engine("mysql://cf-python:password@localhost/task_database")
```

- Create the Session Object and declarative base class
 ```python 
# Create a Session class that binds to the DB engine
Session = sessionmaker(bind=engine)

# Create a session object, which will be used for DB interactions
session = Session()

# Create a declarative base class
Base = declarative_base()
```
## Part 2

- Define an attribute to set the table’s name as final_recipes  and  create table columns
    - id: integer; primary key; increments itself automatically.
    - name: string with 50-character limit; stores the recipe’s name. 
    - ingredients: string type; character limit of 255; stores the ingredients of the recipe in the form of a string.
    - cooking_time: integer; stores the recipe’s cooking time in minutes
    - difficulty: string with 20-character limit; stores one of four strings that describe the difficulty of the recipe (Easy; Medium; Intermediate; Hard).

 ```python 
# Define the Recipe class as a model
class Recipe(Base):
    # Set the table name
    __tablename__ = "final_recipes"

    # Define columns for the table
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    # Define a representation method for debugging
    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"
    
    # Define a string representation method for user output
    def __str__(self):
        return (
            f"Recipe ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Ingredients: {self.ingredients}\n"
            f"Cooking Time: {self.cooking_time} minutes\n"
            f"Difficulty: {self.difficulty}"
        )

    # Define a method to calculate recipe difficulty
    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.return_ingredients_as_list()) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(self.return_ingredients_as_list()) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(self.return_ingredients_as_list()) < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

    # Define a method to return ingredients as a list
    def return_ingredients_as_list(self):
        if not self.ingredients:
            return []
        else:
            return self.ingredients.split(", ")

# Create the corresponding table in the database
Base.metadata.create_all(engine)
```

## Part 3

### Create recipe functions

 - Function 1: create_recipe()

```python 
def create_recipe(session):
    try:
        # Recipe details
        name = input("Enter the name of the recipe:")

        if len(name) > 50:
            print("Recipe name is too long (max 50 characters).")
            return
        
        ingredients = []
        num_ingredients = int(input("Enter the number of ingredients:"))
        for i in range(num_ingredients):
            ingredient = input(f"Enter ingredient {i + 1}: ")
            ingredients.append(ingredient)

        ingredients_str = ", ".join(ingredients)

        # Check if cooking time is a valid number
        try:
            cooking_time = int(input("Enter cooking time (in minutes): "))
        except ValueError:
            print("Invalid cooking time. Please enter a valid number!")
            return
        
        # Create a new recipe object
        recipe_entry = Recipe(name=name, ingredients=ingredients_str, cooking_time=cooking_time)

        # Calculate and set difficulty
        recipe_entry.calculate_difficulty()

        # Add the recipe to the database and commit the change
        session.add(recipe_entry)
        session.commit()

        # Print success message
        print_result_message(success=True)

    except Exception as e:
        # Print error message with exception details
        print_result_message(success=False, message="There was an error creating the recipe:", exception=e)
```

 - Function 2: view_all_recipes()

```python 
def view_all_recipes(session):
    # Retrieve all recipes from the DB and display them
    recipes = session.query(Recipe).all()

    if not recipes:
        print("No recipes were found in the database!")
        return
    
    for recipe in recipes:
        print("+" * 40)
        print(recipe)
```

 - Function 3: search_by_ingredients()

```python 
def search_by_ingredients(session):
    try:
        # Check if there are any entries in the table
        if session.query(Recipe).count() == 0:
            print("No recipes found in the database.")
            return

        # Retrieve values from the 'ingredients' column
        results = session.query(Recipe.ingredients).all()

        all_ingredients = set()
        for result in results:
            ingredients_list = result[0].split(', ')
            all_ingredients.update(ingredients_list)

        # Display the available ingredients to the user
        print("Available ingredients:")
        for index, ingredient in enumerate(all_ingredients, start=1):
            print(f"{index}. {ingredient}")

        # Ask the user for ingredient choices
        ingredient_choices = input("Enter ingredient numbers separated by spaces: ").split()
        
        # Convert user input to integers
        ingredient_choices = [int(choice) for choice in ingredient_choices]

        # Validate user input
        if not all(1 <= choice <= len(all_ingredients) for choice in ingredient_choices):
            print("Invalid ingredient choice. Please enter valid numbers.")
            return

        # Get the selected ingredients as strings
        search_ingredients = [list(all_ingredients)[choice - 1] for choice in ingredient_choices]

        # Initialize a list of search conditions for at least one ingredient
        any_conditions = []
        for ingredient in search_ingredients:
            like_term = f"%{ingredient}%"
            any_conditions.append(Recipe.ingredients.like(like_term))

        # Query the database for recipes containing at least one selected ingredient
        any_matching_recipes = session.query(Recipe).filter(or_(*any_conditions)).all()

        # Initialize a list of search conditions for every ingredient
        all_conditions = []
        for ingredient in search_ingredients:
            like_term = f"%{ingredient}%"
            all_conditions.append(Recipe.ingredients.like(like_term))

        # Query the database for recipes containing every selected ingredient
        all_matching_recipes = session.query(Recipe).filter(and_(*all_conditions)).all()

        print("\nRecipes containing at least one selected ingredient:")
        if any_matching_recipes:
            for recipe in any_matching_recipes:
                print(recipe)
        else:
            print("No recipes found containing at least one selected ingredient.")

        print("\nRecipes containing every selected ingredient:")
        if all_matching_recipes:
            for recipe in all_matching_recipes:
                print(recipe)
        else:
            print("No recipes found containing every selected ingredient.")

    except Exception as e:
        print_result_message(success=False, message="An error occurred while searching for recipes:", exception=e)
```

 - Function 4: edit_recipe()

```python 
def edit_recipe(session):
    try:
        # Check if any recipes exist in the DB
        recipes = session.query(Recipe).all()
        if not recipes:
            print("No recipes were found.")
            return
        
        # Display the list of recipes to choose from
        print("\nRecipes")
        for i, recipe in enumerate(recipes, start=1):
            print(f"{i}. {recipe.name}")
        
        # Ask the user to select a recipe by number
        choice = input("Enter the number of the recipe to edit (or 'q' to quit): ")
        if choice.lower() == 'q':
            return
        
        try: 
            choice = int(choice)
            if 1 <= choice <= len(recipes):
                # Retrieve the selected recipe
                recipe_to_edit = recipes[choice - 1]

                # Display the selected recipe details
                print("\nSelected Recipe: ")
                print(recipe_to_edit)

                # Ask the user which attribute to edit
                attribute = input("\nEnter the number of the attribute to edit:"
                                  "\n1. Name\n2. Ingredients\n3. Cooking Time\n"
                                  "Or press 'q' to quit editing: ")
                
                if attribute.lower() == 'q':
                    return
                
                try:
                    attribute = int(attribute)
                    if attribute == 1:
                        # Edit recipe name
                        new_name = input("Enter the new name of the recipe: ")
                        if len(new_name) > 50:
                            print("Recipe name is too long (max 50 characters).")
                        else:
                            recipe_to_edit.name = new_name
                            session.commit()
                            print_result_message(success=True)
                    elif attribute == 2:
                        # Edit ingredients
                        num_ingredients = int(input("Enter the number of ingredients: "))
                        new_ingredients = []
                        for i in range(num_ingredients):
                            ingredient = input(f"Enter ingredient {i + 1}: ")
                            new_ingredients.append(ingredient)
                        recipe_to_edit.ingredients = ", ".join(new_ingredients)
                        
                        # Recalculate difficulty after updating ingredients
                        recipe_to_edit.calculate_difficulty()
                        
                        session.commit()
                        print_result_message(success=True)
                    elif attribute == 3:
                        new_cooking_time = input("Enter the new cooking time in minutes: ")
                        try:
                            new_cooking_time = int(new_cooking_time)
                            recipe_to_edit.cooking_time = new_cooking_time
                            recipe_to_edit.calculate_difficulty()
                            session.commit()
                            print_result_message(success=True)
                        except ValueError:
                            print("Invalid cooking time. Please enter a valid number.")
                    else:
                        print("Invalid attribute choice. Please enter a valid number (1, 2, or 3).")
                except ValueError:
                    print("Invalid attribute choice. Please enter a valid number (1, 2, or 3).")
            else:
                print("Invalid recipe choice. Please enter a valid number.")
        except ValueError:
            print("Invalid recipe choice. Please enter a valid number.")

    except Exception as e:
        print_result_message(success=False, message="There was an error editing the recipe:", exception=e)
```

 - Function 5: delete_recipe()

```python 
def delete_recipe(session):
    try:
        # Check the available recipes in the DB
        recipes = session.query(Recipe).all()
        if not recipes:
            print("No recipes found in the database.")
            return

        # Display a list of recipes to choose from
        print("\nRecipes:")
        for i, recipe in enumerate(recipes, start=1):
            print(f"{i}. {recipe.name}")

        # Ask the user to select a recipe by number
        choice = input("Enter the number of the recipe to delete (or 'q' to quit): ")
        if choice.lower() == 'q':
            return

        try:
            choice = int(choice)
            if 1 <= choice <= len(recipes):
                # Retrieve the selected recipe
                recipe_to_delete = recipes[choice - 1]

                # Display the selected recipe's details
                print("\nSelected Recipe:")
                print(recipe_to_delete)

                # Ask for confirmation
                confirm = input("Are you sure you want to delete this recipe? (yes/no): ").lower()
                if confirm == "yes":
                    session.delete(recipe_to_delete)
                    session.commit()
                    print_result_message(success=True)
                elif confirm == "no":
                    print("Recipe deletion canceled.")
                else:
                    print("Invalid choice. Please enter 'yes' or 'no'.")
            else:
                print("Invalid recipe choice. Please enter a valid number.")
        except ValueError:
            print("Invalid recipe choice. Please enter a valid number.")

    except Exception as e:
        print_result_message(success=False, message="There was an error deleting the recipe:", exception=e)
```

## Part 4

 - Create the Main Menu. 

```python 
def main_menu(session, engine):
    while True:
        # Display the main menu options
        print("\n==========================================")
        print("\nMain Menu:")
        print("1. Create a new recipe")
        print("2. View all recipes")
        print("3. Search recipe by ingredient")
        print("4. Edit a recipe")
        print("5. Delete a recipe")
        print("6. Exit")
        print("===========================================\n")


        # Get the user's choice
        choice = input("Enter your choice: ")

         # Process user's choice
        if choice == "1":
            create_recipe(session)
        elif choice == "2":
            view_all_recipes(session)
        elif choice == "3":
            search_by_ingredients(session)
        elif choice == "4":
            edit_recipe(session)
        elif choice == "5":
            delete_recipe(session)
        elif choice == "6":
            print("Bye!")
            session.close()
            engine.dispose()
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu(session, engine)
```

## Part 5

 - Output: Create a few recipes
    - ![step 1](./task1.7/Task1.7_create.png)
 - Output: View all recipes
    - ![step 2](./task1.7/Task1.7_view_all.png)
 - Output: Search recipe by ingredient/s
    - ![step 3](./task1.7/Task1.7_search_by_ingredient.png)
 - Output: Edit a recipe
    - ![step 4](./task1.7/Task1.7_update.png)
 - Output: Delete a recipe
    - ![step 5](./task1.7/Task1.7_delete.png)
 - Output: Exit the app
    - ![step 6](./task1.7/Task1.7_exit.png)