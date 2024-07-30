from abc import ABC, abstractmethod
from data import data_Animals


class Animals(ABC) :

    # Todo Name_of_animal, age_of_animal, breed_of_animal

    def __init__(self, animalName,animalAge,animalBreed) :
        self.animalName = animalName # ? Public attribute
        self.animalAge = animalAge # ? Public attribute
        self.__animalBreed = animalBreed # ? Private attribute 

    # * Encapsulation 
    def get_breed(self) :
        return self.__animalBreed # * Returning the private aatribute to access publically
    

    def get_name(self) :
        # todo create a simple logic here to check name of the animal 
        # * Restrict if name of animal is Existed
        
        if self.animalName == data_Animals["nameData"] :
            return False 
        else :
            return True
    


    @abstractmethod 
    def display(self) :
        pass