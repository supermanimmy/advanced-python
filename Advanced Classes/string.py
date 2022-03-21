class Person():
    def __init__(self):
        self.fname = "Clark"
        self.sname = "Kent"
        self.age = 25

    def __repr__(self) -> str:
        return "<Person Class - fname {0}, lname {1}, age {2}".format(self.fname, self.sname, self.age)
    
    def __str__(self) -> str:
        return "Person ({0} {1} is {2})".format(
            self.fname, self.sname, self.age
        )

    def __bytes__(self) -> bytes:
        val = "Person: {0}: {1}: {2}".format(
            self.fname, self.sname, self.age
        )
        return bytes(val.encode('utf-8'))
    

def main():
    cls1 = Person()
    

    print(repr(cls1))
    print(str(cls1))
    print("Formatted: {0}".format(cls1))
    """
    Before
    <__main__.Person object at 0x0000024A778FC040>
    <__main__.Person object at 0x0000024A778FC040>
    Formatted: <__main__.Person object at 0x0000024A778FC040>

    After repr override
    <Person Class - fname Clark, lname Kent, age 25
    <Person Class - fname Clark, lname Kent, age 25
    Formatted: <Person Class - fname Clark, lname Kent, age 25

    After str override
    <Person Class - fname Clark, lname Kent, age 25
    Person (Clark Kent is 25)
    Formatted: Person (Clark Kent is 25
    """
    print(bytes(cls1))

    


if __name__ == '__main__':
    main()