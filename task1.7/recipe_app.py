# Import necessary modules from SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
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
        print(recipe)
