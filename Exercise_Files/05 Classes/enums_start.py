# define enumerations using the Enum base class

from enum import Enum, unique, auto

@unique
class Fruit(Enum):
    APPLE = 1
    ORANGE = 2
    BANANA = 3
    KIWI = 4
    PEAR = auto()
    
    
def main():
    pass
    # TODO: enums have human-readable values and types
    # Fruit.APPLE
    print(Fruit.APPLE)
    # <enum 'Fruit'>
    print(type(Fruit.APPLE))
    # <Fruit.APPLE: 1>
    print(repr(Fruit.APPLE))
    
    # TODO: enums have name and value properties
    # output APPLE 1
    print(Fruit.APPLE.name, Fruit.APPLE.value)
    
    # TODO: print the auto-generated value
    # output 5
    print(Fruit.PEAR.value)
    
    # TODO: enums are hashable - can be used as keys
    # output Andrew Ng Class
    myFruit = {}
    myFruit[Fruit.APPLE] = "Andrew Ng Class"
    print(myFruit[Fruit.APPLE])

if __name__ == "__main__":
    main()
