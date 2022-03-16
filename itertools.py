# advanced iteration functions in the itertools package

import itertools

from numpy import average

def testFunction(x):
    return x < 40

def main():
    #
    pass
    # cycle iterator can be used to cycle over a collection
    seq1 = ['Dries', 'Andrew', 'Arnie', 'Galam', 'Ken Lee', 'Kristopher', 'Kearny']
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))

    # use count to create a simple counter
    count1 = itertools.count(100, 10)
    print(next(count1))
    print(next(count1))
    print(next(count1))

    # accumulate creates an iterator that accumuluates values
    vals = [10,20,30,40,50,60,70,80,90,10,20]
    acc = itertools.accumulate(vals)
    print(list(acc))

    # use chain to connect sequences together
    x = itertools.chain("ABCD", "1234")
    print(set(x))

    # dropwhile and takewhile will return values intill a
    # condition is met
    print(list(itertools.dropwhile(testFunction, vals)))
    print(list(itertools.takewhile(testFunction, vals)))

if __name__ == '__main__':
    main()