def cookbook(*args):
    book, output = {}, []
    for x in args:
        recipes_name, cuisine, ingredients = x
        book[cuisine] = book.get(cuisine, {})
        book[cuisine].update({recipes_name: ingredients})

    for cuisine in sorted(book, key=lambda x: (-len(book[x]), x)):
        output.append(
            f"{cuisine} cuisine contains {len(book[cuisine])} recipes:")
        for recipe in sorted(book[cuisine]):
            output.append(
                f"  * {recipe} -> Ingredients: {', '.join(book[cuisine][recipe])}")

    return '\n'.join(output)


print(cookbook(
    ("Spaghetti Bolognese", "Italian", [
     "spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", [
     "pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))

'''
Italian cuisine contains 3 recipes:
  * Margherita Pizza -> Ingredients: pizza dough, tomato sauce, mozzarella
  * Spaghetti Bolognese -> Ingredients: spaghetti, tomato sauce, ground beef
  * Tiramisu -> Ingredients: ladyfingers, mascarpone, coffee
French cuisine contains 2 recipes:
  * Croissant -> Ingredients: flour, butter, yeast
  * Ratatouille -> Ingredients: eggplant, zucchini, tomatoes


'''
