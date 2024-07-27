from Dog import Dog 


def main() :

    dog = Dog("Dog", "Rambo", 30)

    if dog :
        print(f"{dog.call()} and the age is ({dog.get_age()})")
    else :
        return false 


main()