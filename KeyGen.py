__author__ = 'Pneumatic'

import string  # import all the needs modules
import random
import sys
import os

print("enter the name of the file to hold all the keys:")  # ask user to name file
filename = input("Name Of File ::")  # assign variable filename to the answer user gives
# stdout is used for the output of print and expression statements and for the prompts of input()
temp = sys.stdout  # assign variable temp to sys.stdout in the import sys module
# EOF = End Of File!
sys.stdout = open(filename, 'a')  # assign sys.stdout as a reference to open file in append mode (pointer is at EOF)
print("Do Not Edit")  #
sys.stdout.close()  # close the connection to the opened file
sys.stdout = temp  # assign variable sys.stdout to equal temp (reassigning sys.stdout to itself)
data = open(filename, 'r')  # assign variable data to open the file in reading mode
lines = data.readlines()  # set variable lines to equal the readable lines in the file using reference variable data
data.close()  # close the connection to the opened file


data = open(filename, 'w')  # open a file with writing permissions. Reference variable "data"
print("Generating random keys from uppercase")  # Give directions to user
print("and lowercase with numbers...")
print("Please close terminal with the x button")
print("top right of terminal as this is on a loop.")
print("\n \n WARNING may generate the same key twice WARNING \n")
t = input("Enter char length :")  # Get the length of the keys to generate and assign to variable t
a = int(t)  # change the data type from string to integer storing it in variable a
input("If You Wish To Continue Press Any Key.....")  # ask the user if they do want to generate keys

print("\n \n \n Generating........")  # Give the user some notification that the script is working
k = 3  # assign variable k to equal 3
x = 1  # assign variable x to equal 1
clear = 1000000  # assign variable clear to equal 1 million (1000000)

while x:  # while x is true (1 is always true 0 is always false) do the below statements
    def lower(size=a, chars=string.ascii_lowercase + string.digits):
    # create function with parameters of size (user choice), chars (lowercase a-z) and string 0123456789
        return ''.join(random.choice(chars) for x in range(size))
    # return joined random choices from lowercase characters and digits while(for) x is in range of size(user choice)

    def upper(size=a, chars=string.ascii_uppercase + string.digits):
    # create function with parameters of size (user choice), chars (uppercase a-z and string 0123456789)
        return ''.join(random.choice(chars) for x in range(size))
    # return joined random choices from uppercase characters and digits while(for) x is in range of size(user choice)

    def characters(size=a, chars=string.ascii_uppercase+string.ascii_lowercase + string.digits):
    # create a function with parameters of size (user choice), chars(uppercase, lowercase and digits)
        return ''.join(random.choice(chars) for x in range(size))
    # return joined random choices from uppercase, lowercase and digits while(for) x is in range of size(user choice)
    lines[0] = lower()+"\n"+upper()+"\n"+characters()+"\n"
    # Go to first index in lines (lines was the read lines from the file) and set it to call those functions
    data.writelines(lines)
    # write the lines in the parenthesis in this case random characters from the functions upper(), lower(), and chars()
    v = 3 * x  # set v to equal 3 times x
    tim = x  # set tim to x
    mb = os.path.getsize(filename)  # assign variable mb to equal the filesize of the file using os.path.getsize()
    Fsize = ""  # assign Fsize to a blank string statement

    if tim == clear:  # if tim equals clear (1 million) run the below code

        if mb >= 1048576:  # if mb is greater than or equal to 1048576(1.048m)
            mb /= 1048576  # assign mb to mb/1048576
            Fsize = " MB's"  # set Fsize to " MB's" (Megabytes)
        elif mb >= 1073741824:  # else if mb is greater than 1073741824(1.073b)
            mb /= 1073741824  # assign mb to mb/1073741824
            Fsize = " GB's"  # assign Fsize to " GB's" (Gigabytes)
        elif mb >= 1099511627776:  # else if mb is greater than or equal 1099511627776 (1.099T)
            mb /= 1099511627776  # assign mb to mb/1099511627776
            Fsize = " TB's"  # assign Fsize to "TB's" (Terabytes)
    print("Processed Keys:: "+str(v)+"      "+"File Size ::"+str(mb)+Fsize)
    # print the number of generated keys and the size of the file
    clear += 1000000  # assign clear to clear + 1000000
    mb = mb  # assign mb to mb

    x += 1  # assign x to x + 1