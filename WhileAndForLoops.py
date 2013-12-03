__author__ = 'Pneumatic'

count = 0  # Set count to 0
while count < 9:  # While count is less than nine
    print('The count is:', count)  # Print the count
    count += 1  # add 1 to count after each iteration of the loop
else:  # use of an else statement in a while loop, once the loop is not true it runs the else statement
    print(count, "is not less than 9")
print("Good bye!")

#BELOW CODE EXECUTES AN INFINITE LOOP ONLY UNCOMMENT IF YOU KNOW HOW TO EXIT IT!
# var = 1
# while var == 1:  # This creates an infinite loop because 1 will always equal 1
#    num = input("Enter a number  :")  # set variable num to the user input
#    print("You entered: ", num)  # print the users number
#   Since we never altered the variable var from 1 this will run continuously
# print("Good bye!")
#END OF CODE FOR INFINITE LOOP!

# For iterating_variable in sequence, iterating means repeat until end of sequence
for letter in 'Python':     # For letter(blank variable) in the word Python
    print('Current Letter :', letter)  # Print the current letter,

fruits = ['banana', 'apple', 'mango']  # Create list with 3 fruits in it
for fruit in fruits:  # For fruit(blank variable) in the list fruits
    print('Current fruit :', fruit)  # Prints the current fruit

print("Good bye!")

# Alternative way of iterating through each item
fruits1 = ['banana', 'apple', 'mango']  # Create a list of 3 fruits
for index in range(len(fruits1)):  # range gives us the sequence to iterate over and len() is the length of fruits1
    print('Current fruit :', fruits1[index])  # Prints current fruit by index, index is 0,1,2(banana, apple, mango)

print("Good bye!")

for num in range(10, 20):   # to iterate between 10 to 20
    for i in range(2, num):  # to iterate on the factors of the number
        if num % i == 0:       # if the number modded(gives the remainder of /) is  == to 0 do rest of if statement
            j = num / i           # take the number and divide it by i
            print('%d equals %d * %d' % (num, i, j))  # %d is for formatting integers in string format
            # % (variables) are the placeholders for the %d's first one is num then i then j goes in logical order
            break  # to move to the next number, the #first FOR
    else:                  # else the number isn't divisible by 2 to 20(num is 10-20)
        print(num, 'is a prime number')  # Prints that the number is prime