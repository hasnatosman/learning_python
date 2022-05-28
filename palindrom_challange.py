# palindrome challenge....................................
# any number or string you take in input, it must be same if we revers............

def is_palindrome(teststr):
    # use the slice trick to reverse the sting............................
    if teststr == teststr[::-1]:
        return True
    return False


run = True
while (run):
    teststr = input("Input string to test palindrome or 'exit': " )

    # if user type exit then quit the program................................

    if teststr == 'exit':
        run = False
        break

    # convert all string to lower case......................................

    teststr = teststr.lower()

    # strip all the spaces & punctuation from the string....................

    newstr = ""
    for x in teststr:
        if x.isalnum():
            newstr += x

    print('Palindrome test: ', is_palindrome(newstr))