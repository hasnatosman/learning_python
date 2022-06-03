from datetime import date
from datetime import time
from _datetime import datetime


def main():
    # get todays information.........................................
    today = date.today()
    print("Today's date is: ", today)

    # date components
    print("Today is: ", today.day, today.month, today.year)

    # date  time
    now = datetime.now()

    # formatted as string...................................
    print("Time is: ", now)
    print(now.strftime("Year is: %y"))
    print(now.strftime("Day is: %a"))
    print(now.strftime("Month is: %m"))
    print(now.strftime("Month name is: %B"))
    print(now.strftime("Month name is: %b"))


if __name__ == "__main__":
    main()
