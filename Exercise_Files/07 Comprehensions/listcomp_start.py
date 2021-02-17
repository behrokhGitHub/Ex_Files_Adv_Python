# Demonstrate how to use list comprehensions


def main():
    # define two lists of numbers
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # TODO: Perform a mapping and filter function on a list
    evensquared = list(map(lambda e: e**2, evens))
    print(evensquared)
    
    evensquared = list(
        map(lambda e: e**2, filter(lambda e: e> 4 and e<16, evens)))
    print(evensquared)
    
    # TODO: Derive a new list of numbers frm a given list
    evensquared =[e**2 for e in evens]
    print(evensquared)
    
    # TODO: Limit the items operated on with a predicate condition
    oddsquared =[e**2 for e in odds if e >4 and e<16]
    print(oddsquared)

if __name__ == "__main__":
    main()
