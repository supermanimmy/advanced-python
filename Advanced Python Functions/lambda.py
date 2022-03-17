# Using lambdas as in-place functions

def CelsisusToFahrenheit(temp):
    return (temp*9/5)+32

def FahrenheitToCelsisus(temp):
    return (temp-32)* 5/9

def main():
    # temperature
    ctemps = [0,12,34,100]
    ftemps = [32,65,100,212]

    #using regular functions
    print(list(map(FahrenheitToCelsisus, ftemps)))
    print(list(map(CelsisusToFahrenheit, ctemps)))

    #using lambda
    print(list(map(lambda t: (t-32)* 5/9, ftemps)))
    print(list(map(lambda t: (t*9/5)+32, ftemps)))



if __name__ == '__main__':
    main()