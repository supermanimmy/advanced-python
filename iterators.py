# using iterator functions to enumerate, zip, iter, next


def main():
    #define a lsit of days in English and French
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    daysFr = ['Dim', 'Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam']

    #iterator over a collection
    i = iter(days)
    print(next(i))
    print(next(i))

    # iterator using a function and a sentinel '' 
    with open("testfile.txt", "r") as fp:
        for line in iter(fp.readline, ''):
            print(line)

    # use regular interation over the days
    # for m in range(len(days)):
    #     print(m+1, days[m])

    # using emuerate reduces code and provides counter
    for i,m in enumerate(days, start=1):
        print(i,m)

    # using zip function to combine sequences
    for i,m in enumerate(zip(days, daysFr), start=1):
        print(i,m[0], '=', m[1], 'in French')

if __name__ == '__main__':
    main()