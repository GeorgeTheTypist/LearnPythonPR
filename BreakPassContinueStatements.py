__author__ = 'Pneumatic'

for letter in 'Python':  # Iterate through the word python and print check if letter is "h" stop iterating
    if letter == 'h':  # once letter == h stop iterating o n won't be printed since it is after h
        break
    print('Current Letter :', letter)

var = 10  # set var to 10
while var > 0:  # while var is greater than 10
    print('Current variable value :', var)  # Print the variable
    var -= 1  # set var to var -1 (10 becomes 9...)
    if var == 5:  # If var is 5 stop iterating 4,3,2,1 won't be printed
        break  # if var is 5 will go to the next line which is print("goodbye")

print("Good bye!")

for letter in 'Python':  # iterate through python
    if letter == 'h':  # if letter is h continue the for loop iteration
        continue
    print('Current Letter :', letter)  # will print every letter in python

var = 10  # set var to 10
while var > 0:  # while var is greater than 0
    var -= 1  # set var to  var -1
    if var == 5:  # if var is 5 continue
        continue
    print('Current variable value :', var)  # will print all numbers less than 10 but greater than 0
print("Good bye!")  # outside of any whiles or if statements will print no matter what

for letter in 'Python':  # Iterate through python
    if letter == 'h':  # once letter reaches h
        pass
        print('This is pass block')  # inject this string in between t and h
    print('Current Letter :', letter)

print("Good bye!")