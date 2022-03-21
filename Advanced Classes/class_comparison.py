# use special methods to compare objects to each other

class Employee():
    def __init__(self, fname, lname, level, yrsService):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.seniority= yrsService

    def __repr__(self):
        return "<Employee Class - fname {0}, lname {1}, level {2}, years of service {3}".format(self.fname, self.lname, self.level, self.seniority)

    def __str__(self) -> str:
        return "Employee {0} {1}, level {2} with {3} years of service".format(self.fname, self.lname, self.level, self.seniority)

    # compare employee levels
    def __ge__(self, other):
        if (self.level == other.level):
            return self.seniority >= other.seniority
        return self.level >= other.level

    def __gt__(self, other):
        if (self.level == other.level):
            return self.seniority > other.seniority
        return self.level > other.level

    def __lt__(self, other):
        if (self.level == other.level):
            return self.seniority < other.seniority
        return self.level < other.level

    def __le__(self, other):
        if (self.level <= other.level):
            return self.seniority >= other.seniority
        return self.level <= other.level

    def __eq__(self, other):
        if (self.level == other.level):
            return self.seniority == other.seniority
        return self.level == other.level



def main():
    #defining a list of employees
    dept = []
    dept.append(Employee("Charlie", "Chaplin", 4, 29))
    dept.append(Employee("Clark", "Kent", 3, 10))
    dept.append(Employee("Lex", "Luthor", 4, 10))
    dept.append(Employee("Darth", "Vader", 4, 10))
    dept.append(Employee("Atticus", "Finch", 3, 20))
    dept.append(Employee("Sherlock", "Holmes", 5, 30))


    # who's more senior?
    print(dept[0] > dept[1])
    print(dept[0]< dept[2])

    #sort department
    sortEmp = sorted(dept)

    for emp in sortEmp:
        print(emp)
        
    print(dept[1])

if __name__ == '__main__':
    main()