from abc import ABC, abstractmethod


# Todo Encapsulation 


class Animals(ABC) :

    def __init__(self, Type, name, age) :
        self.Type = Type  # ? A public attribute 
        self.name = name  # ? A public attribute 
        self.__age = 10  # ? A private attribute (age is not accessible in subclass)
    
    @abstractmethod
    def call(self) :
        pass

    def get_age(self) :
        return self.__age 