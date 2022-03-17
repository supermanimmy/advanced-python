# the use of keyword-only arguments

# use of keyword arguments help to ensure code clarity
def myFunction(a, arg2, *, b=True):
    print('It worked')

def main():
    myFunction(1,2,b=True)

if __name__ == '__main__':
    main()