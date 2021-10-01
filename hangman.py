def get_word():
    # word = random.choice(words_list)
    word = "market"
    return word.lower()

# To play game


def play(word):
    word_completion = "_" * len(word)  # _ _ _ _ _
    guessed = False
    guessed_letters = []

    tries = 6
    print("Lets play hangman")
    # This will get the drawing of correct hangman

    print(hangman(tries))

    # This will highlist how many words has been completed
    print(word_completion)
    print("\n")

    # While guess is True and Tries is > 6
    while not guessed and tries > 0:
        print(f"Tries left: {tries}")
        guess = input("Please guess a letter: ").lower()
        # To guess length is 1 and alphabetic
        if len(guess) == 1 and guess.isalpha():
            # If letter is already guessed
            if guess in guessed_letters:
                print("**********************")
                print("You already guessed the letter", guess)
                print()
            # if guess is not in the word
            elif guess not in word:
                print("**********************")
                print(guess, "is not in the word")
                print()
                tries -= 1
                guessed_letters.append(guess)
            # if guess is in the word
            else:
                print("**********************")
                print("good", guess, "is in the word")
                print()
                guessed_letters.append(guess)
                # To change word completion to list
                word_as_list = list(word_completion)
                x = []
                # To get index and letter of the word
                for count, letter in enumerate(word):
                    # If the letter in the wod matches the guess letter append that index of the letter to x[]
                    if letter == guess:
                        x.append(count)
                # the guessed letter will replace the appropriate index
                for index in x:
                    word_as_list[index] = guess
                # To convert list to string
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

        else:
            print("**********************")
            print("Not a valid guess")
            print()
        print(hangman(tries))
        print(word_completion)
        print
        print("\n")
    if guessed:
        print("congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " +
              word + "Maybe next time!")


def hangman(tries):
    if tries == 6:
        print("+|+")
        print("+|+")
        print("+|+")
        print("+|+")
        print("+|+")
    elif tries == 5:
        print("+______________+")
        print("+|+")
        print("+|+")
        print("+|+")
        print("+|+")
        print("+|+")
    elif tries == 4:
        print("+________+")
        print("+|        |")
        print("+|        0")
        print("+|+")
        print("+|+")
        print("+|+")
    elif tries == 3:
        print("+________+")
        print("+|        |")
        print("+|        0")
        print("+|        |")
        print("+|        \ ")
        print("+|+")
    elif tries == 2:
        print("+________+")
        print("+|        |")
        print("+|        0")
        print("+|        |")
        print("+|       / \ ")
        print("+|+")
    elif tries == 1:
        print("+________+")
        print("+|        |")
        print("+|        0")
        print("+|        |")
        print("+|        / \ ")
        print("+|         |")
        print("+|+")
    elif tries == 0:
        print("+________+")
        print("+|        |")
        print("+|        0")
        print("+|        |")
        print("+|        / \\")
        print("+|         |")
        print("+|       /   \\")
        print("+|+")
    return tries


def main():
    word = get_word()
    play(word)
    while input("Play Again? (y/n) ").lower() == "y":
        # Call random word method to get a word
        # word = get_word()
        # Call play method to play the game
        play(word)










if __name__ == "__main__":
    main()