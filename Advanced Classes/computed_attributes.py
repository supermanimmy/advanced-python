# customising string representations of objects

from multiprocessing.dummy import Value
from typing import Iterable


class Color():
    def __init__(self) -> None:
        self.red = 50
        self.green = 75
        self.blue = 100

    # use getattr to dynamically return a value
    def __getattr__(self, attr):
        if attr == "rgbcolor":
            return (self.red, self.green, self.blue)
        elif attr == 'hexcolor':
            return "#{0:02x}{1:02x}{2:02x}".format(self.red, self.green, self.red)
        else:
            raise AttributeError

    
    # use setattr yo dynamically return a value
    def __setattr__(self, attr, val):
        if attr == "rgbcolor":
            self.red= val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val)

    # use dir to list all available properties
    def __dir__(self) -> Iterable[str]:
        return ("red", "green", "blue", "rgbcolor", "hexcolor")
        

def main():
    # print value of computed attribute
    cls1 = Color()
    print(cls1.rgbcolor)
    print(cls1.hexcolor)

    # set value of computed attribute
    cls1.rgbcolor = (125,200,90)
    print(cls1.rgbcolor)
    print(cls1.hexcolor)

    # access a regular attribute
    print(cls1.red)

    # list all available attributed
    print(dir(cls1))



if __name__ == '__main__':
    main()