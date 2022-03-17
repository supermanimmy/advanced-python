# demonstrating the usage of OrderedDict objects
from collections import OrderedDict
from os import O_RDONLY

def main():
    #list of sport teams with wins and losses
    sportsTeams = [
        ('Royals', (18,12)),
        ('Rockets', (24,7)),
        ('Cardinals', (20,10)),
        ('Dragons', (22,10)),
        ('Kings', (15,15)),
        ("Chargers", (20,10)),
        ("Jets", (16,14)),
        ('Warriors', (25,5))

    ]


    # sort by the number of wins
    sortedTeams = sorted(sportsTeams, key=lambda t: t[1][0], reverse=True)
    print(sortedTeams)

    # create an ordered dictionary of the teams
    teams = OrderedDict(sortedTeams)
    print(teams)

    # use popitem to remove the top item
    tm, wl = teams.popitem(False)
    print("Top team: ", tm, wl)

    for i, m in enumerate(teams, start=1):
        print(i, m)
        if i == 4:
            break

    # test for equality
    a = OrderedDict({'a': 1, 'b': 2, 'c': 3})
    b = OrderedDict({'a': 1, 'b': 2, 'c': 3})
    #moving a to the end to show order is important
    c = OrderedDict({'b': 2, 'c': 3, 'a': 1})
    #normal dict with different order
    d = {'c': 3, 'b': 2, 'a': 1}

    # comparing two ordereddict with same values
    print("Equality test: ", a==b)
    #comparing two ordereddict with same values at different order
    print("Equality test:", a==c)
    #comparing orderedict with regular dict
    print("Equality test with normal dict:", d==a) #order doesn't matter if compared to normal dict

if __name__ == '__main__':
    main()