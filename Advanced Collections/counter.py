# demonstrating the counter, counter is a dictionary

from collections import Counter

def main():
    #list of students
    class1 = ['Arnie', 'Tom', 'Galam', 'Lucas', 'Kris', 'Luki', 'Jonathan', 'Pajeet']

    class2 = ['Arnie', 'Galam', 'Tomas', 'Lucie', 'Chris', 'Imran', 'Harry', 'Potter']

    #Creating counter for list of students

    c1 = Counter(class1)
    c2 = Counter(class2)

    # using functions
    print(c1['Arnie'])

    print(sum(c1.values()), 'Students in class 1')

    #combine two classes
    c1.update(class2)
    print(c1)

    #most common
    print(c1.most_common(2))

    #seperate the classses
    c1.subtract(class2)
    print(c1.most_common(3))

    #intersection
    print(c1 & c2)

if __name__ == '__main__':
    main()