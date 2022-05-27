#  declare a basic function..................................

def func1():
    print('I am a Function')


# func1()
# print(func1())
# print(func1)


# function that takes arguments...............................

def func2(arg1, arg2):
    print(arg1, " ", arg2)


func2(10, 20)
print(func2(30, 40))
print()


# function that returns value....................................

def cube(x):
    return x * x * x


print(cube(3))
print()


# function takes default value...................................

def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result


print(power(2))
print(power(2, 3))
print(power(x=3, num=2))
print()
print()


# function with variable number of arguments .........................

def multi_add(*args):
    result = 0
    for i in args:
        result = result + i
    return result


print(multi_add(2, 3, 4))
