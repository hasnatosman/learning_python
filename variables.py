# basic data types in python

myint = 25
myfloat = 25.50
mystr = " Hasnat"
mybool = True
mylist = [0, 1, "two", 3.5, False, 10, 9, 110]
mytuple = (2, 5, 9)
mydict = {'name': 'kazi', 'age': 29}

# print(myint)
# print(myfloat)
# print(mystr)
# print(mybool)
# print(mylist)
# print(mytuple)
# print(mydict)

# re-declaring a variable works
# myint = 'twenty Five'
# print(myint)

# to access a member of sequence type, use []..................
print(mylist[2])
print(mytuple[1])
print(mylist[1:8:2])

# to reverse the sequence.......................
print(mylist[::-1])

# to access in dict, need to call by keys.....................
print(mydict['name'])
print(mydict['age'])

# variable to different types can not be combined.............

print('My age is ' + str(26))
print('My age is', 26)


# global vs local variable........................

def someFunction():
    # global mystr
    mystr = " Khaled"
    print(mystr)


someFunction()
print(mystr)
