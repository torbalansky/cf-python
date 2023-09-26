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