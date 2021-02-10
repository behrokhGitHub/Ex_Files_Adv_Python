# Use lambdas as in-place functions


def CelsisusToFahrenheit(temp):
    return (temp * 9/5) + 32


def FahrenheitToCelsisus(temp):
    return (temp-32) * 5/9

def firstfunc(n):
        return lambda a : a * n
    
def main():
    ctemps = [0, 12, 34, 100]
    ftemps = [32, 65, 100, 212]

    # TODO: Use regular functions to convert temps
    print(list(map(CelsisusToFahrenheit, ctemps)))
    print(list(map(FahrenheitToCelsisus, ftemps)))
    
    # TODO: Use lambdas to accomplish the same thing
    print(list(map(lambda t: (t * 9/5) + 32, ctemps)))
    print(list(map(lambda t: (t-32) * 5/9, ftemps)))

    x = lambda a : a + 10
    print(x(5))
    x = lambda a, b: a + + b + 10
    print(x(5, 6))
    x = lambda a, b, c : a + + b + c + 10
    print(x(5, 6, 7))
    
    first = firstfunc(5)
    print(first(5))
    
    
    

































if __name__ == "__main__":
    main()
