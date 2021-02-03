#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:35:08 2021

@author: behrokh
"""
import collections

def isprime(n):
    return n% 2 == 0

def squarenum(n):
    return n**2

def main():
    # list of students in class 1
    class1 = ["Bob", "Becky", "Chad", "Darcy", "Frank", "Hannah"
              "Kevin", "James", "James", "Melanie", "Penny", "Steve"]

    # list of students in class 2
    class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
              "Gabby", "Kelly", None, "Joe", "Sam", "Tara", "Ziggy"]

    print(any(class1))
    
    # None or "" means empty or null string
    print(all(class2))

    # Iterators
    # Iter
    it = iter(class1)
    print(next(it))
    print(next(it))
    print(next(it))
    
    # using enumarate
    for num, student in enumerate(class1, start=1):
        print(num, student)
        
    # using enumerate, returning a tuple
    for item in enumerate(class1, start=1):
        print(item)
      
    print()
    print("using zip")
    # using zip; The function takes in iterables as arguments and returns 
    # an iterator. This iterator generates a series of tuples containing 
    # elements from each iterable
    for i in zip(class1, class2):
        print(i)
    
    print()
    print("filter")
    # filter function receives a function, and a iterable; 
    l = [1,2,3,4,5,6,76,8,9,10, 11]
    l = list(filter(isprime, l))
    print(l)
    
    print()
    print("using map")
    l = list(map(squarenum, l))
    print(l)
    
    print()
    print("Advanced Collections")
    print('using namedtuple')
    Employee = collections.namedtuple('Employee', 'name city age')
    e1 = Employee('John', 'San Diego', 42)
    print(e1)
    
    l = ['Sally', 'Los Angles', 45]
    e2 = Employee._make(l)
    print(e2)
    
    print()
    print('usingdefaultdict')
    fruitslist=['apple', 'orange', 'apple', 'grape', 'orange', 'banana', 'berry', 'orange', 'pear', 'banana']
    d = collections.defaultdict(int)
    for i in fruitslist:
        d[i] += 1
    
    for k, v in d.items():
        print(k, ',', str(v))
        
    # how to sort a dictionary based on its values      
    d = {k:v for k, v in sorted(d.items(), key=lambda item:item[1],reverse= True)}
    l = list({k:v for k, v in sorted(d.items(), key=lambda item:item[1],reverse= True)})
    print(d)
    print(l)
    
    
    
if __name__ == "__main__":
    main()
