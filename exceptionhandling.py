# how to handle exception error..........................

try:
    x = 10 / 0

except:
    print(' That will not give any output !')


# handle different way.................................

try:
    num = int(input("Input a number : "))
    print("Result is: ", 10/ num)

except ZeroDivisionError as e:
    print('You can not divide by zero!')

except ValueError as e:
    print('You did not give a valid number !')
    print(e)

finally:
    print('This code always run !')
