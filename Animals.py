from abc import ABC, abstractmethod


# Todo Encapsulation 


class Animals(ABC) :

    def __init__(self, Type, name) :
        self.Type = Type 