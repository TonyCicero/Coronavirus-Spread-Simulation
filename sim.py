import random

#----Simulation Rules----
#2 Towns
#Each town has 1 hospital 1 school 2 workplaces
#Each town has 100 houses
#Each house has 4 people (Must have at least 1 adult)
#ages 0-19 go to school in own town
#ages 20-69 work
#10% from each town work at hospital
#10% from each town work at school
#40% work at workplace in own town
#40% work at workplace in other town


#Infected status probabilities
MILD = .80
SEVERE = .138
CRITICAL = .061

#Death Rate by age category
#80+ years old      index=8
#70-79 years old    index=7
#60-69 years old    index=6
#50-59 years old    index=5
#40-49 years old    index=4
#30-39 years old    index=3
#20-29 years old    index=2
#10-19 years old    index=1
#0-9 years old	    index=0
DEATHRATE_age = [0, .002, .002, .002, .004, .013, .036, .08, .148]

#Death Rate by Sex
#Male       index=0
#Female     index=1
DEATHRATE_sex = [.028, .017]

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
    def __init__(self, status, age, gender, home, work):
        self.Status = status
        self.Age = age
        self.Gender = gender
        self.Home = home
        self.Work = work
        
