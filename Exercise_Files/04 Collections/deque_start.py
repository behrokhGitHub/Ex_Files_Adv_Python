# deque objects are like double-ended queues

import collections 
import string


def main():
    
    # TODO: initialize a deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)

    # TODO: deques support the len() function
    print(len(d))
    
    # TODO: deques can be iterated over
    for c in d:
        print(c, end=',')
    print()

    # TODO: manipulate items from either end
    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(1)
    print(d)
    print()
    
    # TODO: rotate the deque
    d.rotate(10)
    print(d)

if __name__ == "__main__":
    main()
