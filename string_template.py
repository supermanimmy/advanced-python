# Demonstrating template string functions
from string import Template


def main():
    #Usual string formatting with format()
    str1 = "You're {} in {}".format('coding', 'Python')
    print(str1)

    #creating a template with placeholders
    templ = Template("You're ${activity} in ${language}")

    str2 = templ.substitute(activity='coding', language='Python')

    print(str2)

    #using substitute with dictionary
    data = {
        'activity': 'coding',
        'language': 'python'
    }

    str3 = templ.substitute(data)
    print(str3)




if __name__ == '__main__':
    main()