import random


print("Welcome To the Hangman's game ")
print("let's play the game")
print("you only 6 lives so try to guess the word within 6 attempts! Good luck !!")

wordlist = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
    "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry",
    "strawberry", "tangerine", "ugli", "vanilla", "watermelon", "xigua", "yellow",
    "zucchini", "apricot", "blueberry", "cantaloupe", "dragonfruit", "jackfruit",
    "lime", "melon", "nutmeg", "olive", "peach", "pear", "plum", "pomegranate",
    "quinoa", "rhubarb", "starfruit", "tamarind", "kumquat", "coconut", "chili",
    "basil", "cilantro", "oregano", "parsley", "sage", "thyme", "vanilla",
    "chocolate", "coffee", "tea", "sugar", "salt", "pepper", "cinnamon",
    "ginger", "garlic", "onion", "carrot", "potato", "broccoli", "spinach",
    "lettuce", "cabbage", "cauliflower", "zucchini", "eggplant", "bell pepper",
    "asparagus", "artichoke", "beet", "pumpkin", "squash", "radish", "turnip",
    "sweet potato", "corn", "pea", "green bean", "chickpea", "lentil",
    "tofu", "tempeh", "quinoa", "barley", "rice", "pasta", "bread",
    "tortilla", "croissant", "bagel", "muffin", "donut", "cake", "cookie",
    "pie", "brownie", "pudding", "ice cream", "gelato", "sorbet", "yogurt",
    "salsa", "hummus", "guacamole", "dip", "syrup", "sauce", "jam",
    "jelly", "marmalade", "chutney", "pickle", "mustard", "ketchup", "barbecue",
    "dressing", "vinaigrette", "mayonnaise", "olive oil", "vinegar", "cooking oil",
    "butter", "margarine", "cream", "cheese", "milk", "yogurt", "egg",
    "pork", "beef", "chicken", "turkey", "duck", "lamb", "fish", "seafood",
    "shrimp", "crab", "lobster", "clam", "oyster", "mussel", "scallop",
    "ham", "bacon", "sausage", "salami", "pepperoni", "hot dog", "bologna",
    "sardine", "tuna", "salmon", "trout", "tilapia", "snapper", "cod"
]


lives=6
chosen_word=random.choice(wordlist)
print(chosen_word)

display=[]
for i in range(len(chosen_word)):
    display+='-'
print(display)


game_over=False

while not game_over:
    guessed_letter=input("Guess a letter : ").lower
    for position in range(chosen_word):