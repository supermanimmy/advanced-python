# Using namedtuple objects example
import collections

def main():
    #Creating namedtuple
    Point = collections.namedtuple("Point", "x y")
    p1 = Point(10,20)
    p2 = Point(30,20)
    print(p1, p2)
    print(p1.x, p1.y)

    #Replacing values using replace function
    p1 = p1._replace(x=8)
    print(p1)

if __name__ == '__main__':
    main()