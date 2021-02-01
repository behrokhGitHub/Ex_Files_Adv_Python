# Demonstrate the usage of namdtuple objects

import collections


def main():
    # TODO: create a Point namedtuple
    Point = collections.namedtuple('point', 'x y')
    p1 = Point(10,20)
    p2 = Point(30,40)
    print(p1)
    print(p2)

    # TODO: use _replace to create a new instance
    p1 = p1._replace(x=100)
    print(p1)
    

if __name__ == "__main__":
    main()
