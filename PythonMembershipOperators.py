__author__ = 'Pneumatic'

a = 10  # set variable a to 10
b = 20  # set variable b to 20
listing = [1, 2, 3, 4, 5]  # create list containing numbers 1-5

if a in listing:  # if a(10) is in listing print "is in list" else print "isn't in list"
    print("Line 1 - a is available in the given list")
else:
    print("Line 1 - a is not available in the given list")

if b not in listing:  # if b(20) is not in listing(true) print "isn't in list" else print "is in list"
    print("Line 2 - b is not available in the given list")
else:
    print("Line 2 - b is available in the given list")

a = 2  # set variable a to 2
if a in listing:  # if a(2) is in listing(1-5, true) print "is in list" else print "isn't in list"
    print("Line 3 - a is available in the given list")
else:
    print("Line 3 - a is not available in the given list")