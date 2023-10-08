# Import necessary modules from SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, or_, and_
from sqlalchemy.orm import sessionmaker, declarative_base

# Create an SQLAlchemy engine to connect to the MySQL DB
engine = create_engine("mysql://cf-python:password@localhost/task_database")

# Create a Session class that binds to the DB engine
Session = sessionmaker(bind=engine)

# Create a session object, which will be used for DB interactions
session = Session()

# Create a declarative base class
Base = declarative_base()

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

def print_result_message(success=True, message="", exception=None):
    # This function prints a success or failure message based on the 'success' parameter
    if success:
        print()
        print("Operation successful!")
        print()
    else:
        print()
        print(f"Operation failed: {message}")
        if exception:
            print(f"Error details: {exception}")
        print()

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

def view_all_recipes(session):
    # Retrieve all recipes from the DB and display them
    recipes = session.query(Recipe).all()

    if not recipes:
        print("No recipes were found in the database!")
        return
    
    for recipe in recipes:
        print("+" * 40)
        print(recipe)

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

        # Initialize a list of search conditions
        conditions = []
        for ingredient in search_ingredients:
            like_term = f"%{ingredient}%"
            conditions.append(Recipe.ingredients.like(like_term))

        # Query the database for recipes matching the conditions
        matching_recipes = session.query(Recipe).filter(*conditions).all()

        if not matching_recipes:
            print("No recipes found matching the selected ingredients.")
        else:
            print("Matching Recipes:")
            for recipe in matching_recipes:
                print(recipe)

    except Exception as e:
        print_result_message(success=False, message="An error occurred while searching for recipes:", exception=e)

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
