__author__ = 'Pneumatic'

a = 21
b = 10

if a == b:  # Checks if a is the same as b (==)
    print("Line 1 - a is equal to b")
else:
    print("Line 1 - a is not equal to b")

if a != b:  # Checks if a is not the same as b (!=)
    print("Line 3 - a is not equal to b")
else:
    print("Line 3 - a is equal to b")

if a < b:  # Checks if a is less than b (<)
    print("Line 4 - a is less than b")
else:
    print("Line 4 - a is not less than b")

if a > b:  # Checks if a is greater than b (>)
    print("Line 5 - a is greater than b")
else:
    print("Line 5 - a is not greater than b")

a = 5
b = 20
if a <= b:  # Checks if a is less than or equal to b (<=)
    print("Line 6 - a is either less than or equal to  b")
else:
    print("Line 6 - a is neither less than nor equal to  b")

if b >= a:  # Checks if a is greater than or equal to b (>=)
    print("Line 7 - b is either greater than  or equal to b")
else:
    print("Line 7 - b is neither greater than  nor equal to b")