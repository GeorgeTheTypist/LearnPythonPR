__author__ = 'Pneumatic'

decision = "y"
while decision == "y":

    x = input("Please enter a number: ")
    y = input("Please enter a second number: ")
    t = int(x)
    u = int(y)
    choice = input("Multiplication, Division, Addition, Subtraction? ")
    if choice == "Multiplication":
        answer = t * u
        print(x, "times", y, "is", answer)
    elif choice == "Division":
        answer = t / u
        print(x, "divided by", y, "is", answer)
    elif choice == "Subtraction":
        answer = t - u
        print(x, "minus", y, "is", answer)
    else:
        answer = t + u
        print(x, "plus", y, "is", answer)
    decision = input("Do you wish to continue? y/n?")