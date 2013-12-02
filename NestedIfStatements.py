__author__ = 'Pneumatic'

var = 100  # set var to 100
if var < 200:  # check if var is less than 200
    print("Expression value is less than 200")  # print "is less than 200"
    if var == 150:  # no check if var is equal to 150 (false, go to next decision)
        print("Which is 150")
    elif var == 100:  # else if(elif) var is equal to 100 (true) print "is 100"
        print("Which is 100")
    elif var == 50:  # this decision won't be ran because the previous decision returned true
        print("Which is 50")
elif var < 50:  # else if(elif) from the first if asking if var is less than 200, is no asking if var is less than 50
    print("Expression value is less than 50")
else:  # if none of the above statements are true print "could not find true expression"
    print("Could not find true expression")

print("Good bye!")  # outside of if statements will be printed no matter what