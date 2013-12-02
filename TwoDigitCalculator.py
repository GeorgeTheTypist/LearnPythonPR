__author__ = 'Pneumatic'

x = input("Input number 1")  # Ask user for first number
y = input("Input number 2")  # Ask user for second number
b = int(x)  # cast the answer to an integer
c = int(y)  # cast the answer to an integer
answer = 0  # create an answer variable to hold the answer
equation = input("Multiply? /? Add? Subtract?")  # ask what equation they want performed

if equation == "Add":  # if users enters add, set answer to b+c

    answer = b+c
elif equation == "/":  # elif(else if) user enters division, set answer to b/c
    answer = b/c
elif equation == "Multiply":  # elif user enters Multiply, set answer to b*c
    answer = b*c
else:  # else, set answer to b-c
        answer = b-c

print(answer)
