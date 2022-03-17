# use of variable argument lists

def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result

def main():
    # Passing different arguements
    print(addition(5,10,20))
    
    #passing a list
    myNums = [5,9,8,10,3]
    print(addition(*myNums))

if __name__ == '__main__':
    main()