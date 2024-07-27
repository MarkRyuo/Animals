from Dog import Dog 


def main() :

    dog = Dog("Rambo", "Dog", 30)
    dog.call()
    print(dog.get_age())

    if dog :
        print(f"{dog.call()} and the age is {dog.get_age()}")


main()