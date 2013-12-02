__author__ = 'Pneumatic'
# Main difference between lists and tuples is tuples cannot be altered (ie. read only)
tuples = ('abcd', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')
tuple2 = ('abcd', 786, 2.23, 'john', 70.2)
lists = ['abcd', 786, 2.23, 'john', 70.2]
diction = {}
diction['one'] = "This is one"
diction[2] = "This is two"
tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}  # Syntax (key : value)

print(diction['one'])         # Prints value for 'one' key
print(diction[2])             # Prints value for 2 key
print(tinydict)            # Prints complete dictionary
print(tinydict.keys())     # Prints all the keys
print(tinydict.values())   # Prints all the values
                           # tuple[2] = 1000 Invalid syntax to change the tuple (cannot be altered!)
lists[2] = 1000            # Valid syntax to change the list
print(tuples)              # Prints complete list
print(tuples[0])           # Prints first element of the list
print(tuples[1:3])         # Prints elements starting from 2nd till 3rd
print(tuples[2:])          # Prints elements starting from 3rd element
print(tinytuple * 2)       # Prints list two times
print(tuples + tinytuple)  # Prints concatenated lists
print(lists)