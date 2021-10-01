

vowels = ["a", "e", "i", "o", "u"]
# To tak user input
user_input = input("Enter a word: ")
# To store a new word
new_message = ""
# This loops each letter from user entered word
for letter in user_input:
    # Condition to check does the letter is in vowels array
    if letter not in vowels:
        # add the letter not a vowel inside new message
        new_message += letter
print(new_message)
