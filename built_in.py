#demonstrating built-in utility functions


def main():

    # use any() and all() to test sequences for boolean values
    list1 = [1,2,3,4,5,0,9,10,20,4]

    # any evaluates to true (anything except for 0)
    print(any(list1))

    #needs all values to be true (0 is not)
    print(all(list1))

    # min max sum
    print(min(list1))
    print(max(list1))
    print(sum(list1))

if __name__ == '__main__':
    main()