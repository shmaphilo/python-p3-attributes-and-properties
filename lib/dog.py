#!/usr/bin/env python3 


class Dog:
    APPROVED_BREEDS = [
        "Mastiff",
        "Chihuahua",
        "Corgi",
        "Shar Pei",
        "Beagle",
        "French Bulldog",
        "Pug",
        "Pointer"
    ]

    def __init__(self, name, breed):
        self._name = None
        self._breed = None
        self.name = name  
        self.breed = breed  

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not (1 <= len(value) <= 25) or not isinstance(value, str):
            raise ValueError("Name must be a string between 1 and 25 characters.")
        self._name = value

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value not in self.APPROVED_BREEDS:
            raise ValueError("Breed must be in the list of approved breeds.")
        self._breed = value

    def __str__(self):
        return f"{self.name}, {self.breed}"

try:
    my_dog = Dog("Buddy", "Terrier")
except ValueError as e:
    print(e) 

