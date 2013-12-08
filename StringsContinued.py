__author__ = 'Pneumatic'
var2 = "Python programming"
string1 = "hi"
sub = "i"
strs = "this is string example....wow!!! this is really string"
string = "i"
var2.islower()  # returns true if all characters in var2 are lowercase and if there is at least 1 character, else false
var2.isnumeric()  # returns true if var2 is all numeric only works on unicode must predefine variable using u var2=u"92"
var2.isspace()  # returns true if var2 is only spaces and if there is at least 1 character, else false
var2.istitle()  # checks if all characters following non cased-based(letters) characters are uppercase and all other
# case-based characters are not
var2.isupper()  # returns true if all characters in var2 are uppercase if not returns false
sub.join(var2)  # joins the characters in var2 by the defined string in sub will print (piyitihioini.....)
len(var2)  # returns the length of the string
var2.ljust(30, "x")  # returns string left justified parameters(self, width, fillcharacter)
var2.lower()  # returns a copy of the string in all lower case
var2.lstrip()  # returns a copy of the string with all specified or whitespaces trimmed off the beginning. lstrip(char)
var2.rstrip()  # returns a copy of the string with all specified or whitespaces trimmed off the end. rstrip(char)
min(string1)  # returns the lowest ascii value character  !!Google ascii table if confused!!
max(string1)  # returns the highest value ascii character !!Google ascii table if confused!!
strs.rfind(string)  # returns the last index where the specified string is
strs.replace("is", "was")  # replaces the substring is with was (old new, #replaced)
strs.replace("is", "was", 3)  # replaces the substring is with was up to 3 times (old, new, #replaced)
strs.rindex(string)  # returns the last index where the substring string is found, or raises an exception if not found
var2.rjust(20, "v")  # returns string right justified parameters(self, width, fillcharacter)
strs.split()  # returns a list of all the words separated in the string
strs.split(' ', 1)  # returns a list of all the words separated in string a certain number of times(1)
strs.splitlines()  # returns a list of all the lines in string, optionally including the line breaks if num given
strs.startswith('this')  # returns true if strs starts with specified string, also can decided when to start/stop string
strs.strip()  # strips all characters(whitespaces by default) from both sides of string or any character specified in ()
strs.swapcase()  # changes the case-based characters case lower becomes upper and vice versa
strs.title()  # returns a copy of the string in which first characters of all the words are capitalized
strs.upper()  # returns a copy of the string with all upper case letters
strs.zfill(40)  # pads to the left of the string with 0's until the width is reached
strs.isdecimal()  # checks whether the string consists of only decimal characters only on unicode objects
