from enum import Enum, IntFlag, unique, auto, IntEnum, IntFlag

@unique # puts constraint on values being unique
class Fruit(Enum):

    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    PEAR = auto()
    #name has to be unique, but values don't unless specified with @unique decorator

class Shape(IntEnum):
    CIRCLE = 1
    SQUARE = 4
    SQUARE_ALIAS = 4
    TRIANGLE = 3
    PENTAGON = 5

class  Perm(IntFlag):
    R = 4
    W = 2
    X = 1
    RWX = 7


def main():
    #enums have human-readable values
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))

    #enums have name and value properties
    print(Fruit.APPLE.name, Fruit.APPLE.value)

    #auto value for aear
    print(Fruit.PEAR.value)

    #enums are hashable- can be used as keys
    myFruits = {}
    myFruits[Fruit.BANANA] = "Come Mr. Tally-man"
    print(myFruits[Fruit.BANANA])

    #access to enumeration members and their attributes

    print(Fruit(1)) # by value
    print(Fruit(3))
    print(Fruit['PEAR'])

    # enum members name or value
    member = Fruit.ORANGE
    print(member.name)
    print(member.value)

    # list iteration
    print(list(Fruit))

    # __members__ iteration
    for name, member in Fruit.__members__.items():
        print(name, member)

    # comparison by identity
    print(Fruit.APPLE is Fruit.APPLE)
    print(Fruit.APPLE is Fruit.BANANA)

    # Ordered comparison only works for IntEnum
    # print(Fruit.APPLE < Fruit.BANANA)

    # Equality camparison
    print("Equality Comparison:")
    print(Fruit.APPLE == Fruit.BANANA)

    #Functional API
    Animal = Enum("Animal", 'ANT BEE CAT DOG')
    print(Animal)
    print(Animal.ANT.value)

    # Ordered comparison of IntEnum
    print(Shape.CIRCLE==1)

    #IntFlag using bitwise operators
    print( Perm.R + Perm.W)
    print(Perm.RWX.value)
    print(~Perm.W)
    print(Perm.X |99)


if __name__ == '__main__':
    main()
