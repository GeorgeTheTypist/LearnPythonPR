__author__ = 'Pneumatic'

a = 21
b = 10
c = 0

c = a + b
print("Line 1 - Value of c is ", c)  # c = a + b will assign value of a + b into c
c += a
print("Line 2 - Value of c is ", c)  # c += a is equivalent to c = c + a
c *= a
print("Line 3 - Value of c is ", c)  # c *= a is equivalent to c = c * a
c /= a
print("Line 4 - Value of c is ", c)  # c /= a is equivalent to c = c / a

c = 2
c %= a
print("Line 5 - Value of c is ", c)  # c %= a is equivalent to c = c % a, since 2 can't be divided by 21, just prints 2
c **= a
print("Line 6 - Value of c is ", c)  # c **= a is equivalent to c = c ** a
c //= a
print("Line 7 - Value of c is ", c)  # c //= a is equivalent to c = c // a
