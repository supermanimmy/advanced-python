# using transform functions like sorted, filter, map

def filterFunc(x):
    # Returns True if it's an odd number
    if x % 2 == 0:
        return False
    return True

def filterFunc2(x):
    # Returns True if char is lower case, use islower for uppercase
    if x.isupper():
        return False
    return True

def squareFunc(x):
    return x**2

def toGrade(x):
    if x >= 90:
        return "A"
    elif (x >= 80):
        return "B"
    elif (x >= 70):
        return "C"
    elif (x >= 60):
        return "D"
    else:
        return "F"


def main():
    #sample sequence to operate on
    nums = (1,2,5,80,3500, 40, 343, 301)
    chars = "abecedefiksdSDKDPSDN"
    grades = (81, 98, 100, 50, 25, 37, 10)
    
    # using filter to remove items from a lsit
    odds = list(filter(filterFunc, nums))
    print(odds)

    # using filter on non-numeric sequence
    lowers = list(filter(filterFunc2, chars))
    print(lowers)

    # using map to create a new sequence of values
    squarres = list(map(squareFunc, nums))
    print(squarres)

    # use sorted and map to change numbers to grade
    grades = sorted(grades)
    letters = list(map(toGrade, grades))
    print(letters)

if __name__ == '__main__':
    main()