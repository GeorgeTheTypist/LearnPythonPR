__author__ = 'Pneumatic'

diction = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}  # create a new dictionary
diction1 = {'abc': 456}
diction2 = {'abc': 123, 98.6: 37}
seq = 'Name', 'Height', 'Weight'
diction3 = dict.fromkeys(seq)  # create a new dictionary with keys from variable seq, values will be none
# Key:Value so above Alice would be the Key and the value would be 2341, same format for others as well, keys are unique
# They must me immutable (unable to be changed) values can be anything and can be the same inside a dictionary
# Cannot have duplicate keys last key will win "bob", 2, "bob", 3 , bob will be assigned to 3
print("First value in diction", diction['Alice'])  # print the first value in diction by calling the key "alice"
# Can't access values by keys that aren't inside a dictionary, this won't work diction["Bob"]
diction["Thomas"] = 7626  # add a new value of 7626 with a key of Thomas
diction["Beth"] = 9100  # Change the value of Beth to 9100
del diction["Thomas"]  # delete entry with key "Thomas"
diction.clear()  # clear everything inside the dictionary
del diction  # delete the dictionary
diction1 == diction2  # compares diction1 to diction 2
len(diction2)  # returns the length of diction 2 (number of pairs of keys:values)
str(diction1)  # Produces a printable string version of the dictionary
type(diction1)  # returns the type of variable diction1 is (dictionary)
diction2.copy()  # creates a copy of diction2
diction3.values()  # returns the values in diction3
diction2.get("abc", "Key does not exists")  # return value of key abc, if there is no key abc return does not exist
diction1.values()  # returns a list of dic(keys:values) tuple pairs
diction1.keys()  # returns a list of the keys in dictionary diction1
diction1.setdefault("def", None)  # return value of key if there isn't one return the value as none
diction1.update(diction2)  # update the dictionary with the additional keys:values of diction2