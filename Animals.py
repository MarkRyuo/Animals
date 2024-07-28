from abc import ABC, abstractmethod


# Todo Polymorphism 
# Todo add new parameter in superclass 


class Animals(ABC) :

    def __init__(self, Type, name, age) :
        self.Type = Type  # ? A public attribute 
        self.name = name  # ? A public attribute 
        self.__age = age  # ? A private attribute (age is not accessible in subclass)
    
    
    def get_age(self) :
        return self.__age # ? Encapsulation use the get_age method for accessing the private attribute (self.__age)
    
    @abstractmethod
    def call(self) : # ? Abstract uses to efficiency for subclasses 
        pass 