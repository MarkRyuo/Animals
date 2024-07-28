from Dog import Dog 


def main() :

    dog = Dog("Dog", "Rambo", 30,"Moda")

    if dog : # * Creating a statement 
        print(f"{dog.call()} and the age is ({dog.get_age()})")
    else :
        return False


main()