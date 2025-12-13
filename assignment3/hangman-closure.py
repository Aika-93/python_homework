#Task_4: Closure Practice

def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter)
        result = ""
        for i in secret_word:
            if i in guesses:
                result += i
            else:
                result += "_"
        print(result)
        if "_" not in result:
            return True
        else:
            return False
    return hangman_closure

game = make_hangman(input("Enter the secret word: "))

while True:
    letter = input("Enter a letter: ")
    finished = game(letter)
    if finished:
        print("Congrats")
        break