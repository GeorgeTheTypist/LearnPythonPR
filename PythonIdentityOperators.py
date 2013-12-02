__author__ = 'Pneumatic'

a = 20  # set a to 20
b = 20  # set b to 20

if a is b:  # if a is b (both are 20, true) print same identity, else print not same identity
    print("Line 1 - a and b have same identity")
else:
    print("Line 1 - a and b do not have same identity")

if id(a) == id(b):  # if identity of a is equal to identity of b (both 20, true), print same identity, else not same
    print("Line 2 - a and b have same identity")
else:
    print("Line 2 - a and b do not have same identity")

b = 30  # set b to 30
if a is b:  # if a is b (b is 30, a is 20, false) print same identity, else print not same identity
    print("Line 3 - a and b have same identity")
else:
    print("Line 3 - a and b do not have same identity")

if a is not b:  # if a is not b(30 is not same as 20, true) print not same identity, else print same identity
    print("Line 4 - a and b do not have same identity")
else:
    print("Line 4 - a and b have same identity")