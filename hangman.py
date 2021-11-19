from os import system
from functools import reduce
import random

def loadWords(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read().splitlines()


def run():
    print("Welcome to Hangman!")
    # words = loadWords("words.txt")
    words = ["hola", "mundo", "perro", "gato", "casa", "coche", "casa", "coche"]
    word = random.choice(words)
    letters = list(word)
    missing_word = []
    [missing_word.append({"value": x, "check": False}) for x in letters]
    win = False
    attempts = 0
    while win == False and attempts < 6:
        print_word(missing_word, attempts)
        new_letter = input("Nueva letra: ")
        missing_word = [letter | {"check": letter["value"] == new_letter or letter["check"]} for letter in missing_word]
        win = reduce(lambda x, y: x and y, [d['check'] for d in missing_word] )
        attempts = attempts + 1
    print_word(missing_word, attempts)
    print("Tu ganas!!!")

def print_word(word, attempts):
    system("clear")
    print("Digite una letra y descubra la palabra:")
    secret_word = ""
    for letter in word:
        if(letter["check"]):
            secret_word = secret_word + letter["value"]
        else:
            secret_word = secret_word + "_"
        secret_word = secret_word + " "
    print(secret_word)
    print("Intentos: " + str(attempts))


if __name__ == "__main__":
    run()