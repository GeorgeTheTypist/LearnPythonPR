__author__ = 'Pneumatic'

try:  # try these two lines of code to see if they work
    fh = open("testfile", "w")  # create a reference variable for the opened file testfile, and "w" (writing privileges)
    fh.write("This is my test file for exception handling!!")  # write to the file the string
except IOError:  # if there is IOError(Input/Output) print the below statement telling why it didn't work
    print("Error: can\'t find file or read data")  # the / is an escape character so ' is processed as a ' not a quote
else:  # if they work then type written successfully and close the file connection
    print("Written content in the file successfully")
    fh.close()  # close the file in reference variable fh (testfile)

try:  # try these two lines of code to see if they work
    fh = open("testfile", "r")  # open a file for "r" (read only mode)
    fh.write("This is my test file for exception handling!!")  # since we used r to read the file we can't write to it
except IOError:  # this will be executed because there was an IOError(Input/Output)
    print("Error: can\'t find file or read data")  # print this because there was an IOError(Input/Output)
else:
    print("Written content in the file successfully")  # if there is no error in the try block then run this

try:  # try the below statements
    fh = open("testfile", "r")  # open a file in read only mode
    try:
        fh.write("This is my test file for exception handling!!")  # try to write to the file
    finally:  # this will be ran no matter what even if there is an error
        print("Going to close the file")  # prints this first before the exception if there is one
        fh.close()  # close the file
except IOError:  # if there is an error in the try statement print the exception
    print("Error: can\'t find file or read data")


def temp_convert(var):  # create a function called temp_convert using 1 argument called var
    try:
        return int(var)  # try to return cast (change) var to an integer and return the result
    except ValueError:
        print("The argument does not contain numbers:", var)  # since xyz can't change to an integer this is printed


temp_convert("xyz")  # call the function using xyz as the argument for variable var


def levels(level):
    if level < 1:
        raise("Invalid level!", level)
      # The code below to this would not be executed
      # if we raise the exception
      # levels(0) will be ran as it is what calls this function without it this function wouldn't run
levels(0)  # call the function levels using 0 as the level argument