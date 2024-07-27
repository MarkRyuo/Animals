from abc import ABC, abstractmethod


# Todo Encapsulation 


class Animals(ABC) :

    def __init__(self, Type, name, age) :
        self.Type = Type  # ? A public attribute 
        self.name = name  # ? A public attribute 
        self.__age = age  # ? A private attribute (age is not accessible in subclass)
    
    
    def call(self) :
        pass

    @abstractmethod
    def get_age(self) :
        pass 