from Dog import Dog 


def main() :

    dog = Dog("Rambo", "Dog", 30)

    if dog :
        print(f"{dog.call()} and the age is {dog.get_age()}")


main()