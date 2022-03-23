# demonstrating how to use list comprehensions

def main():
    #define two lists of numbers
    evens = [2, 4, 6, 8, 10, 12, 14, 16]
    odds = [1, 3, 5, 7, 9, 11, 13, 15]

    # creating squares with filter function using lambda and map
    evenSquared = list(
        map(lambda e: e**2,
        filter(lambda e: e > 4 and e < 10, evens)))

    # using list comprehension to create a list of squared even numbers
    evenSquared2 = [e**2 for e in evens if e > 4 and e < 10]
    print(evenSquared2)

    # Limit items operated on with a predicate condition
    oddSquared = [e ** 2 for e in odds if e > 3 and e < 15 ]
    print(oddSquared)



if __name__ == '__main__':
    main()