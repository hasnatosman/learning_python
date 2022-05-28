# to know something about the computer and os ..........................

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # print the name of os ............................
    print(os.name)

    # check the item existence or type ...............

    print("Item exists: ", str(path.exists("textfile.txt")))
    print("Item is a file: ", str(path.isfile("textfile.txt")))
    print("Item is a dir: ", str(path.isdir("textfile.txt")))

    # work with file path....................................

    print("Item's path: ", path.realpath("textfile.txt"))
    print("Item's path & name: ", path.split(path.realpath("textfile.txt")))

    # get the modification information ................................

    t = time.ctime(path.getmtime("textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

    # last modified time .................................................

    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("It has been ", td, " since the file modified.")
    print("Or", td.total_seconds(), "seconds")


if __name__ == "__main__":
    main()
