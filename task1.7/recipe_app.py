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
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
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
