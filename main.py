Commit Message: Remove unnecessary conditional in get_recipes_by_ingredient method

```python


class Ingredient:
    def __init__(self, name):
        self.name = name


class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions


class RecipeBook:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def get_recipe(self, name):
        for recipe in self.recipes:
            if recipe.name == name:
                return recipe
        return None

    def get_recipes_by_ingredient(self, ingredient_name):
        matching_recipes = []
        for recipe in self.recipes:
            for ingredient in recipe.ingredients:
                if ingredient.name == ingredient_name:
                    matching_recipes.append(recipe)
                    break
        return matching_recipes


def main():
    # Create a recipe book
    book = RecipeBook()

    # Create some recipes
    ingredient1 = Ingredient("spaghetti")
    ingredient2 = Ingredient("bacon")
    ingredient3 = Ingredient("eggs")
    ingredient4 = Ingredient("parmesan cheese")
    recipe1 = Recipe(
        "Pasta Carbonara",
        [ingredient1, ingredient2, ingredient3, ingredient4],
        "1. Cook spaghetti. 2. Fry bacon. 3. Beat eggs with parmesan cheese. 4. Combine cooked spaghetti, bacon, and egg mixture."
    )

    ingredient5 = Ingredient("chicken")
    ingredient6 = Ingredient("broccoli")
    ingredient7 = Ingredient("carrots")
    ingredient8 = Ingredient("soy sauce")
    recipe2 = Recipe(
        "Chicken Stir-Fry",
        [ingredient5, ingredient6, ingredient7, ingredient8],
        "1. Cut chicken into small pieces. 2. Stir-fry chicken, broccoli, and carrots. 3. Add soy sauce."
    )

    # Add recipes to the recipe book
    book.add_recipe(recipe1)  # Adding recipe1 to the recipe book
    book.add_recipe(recipe2)  # Adding recipe2 to the recipe book

    # Get a recipe by name
    pasta_carbonara_recipe = book.get_recipe("Pasta Carbonara")
    if pasta_carbonara_recipe:
        print("Recipe found:", pasta_carbonara_recipe.name)
        print("Ingredients:")
        for ingredient in pasta_carbonara_recipe.ingredients:
            print("-", ingredient.name)
        print("Instructions:", pasta_carbonara_recipe.instructions)
    else:
        print("Recipe not found.")

    # Get recipes by ingredient
    recipes_with_bacon = book.get_recipes_by_ingredient("bacon")
    if recipes_with_bacon:
        print("\nRecipes with bacon:")
        for recipe in recipes_with_bacon:
            print("-", recipe.name)
    else:
        print("No recipes found with bacon.")


if __name__ == "__main__":
    main()
```
