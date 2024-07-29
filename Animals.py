from abc import ABC, abstractmethod


class Animals(ABC) :

    # Todo Name_of_animal, age_of_animal, breed_of_animal

    def __init__(self, animalName,animalAge,animalbreed) :
        self.animalName = animalName 
        