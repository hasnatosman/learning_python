# will read and write files................................

def main():
    # creating a new file..................................

    # myfile = open("textfile.txt", "w+")

    #opening a existing file .............................

    # myfile = open("textfile.txt", "a+")

    # write some lines of data ............................

    # for i in range(10):
    #     myfile.write("I love my country & religion.\n")

    # reading an existing files contents ...................

    myfile = open("textfile.txt", "r")

    if myfile.mode == "r":
        contents = myfile.read()
        print(contents)

    # closing newly created file ..........................

    myfile.close()


if __name__ == "__main__":
    main()
