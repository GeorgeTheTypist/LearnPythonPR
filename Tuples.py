__author__ = 'Pneumatic'
# tuples are  like lists except they can't be altered(can't change the information in them)
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"  # any set of multiple objects separated by commas with no identifying symbols {}[] are tuples
tup4 = (50,)  # to create a one item tuple you must follow the character/s with a comma
aList = [1, 2, 3, 4]  # create a list
aTuple = tuple(aList)  # convert aList to a tuple and assign it to aTuple variable
D = ("hello", "Hello", "HELLO")
print("tup1[0]: ", tup1[0])  # prints the first index in tup1(physics)
print("tup2[1:5]: ", tup2[1:5])  # prints the second index to the fifth(2,3,4,5)
# tup1[0] = 100 is not valid for tuples !!They can't be altered/changed however you can combine two tuples or more
tup5 = tup1 + tup2  # create new tuple that is a combination of tup1 and tup2
print(tup5)
del tup4  # cannot delete individual tuple elements like in lists. This deletes the entire tuple
len(tup1)  # returns the amount of objects in the tuple
tup1 + tup2  # combine tup1 with tup2
[tup1] * 2  # repeat tup1 twice
"chemistry" in tup1  # checks to see if "chemistry" is in tup1 if returns true
for x in tup2:  # iterate (assign x) to each value in tup2
    print(x)  # print each value
print(D[2])  # returns the second index of tuple D(HELLO)
print(D[-2])  # returns the second counting from the end of tuple D(Hello)
print(D[1:])  # returns from the first index(Hello) till the end
tup1 == tup2  # compares tup1 to tup2, returns true if they are the same false if they aren't
max(tup2)  # returns the max value of tup2
min(tup2)  # returns the min value of tup2

