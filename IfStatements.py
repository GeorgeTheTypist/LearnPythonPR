__author__ = 'Pneumatic'

# if variable is 0 or null (no data) python sees it as false
var1 = 100  # set var1 to 100
if var1:  # if var1(true) no comparison being made so always true
    print("1 - Got a true expression value")  # prints true expression value
    print(var1)  # prints var1

var2 = 0  # set var2 to 0
if var2:  # if var2(0) always false since it is 0/null
    print("2 - Got a true expression value")  # doesn't print since it isn't true
    print(var2)  # as long as print() is indented(4 spaces) it is inside the if statement, so this won't get printed
print("Good bye!")  # notice no indenting meaning outside of the if statement, this will get printed