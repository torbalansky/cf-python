# Exercise 1: Setting Up Python Development Environment

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
Open a Python script in an editor of your choice and name it "Exercise_1.3.py".

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
