"""Functions for compiling dishes and ingredients for a catering company.""" 

from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name: str, dish_ingredients: list[str]) -> tuple[str, set[str]]:
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name: str, drink_ingredients: list[str]) -> str:
    return f"{drink_name} Mocktail" if ALCOHOLS.isdisjoint(drink_ingredients) else f"{drink_name} Cocktail"


def categorize_dish(dish_name: str, dish_ingredients: list[str]) -> str:
    
    categories = {"VEGAN":VEGAN, "VEGETARIAN":VEGETARIAN, 
                  "PALEO":PALEO, "KETO":KETO, "OMNIVORE":OMNIVORE}
    category = next((cat for cat, ingredients in categories.items() 
                    if set(dish_ingredients).issubset(ingredients)), 
                    "Not found")

    return f"{dish_name}: {category}"


def tag_special_ingredients(dish: tuple[str, list[str]]) -> tuple [str, set[str]]:
    name, ingredients = dish
    special_ingredients = [ing for ing in ingredients if ing in SPECIAL_INGREDIENTS]
    return (name, set(special_ingredients))

def compile_ingredients(dishes: list[set[str]]) -> set[str]:
    return set().union(*dishes)

def separate_appetizers(dishes: list[str], appetizers: list[str]) -> list[str]:
    return list(set(dishes).difference(set(appetizers)))

def singleton_ingredients(dishes, intersection):
    ingredient_counts = {ingredient: sum(1 for dish in dishes if ingredient in dish) for dish in dishes for ingredient in dish}
    return {ingredient for ingredient, count in ingredient_counts.items() if count == 1} 
