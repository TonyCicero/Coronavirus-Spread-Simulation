import random

class Town:
    houses = [] 
    def __init__(self, numH):
        BuildHouses(self,numH)
    def BuildHouses(self, numH):
        for x in range(0,numH):
            houses.append(House())

class House:
    people = []
    ppp = 4;
    def __init__():
        for x in range(0, ppp):
            people.append(Person())
        
    
class Person:
    def __init__(self, status, age):
        self.status = status
        self.Age = age
        
