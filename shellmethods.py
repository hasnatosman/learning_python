# will do some fun on shell method..............................

import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile


def main():
    # make a duplicate of existing file........................

    if path.exists("textfile.txt"):
        # get the path to current directory............................

        src = path.realpath("textfile.txt")

        # let's make a backup file ...................................

        # dst = src + ".bak"
        # shutil.copy(src, dst)

        # rename the file ..........................................

        os.rename("textfile.txt", "newfile.txt")

# now put things into zip archive .................................


if path.exists("textfile.txt.bak"):
    src = path.realpath("textfile.txt.bak")

    root_dir, tail = path.split(src)
    shutil.make_archive("archive", "zip", root_dir)

    # more control over zip file ..............something went wrong...................
    
    # with ZipFile("testzip.zip", "w") as newzip:
    #     newzip.write("textfile.txt")


if __name__ == "__main__":
    main()
