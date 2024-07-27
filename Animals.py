from abc import ABC, abstractmethod


# Todo Encapsulation 


class Animals(ABC) :

    def __init__(self, Type, name, age) :
        self.Type = Type  # ? A public attribute 
        self.name = name  # ? A public attribute 
        self.__age = age  # ? A private attribute (age is not accessible in subclass)
    
    
    def call(self) :
        print(f"The name of this {self.Type} is {self.name}") # ! Solve this problem


    def get_age(self) :
        return self.__age 