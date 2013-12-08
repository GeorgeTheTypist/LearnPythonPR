__author__ = 'Pneumatic'
paragraph = """This is a long string made up of several lines the triple quotes allow for things
like newlines to be printed without the need for the escape character and tabs as well"""
var1 = 'Hello Python World!'
var2 = "Python Programming"
string1 = "hi"
sub = "i"
intab = "abcde"  # create a new string containing characters
outtab = "12345"  # create a translation for abcde to be replaced with 12345
trantab = str.maketrans(intab, outtab)  # create a new translation table using maketrans(default, translated)
print(var2.translate(trantab, "yt"))  # translate var2 using trantab, delete characters yt
print("var1[0]: ", var1[0])  # Prints the first(0) character in var1 which is H (in programming they start at 0)
print("var2[1:5]: ", var2[1:5])  # Prints the first to the fifth character in var2
print("Updated String "+var1[:6]+'Python')  # prints var1 till 5th place then replaces from the sixth onward "python"
print("Concatenation" + " is combining strings together," + " pythons concatenation symbol is +")
print("To create new lines in a string\nyou can use \ n (no spaces) ")
print("To\t display hitting tab type \ t (no spaces)")
print("hello" * 6)  # "string" * (number) repeats string by number given "hello" * 2 will result in hellohello
print("H" in "hello")  # checks to see if "H" is in "Hello returns true or false if it is or isn't in the variable
print("a" not in var1)  # checks if "a" is not in var1 returns true or false if it isn't in or is in the variable
print(r"\n")  # r suppresses escape characters will print \n instead of a new line
print("String format %s is a percent %s " % ("operator", "sign"))  # %s calls strings after % in order
print("There are %d and %c also %f as well as %e" % (12, "a", 2.122, 9**2))
# %d is for integers, %c is for characters, %f is for floating point numbers, and %e is for exponential notation
print(paragraph)
string1.capitalize()  # capitalizes the first letter in the string
string1.center(20, "a")  # centers the text. parameters are (length of string, "filler character")
string1.count(sub, 0, 2)  # counts the number of times the substring( sub variable, i) is in the variable string1
string1.endswith(sub)  # checks to see if string ends in a specific suffix arguments are (suffix, start, end)
var2.find(var1)  # returns the index at which var2 is in variable 1 else returns -1 (variable, start, end)
 # var2.index(var1) returns the index at which var2 is in variable 1 else returns an error (variable, start, end)
var2.isalnum()  # returns true if var2 has numbers in it else returns false
var2.isalpha()  # returns true if var2 consists of alphabetic characters only else returns false
var2.isdigit()  # returns true if all characters in var2 are digits and at least one character, if not false

