__author__ = 'Pneumatic'


def printme(parameters):  # create a function called printme using def
    """This is a doc sting document what this function will do. This prints a passed string into this function"""
    print(parameters)  # prints anything that is stored inside parameters
    return

printme("I'm first call to user defined function printme")  # calls the function printme and stores the string in
printme("I am the second call to user defined function printme")  # the (parameters)


def changeme(mylist):  # create function mylist with arguments of mylist
    """This changes a passed list into this function"""
    mylist.append([1, 2, 3, 4])  # append(add on to the end) [1, 2, 3, 4] to mylist
    print("Values inside the function: ", mylist)  # print the altered values of mylist
    return  # exit out of the function and go back to the outside code


mylist = [10, 20, 30]  # create a new list
changeme(mylist)  # call the function changeme with the arguments of mylist
print("Values outside the function: ", mylist)  # the values stay through the function


def changeme(mylist2):   # create function changeme using parameters mylist2
    """This changes a passed list into this function"""
    mylist2 = [1, 2, 3, 4]  # This would assign new reference in mylist
    print("Values inside the function: ", mylist2)  # print the new value of mylist2
    return

mylist2 = [10, 20, 30]  # create mylist2
changeme(mylist2)  # call changeme function
print("Values outside the function: ", mylist2)  # print values of mylist


# Function definition is here
def printme(name, age):  # create function printme with arguments name and age
    """This prints a passed string into this function"""
    print(name, age)  # print name then age
    return

printme(age=50, name="Thomas")  # since we defined age and name it doesn't have to be in order like in function printme
# if we didn't define them we would have to call printme(name,age). Keyword arguments


def printinfo(name, age=35):  # create function printinfo with arguments name, and age(defualt to 35 if not specified)
    """This prints a passed info into this function"""
    print("Name: ", name)  # print name
    print("Age ", age)  # print age, will print 35 unless specified in the call statement
    return  # exit the function printinfo()

printinfo(age=50, name="miki")  # call printinfo function with arguments age=50 and name = miki
printinfo(name="miki")  # call printinfo function with args of name=miki, default age to 35 as specified in printinfo()


def printinfos(arg1, *vartuple):  # create function printinfos() with arguments arg1, and *vartuple
# * indicates (hold the values of all nonkeyword variable arguments, 70, 60, 50 in this case"
    """This prints a variable passed arguments"""
    print(arg1)  # prints arg1 which is 10
    for var in vartuple:  # assign var to each object in vartuple
        print(var)  # print var will print 70, 60, 50
    return  # exit the function printinfos()

printinfos(10)  # call function printinfos set arg1 to 10  don't need to define vartuple it will be left a nothing
printinfos(70, 60, 50)  # call function print, stores any nonkeyword values (all) to *vartuple

total = lambda arg3, arg4: arg3 + arg4
# Lambdas take any # of args but return 1 value in form of an expression, can't contain commands, multiple expressions
print(total(10, 20))  # print (call lambda total set arg3=10, arg4=20) will return 30
print(total(20, 20))  # print (call lambda total set arg3=20, arg4=20) will return 40


def sums(arg1, arg2):  # create function sums with arguments arg1 and arg2
    """ This docstring doesn't need to be here its only for explaining what is happening """
    totals = arg1 + arg2  # set the variable totals to equal arg1 + arg2
    print("Inside the function : ", totals)  # print the totals
    return totals  # return the variable totals defined as arg1 + arg2

totals = sums(10, 20)  # call function sum with args 10, 20 set totals to whats returned
print("Outside the function : ", totals)   # print the variable totals

totaled = 0  # This is a global variable


def sums1(arg1, arg2):  # define(create) function sums1 with arguments arg1 and arg2
   # Add both the parameters and return them."
    totaled = arg1 + arg2  # Here total is local variable sets variable totaled to equal arg1 + arg2
    print("Inside the function local total : ", totaled)  # print variable totaled which is 30
    return totaled  # return variable totaled

# Now you can call sum function
sums1(10, 20)
print("Outside the function global total : ", totaled)  # prints the variable totaled which is 0