# Giving objects number-like behaviour

from tkinter import Y


class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return "<Point x: {0}, y: {1}".format(self.x, self.y)

    #implementing addition
    def __add__(self, other):
        return Point(self.x + other.x, self.y+ other.y)

    #implementing subtraction
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self



def main():
    # declaring some points
    p1 = Point(10,20)
    p2 = Point(25,30)
    print(p1,p2)

    #addition
    print(p1+p2)
    
    #subtraction
    print(p1-p2)

    #in-place addition
    p1 += p2
    print(p1)


if __name__ == '__main__':
    main()