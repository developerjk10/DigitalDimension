aminice = True
print(aminice)
print(type(aminice))
if aminice == True:
    print("give Candy")
else:
    print("give test")

experiment = 1
if experiment == 1 and type(aminice)==bool:
    print("give food")
elif experiment == 2:
    print("give stock")
else:
    print("do nothing")