# demonstrating the usage of defaultdict objects
from collections import defaultdict

def main():

    #list of items we want to count
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'orange', 'banana',]

    # normal dictionary to count each element
    fruitCounter  = {}

    #count the elements in the fruits list using the normal dict
    for fruit in fruits:
        if fruit in fruitCounter.keys():
            fruitCounter[fruit] +=1
        else:
            fruitCounter[fruit] = 1

    #print result
    for (k,v) in fruitCounter.items():
        print(k + ": "+ str(v))


    #using defaultdict, passing int, it will create a default value using int as constructor, 0.
    # use lambda: 100 to start at a different value for default
    fruitCounter2 = defaultdict(lambda: 100)

    #counting elements using defaultdict
    for fruit in fruits:
        fruitCounter2[fruit] +=1
    
    for k,v in fruitCounter2.items():
        print(k + ": " + str(v))



if __name__ == '__main__':
    main()