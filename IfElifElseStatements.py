__author__ = 'Pneumatic'

var1 = 100  # set var1 to 100
if var1:  # if var1(true, since it's not null or equal to 0) print both lines since indented meaning inside the if
    print("1 - Got a true expression value")
    print(var1)
else:  # else print these two lines (won't be printed since true)
    print("1 - Got a false expression value")
    print(var1)

var2 = 0  # set var2 to 0 (python sees this as false 0 or null is always false
if var2:  # if var2(false) print two lines below (won't be printed since false)
    print("2 - Got a true expression value")
    print(var2)
else:  # else print the two lines below (since false prints these)
    print("2 - Got a false expression value")
    print(var2)

print("Good bye!")  # outside of if statement will be printed no matter what

var = 100  # set var to 100
if var == 200:  # if var is equal to (200, false 100 is not 200) print two lines below
    print("1 - Got a true expression value")
    print(var)
elif var == 150:  # else if(elif) var is equal to (150, false 100 is not 150) print two lines below
    print("2 - Got a true expression value")
    print(var)
elif var == 100:  # else if(elif( var is eqaul to (100, true 100 is 100) print two lines below
    print("3 - Got a true expression value")
    print(var)
else:  # else (all preceding lines (if, elif, elif) are false print two lines below
    print("4 - Got a false expression value")
    print(var)

print("Good bye!")  # outisde of if statement will be printed no matter what