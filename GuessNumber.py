answer = 5

while True:

    try:
        user_answer = int(input("Enter a number between 1 to 5: "))
        # if user_answer.isalpha():
        #     print("Your entry is wrong. Please enter a numeric value")
        #     user_answer = input("Enter a number between 1 to 5: ")
        # if int(user_answer) == answer:
        if user_answer == answer:
            # print(f"Correct Guess: {answer}")
            # print("Well Done, Game Over")
            break
        else:
            print(f"Wrong Guess: {user_answer}")
            print("ReTry")
    except ValueError:
        print("Your entry is wrong. Please enter a numeric value")


print(f"Correct Guess: {answer}")
print("Well Done, Game Over")

