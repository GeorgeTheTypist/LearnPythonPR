__author__ = 'Pneumatic'
import os  # import the module os
print("this prints to the screen, it's so easy!")  # prints whatever is type between the (), string need to have ""
userInput = input("Type what you want written to file: ")  # this stores the user input in a variable called userInput

#SYNTAX for opening a file.  file object = open(file_name [, access_mode][, buffering])
#If a file is created it is placed in the same folder as the script it is written in
paras = open("paras.txt", "w")  # open file paras.txt, if doesn't exist create it, assign to a reference variable paras
paras = open("paras.txt", "r")  # opens a file to read from (default value)
paras = open("paras.txt", "rb")  # opens a file for reading only in binary format
paras = open("paras.txt", "r+")  # opens a file for both reading and writing
paras = open("paras.txt", "rb+")  # opens a file for both reading and writing in binary format
paras = open("paras.txt", "wb")  # opens a file for writing only in binary format
paras = open("paras.txt", "w+")  # opens a file for both writing and reading. overwrites current file if exists.
paras = open("paras.txt", "wb+")  # opens a file for reading and writing in binary format.
paras = open("paras.txt", "a")  # opens a file for appending. If file doesn't exists creates it.
paras = open("paras.txt", "ab")  # opens a file for appending in binary format. If file doesn't exist creates it.
paras = open("paras.txt", "a+")  # opens file for both appending and reading. If doesn't exist creates new file for r/w
paras = open("paras.txt", "ab+")  # opens file for both appending and reading in binary format. It doesn't exist creates
paras = open("paras.txt", "w")  # open the file in writing format
paras.closed  # returns true if file is closed, false otherwise
paras.mode  # returns access mode with which file was opened
paras.name  # returns name of file
# paras.close()  # close the connection with the file no more writing or reading can be done after this

fo = open("foo.txt", "wb")
print("Name of the file: ", fo.name)  # prints the name of the file using (reference variable).name
print("Closed or not : ", fo.closed)  # prints true or false based on if the file is open or not
print("Opening mode : ", fo.mode)  # prints the mod the file was opened in (wb, write only in binary format)
paras.write(userInput)
# fileObject.read([count]) count is how much you want read (10) first 10 indexes
accounts = open("C:\\Users\TERRY\Documents\\acc.txt", "r")  # opens the file acc in a readable format
contains = accounts.read(10)  # set variable contains the what is read from accounts(file acc.txt)
# print(contains) prints the information which was read from file acc.txt
position = accounts.tell()  # returns the position the file is at specified as count in original file.read()
accounts.seek(0, 0)  # reposition pointer at the beginning again
# os.rename("clint.txt", "clinton.txt") uses os.rename function in module os to rename a file, file needs to be closed
# os.remove("clinton.txt") removes file specified
# os.mkdir("extra files") creates a new directory called extra files
# os.chdir("/extra files/newdir") changes location of directory
os.getcwd()  # returns the current directory
# os.rmdir("extra files")  # removes the directory specified