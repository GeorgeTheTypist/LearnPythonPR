__author__ = 'Pneumatic'

list1 = ['physics', 'chemistry', 1997, 2000]  # create list using []
list2 = [1, 2, 3, 4, 5]  # create list using []
list3 = ["a", "b", "c", "d"]  # create list using []
list4 = ["hello", "Hello", "HELLO"]
aTuple = (1, 2, 3, 33, 4, 5, "six")  # create a tuple
aList = list(aTuple)  # create a new list by converting a tuple
bList = [8, "nine"]  # create a new list
list2[2] = 6  # replaces the second index in list2 with 6
aList.append("seven")  # append (add to the end) seven to the list aList
del list2[4]  # deletes the fourth index in list2
print("list1[0]: ", list1[0])  # prints first item in list1, in programming it starts at 0,1,2,3 so physics is 0
print("list2[1:5]: ", list2[1:5])  # prints the second to the sixth item in list2
print(len(list1))  # prints length of list1
print(list1 + list2)  # using the concatenation symbol + combine the two lists
print(list1*2)  # repeats the list twice
print(1 in list2)  # true of false depending on if 1 is in list2 or not
for i in list1:  # iterate through list1 using i and printing each value
    print(i)  # prints whatever i is (all of list1)
print(list4[0])  # prints first index in list4
print(list4[-2])  # counts from the end
print(list4[1:])  # print indexes 1-end
print(list4 == list2)  # compares to see if the lists are the same
max(list2)  # returns the max value in list2
min(list2)  # returns the min value in list2
print(aList)
aList.count(3)  # counts the number of times 3 shows up in list
aList.extend(bList)  # add onto the end of aList the contents of bList !Cannot use inside of print statement
print(aList)
aList.index(2)  # returns the index of 2 in aList(will return 1)
aList.insert(2, "hello")  # inserts hello at the given index (2)  !Cannot use inside of print statement
print(aList)
print(aList.pop(2))  # removes and returns the last object(default) or object specified
aList.remove(1)  # removes the first object specified from the list
aList.reverse()  # reverses the items in the list !Cannot use inside of print statement
# aList.sort()  sorts the list use a function if given must be same type of variable (string, int, float)