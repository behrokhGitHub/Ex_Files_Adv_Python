# use transform functions like sorted, filter, map


def filterFunc(x):
     if x % 2 == 0:
         return True
     else:
         return False


def filterFunc2(x):
    return True if x.isupper() else False


def squareFunc(x):
    return x**2


def toGrade(x):
    if x >= 90:
        return 'A'
    elif 80 <= x < 90:
        return 'B'
    elif 70 <= x < 80:
        return 'C'
    elif 60 <= x < 70:
        return 'D'
    return 'F'


def main():
    # define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # TODO: use filter to remove items from a list
    # filter(function, iterable) 
    odds = list(filter(filterFunc, nums))
    print(odds)
    
    # TODO: use filter on non-numeric sequence
    ch = list(filter(filterFunc2, chars))
    print(ch)

    # TODO: use map to create a new sequence of values
    sq = list(map(squareFunc, nums))
    print(sq)

    # TODO: use sorted and map to change numbers to grades
    grades = sorted(grades)
    newList = list(map(toGrade, grades))
    print(newList)

if __name__ == "__main__":
    main()
