# Define a class - recipe
class Recipe:
    def __init__(self, name, cooking_time):
        self.name = name
        self.ingredients = []
        self.cooking_time = cooking_time
        self.difficulty = None

    # Class variable to keep track of all ingredients
    all_ingredients = set()

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
    
    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients

    def update_all_ingredients(self):
        Recipe.all_ingredients.update(self.ingredients)

    def __str__(self):
        ingredients_str = ", ".join(self.ingredients)
        return "Recipe: " + self.name + "\nIngredients: " + ingredients_str + "\nCooking time: " + str(self.cooking_time) + " minutes\nDifficulty: " + self.get_difficulty()

# Method to search for recipes by searching for a specific ingredient
def recipe_search(data, search_item):
    found_recipes = []
    for recipe in data:
        if recipe.search_ingredient(search_item):
            found_recipes.append(recipe)
    return found_recipes

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

# Create a list of recipes
recipes_list = [tea, coffee, cake, banana_smoothie, musaka]

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
