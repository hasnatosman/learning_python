def main():
    x = 0

    # while loop.....................................

    while x < 5:
        print(x)
        x = x + 1
    print()

    # for loop........................................

    for i in range(1, 10, 2):
        print(i)
    print()

    # for loop in collection..........................

    days = ['Sat', 'Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri']

    for day in days:
        print(day)
    print()

    # using break......................................
    for i in range(1, 5):
        if i == 4:
            break
        print(i)
    print()

    # using continue..................................
    for i in range(1, 8):
        if i == 4:
            continue
        print(i)
    print()

    # using enumerate in for loop..............................

    days = ['Sat', 'Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri']

    for i,day in enumerate(days):
        print(i, day)
    print('.............Done.......')


if __name__ == "__main__":
    main()
