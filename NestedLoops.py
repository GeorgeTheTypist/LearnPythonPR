__author__ = 'Pneumatic'

# for iterating_var in sequence: :for loop 1
#   for iterating_var in sequence:  :for loop 2
#      statements(s)  :statements of for loop 2
#   statements(s) :statements of for loop 1
#------------------------------------------------
# while expression : While loop 1
#   while expression : While loop 2
#        statements(s) : statements for while loop 2
#   statements(s) : statements for while loop 1

i = 2  # set i to 2
while i < 100:  # while i is less than 100 do the below statements (this program will run until it reaches 99)
    j = 2  # set j to 2
    while j <= (i/j):  # while j is less than or equal to i/j do the if not statement and set j to j+1
        if not(i % j):  # NOT switches logical states true(has remainder) becomes false(no remainder)
# If there is a remainder(true becomes false) don't run break instead go to the if j>i/j statement
# IF there is no remainder(false becomes true) run the break to go to next line setting j to j+1
            break  # only runs if there is no remainder(even number) stop executing code go to next line j+=1 (j = j+1)
        j += 1  # set j to j+1 only if j is less than or equal to i/j
    if j > i/j:  # if j is greater than i/j
        print(i, " is prime")  # print i "is prime
    i += 1  # set i to i+1, continues to run the code until i is not less than 100 then we print goodbye

print("Good bye!")