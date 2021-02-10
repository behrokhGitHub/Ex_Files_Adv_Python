# Demonstrate the use of variable argument lists


# TODO: define a function that takes variable arguments
def addition(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


def main():
    # TODO: pass different arguments
    print(addition(1, 2, 3, 4, 5, 6, 7, 8, 9))

    # TODO: pass an existing list
    myList = [1,3,5,7,9]
    print(addition(*myList))

if __name__ == "__main__":
    main()
