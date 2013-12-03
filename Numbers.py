__author__ = 'Pneumatic'
import random
import math
seq = [1, 2, 3, 4, 5, 6, 7]
q = 2
a = 9  # This is an integer, don't need to worry about max integer size in python it automatically changes to long
b = 12.22  # This is a floating point, notice the decimal
c = 12929120929029393920390390  # This is a long integer
d = 3.14J  # This is a complex number, 3.14 (real), and J(imaginary), complex numbers are rarely used in python
e = -10
x = 22
int(b)  # Converts b to an integer, cutting off the .22
float(c)  # Converts c to a floating point. adding .0 to the end
complex(a)  # Converts a to a complex number with a being the real number and 0 being the imaginary
complex(a, b)  # Converts a and b to a complex number with a being the real number and b being the imaginary
abs(e)  # The absolute value of e: the (positive) distance between e and zero
math.ceil(b)  # The ceiling of x: the smallest integer not less than x (rounds up)
math.exp(a)  # e ** a (** is to the power of) e = 2.71828182846
math.fabs(x)  # returns the absolute value of x
math.floor(b)  # returns floor of x - the largest integer not greater than x (rounds down)
math.log(x)  # returns natural logarithm of x, for x > 0 (x needs to be greater than 0)
math.log10(x)  # returns base-10 logarithm of x for x > 0 (x needs to be greater than 0)
max(x, a, b)  # Returns the highest variable
min(x, a, b)  # Returns the lowest variable
math.modf(b)  # Returns the fractional and whole number in a two item tuple, will return .22 and 12.00
math.pow(x, q)  # Returns x to the power of q
round(b, 1)  # Rounds b to the first decimal place, round((variableORnumber),(decimal place))
math.sqrt(a)  # Returns the square root of a(9) will return 3
random.choice(seq)  # returns a random item from a list, tuple, or string. !!NEED TO IMPORT random!!
random.randrange(q, c, a)  # returns a random element from range(start, stop, step), step is how many times it chooses
random.random()  # returns a random value that is equal to or greater than 0 and is less than 1
random.seed(10)  # sets the integer starting value used in generating random numbers in this case 10
random.shuffle(seq)  # shuffles items in a list or tuple in place
random.uniform(a, x)  # returns a random float r, such that x is less than or equal to r and r is less than y.
math.pi  # returns the value of pi 3.141592653589793
math.e  # returns the value of e 2.718281828459045