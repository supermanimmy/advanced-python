# demonstrating the use of function docstring

def myFunction(arg1, arg2=None):
    """myFunction(arg1, arg2=None) --> Doesn't really do anything, just prints.

    Parameters:
    arg1: the first argument
    arg2: second argument, default is None
    """
    print(arg1, arg2)

def main():
    print(myFunction.__doc__)

if __name__ == '__main__':
    main()