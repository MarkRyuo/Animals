from Dog import Dog 


def main() :

    dog = Dog("Rambo", "Dog", 30)
    dog.call()
    print(dog.get_age())

    if dog :
        print(f"")


main()