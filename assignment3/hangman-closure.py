#Task_4: Closure Practice

def make_hangman(secret_word):
    guesses = []
    attempts = 0

    def hangman_closure(letter):
        nonlocal attempts
        if not letter.isalpha() or len(letter) != 1:
            print("Please enter a single letter.")
            return False
        
        if letter in guesses:
            print(f"You already guessed '{letter}'")
            return False

        guesses.append(letter)
        attempts += 1

        result = ""
        for i in secret_word:
            if i in guesses:
                result += i
            else:
                result += "_"
        print(result)
        print(f"Guessed letters: {guesses}")
        print(f"Attempts: {attempts}")

        if "_" not in result:
            print(f"The word was: {secret_word}".lower())
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