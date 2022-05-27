def main():
    x, y = 150, 100

    # conditional flow uses if, else, elif.........................................
    if x < y:
        result = "x is less than y"
    elif x == y:
        result = "x is the same as y"
    else:
        result = " x is greater than y"
    print(result)
    print()

    # conditional let use like, "a if c else b".....................................

    result = "x is less than y" if x < y else " x is equal or greater than y"
    print(result)
    print()

    # match case makes it east to compare multiple values.............................

    value = "six"
    match value:
        case "one":
            result = 1
        case " two":
            result = 2
        case "three" | "four":
            result = (3, 4)
        case _:
            result = -1
    print(result)
    print()


if __name__ == "__main__":
    main()
