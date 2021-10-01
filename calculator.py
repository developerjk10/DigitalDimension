# Simple Calculator
number_one = int(input("Enter your first number: "))
number_two = int(input("Enter your second number: "))
operator = (input("Enter your operator: "))

while True:
    number_one = int(input("Enter your first number: "))
    number_two = int(input("Enter your second number: "))
    operator = (input("Enter your operator: "))

if operator == "+":
    print(number_one + number_two)
elif operator == "-":
    print(number_one - number_two)
elif operator == "/":
    print(number_one / number_two)
elif operator == "*":
    print(number_one * number_two)
elif operator == "%":
    print(number_one % number_two)
else:
    print("Not a valid operator")

