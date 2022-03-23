# How to use dictionary comprehensions

def main():
    # list of temperature values
    ctemps = [0, 12, 34, 100]
    
    # using comprehension to build a dictionary
    tempDict = {t: (t*9/5)+ 32 for t in ctemps if t < 100}
    print(tempDict)
    print(tempDict[12])

    # merging two dictionaries with a comprehension
    team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
    team2 = {"White": 12, "Macke": 88, "Perce": 4}

    allTeam = {k:v for team in (team1, team2) for k,v in team.items()}
    print(allTeam)




if __name__ == '__main__':
    main()