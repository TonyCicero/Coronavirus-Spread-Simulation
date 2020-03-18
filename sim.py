import random

#----Simulation Rules----
#2 Towns
#Each town has 1 hospital 1 school 2 workplaces
#Each town has 100 houses
#Each house has 4 people (Must have at least 1 adult)
#ages 0-19 go to school in own town
#ages 20-69 work
#10% from each town work at hospital    =3
#10% from each town work at school      =2
#40% work at workplace in own town      =1
#40% work at workplace in other town    =0


#--------------START OF VIRUS STATS------------------

#Infected status probabilities
MILD = .80
SEVERE = .138
CRITICAL = .061


#80+ years old      index=8
#70-79 years old    index=7
#60-69 years old    index=6
#50-59 years old    index=5
#40-49 years old    index=4
#30-39 years old    index=3
#20-29 years old    index=2
#10-19 years old    index=1
#0-9 years old	    index=0

#reproductive number (attack rate / transmissibility)
#(avg num people to which a single infected person will transmit the virus)
Ro = 2.5

#infectivity factors (Needs to be adjusted based on real data)
INFECTIVITY_H = .5 # chance of being infected if someone in house is infected (increase w/ num people in house infected)
INFECTIVITY_W = .1 # chance of being infected if someone in work is infected (increase w/ num people in house infected)

#Death Rate by age category
DEATHRATE_age = [0, .002, .002, .002, .004, .013, .036, .08, .148]

#Death Rate by Sex
#Male       index=0
#Female     index=1
DEATHRATE_sex = [.028, .017]

#status when Home quarentined
QUARANTINE = 'MILD'
#status when hospitalized
HOSPITALIZED = 'SEVERE'

#--------------END OF VIRUS STATS------------------

TOWNSIZE = 100 #houses per town

DAY = 0
TIME = 'DAY'

#Person Status
STATUS = ['NORM','ASYMPT','MILD','SEVERE','CRIT','DEAD']

#houses in each town
HOUSES_A []
HOUSES_B []

#Workplaces for each town. Holds array of workers/students who are currently in the building
Hospital_A []
Infected_HA = 0 #number of infected people in building
School_A []
Infected_SA = 0 #number of infected people in building
Work_A []
Infected_WA = 0 #number of infected people in building

Hospital_B []
Infected_HB = 0 #number of infected people in building
School_B []
Infected_SB = 0 #number of infected people in building
Work_B []
Infected_WB = 0 #number of infected people in building

#array of people killed by virus seperated by town
Dead_A[]
Dead_B[]

#Events that occur during day time (Exposure to virus)
def DayCycle():
    global HOUSES_A
    global HOUSES_B
    global QUARANTINE
    global HOSPITALIZED
    global Work_A
    global Work_B
    global School_A
    global School_B
    global Hospital_A
    global Hospital_B

    #Travel for Town A
    for House in HOUSES_A: #fill building array with people currently in the building
        for person in House:
            if person.Status == QUARANTINE: #person meets home quarantine status
                #is at home
            elif person.Status == HOSPITALIZED: #person should be hospitalized
                Hospital_A.append(person)
            elif person.Age > 6: #older than age group 6 doesnt go to work
                #is at home
            elif person.Work == 0:
                if person.Status != 'NORM':
                    Infected_WA += 1
                Work_A.append(person)
            elif person.Work == 1:
                if person.Status != 'NORM':
                    Infected_WB += 1
                Work_B.append(person)
            elif person.Work == 2 and person.Town == 'A':
                if person.Status != 'NORM':
                    Infected_SA += 1
                School_A.append(x)
            elif person.Work == 2 and person.Town == 'B':
                if person.Status != 'NORM':
                    Infected_SB += 1
                School_B.append(person)
            elif person.Work == 3 and person.Town == 'A':
                if person.Status != 'NORM':
                    Infected_HA += 1
                Hospital_A.append(person)
            elif person.Work == 3 and person.Town == 'B':
                if person.Status != 'NORM':
                    Infected_HB += 1
                Hospital_B.append(person)
                
    #Travel for Town B
   for House in HOUSES_B: #fill building array with people currently in the building
        for person in House:
            if person.Status == QUARANTINE: #person meets home quarantine status
                #is at home
            elif person.Status == HOSPITALIZED: #person should be hospitalized
                Hospital_A.append(person)
            elif person.Age > 6: #older than age group 6 doesnt go to work
                #is at home
            elif person.Work == 0:
                if person.Status != 'NORM':
                    Infected_WA += 1
                Work_A.append(person)
            elif person.Work == 1:
                if person.Status != 'NORM':
                    Infected_WB += 1
                Work_B.append(person)
            elif person.Work == 2 and person.Town == 'A':
                if person.Status != 'NORM':
                    Infected_SA += 1
                School_A.append(x)
            elif person.Work == 2 and person.Town == 'B':
                if person.Status != 'NORM':
                    Infected_SB += 1
                School_B.append(person)
            elif person.Work == 3 and person.Town == 'A':
                if person.Status != 'NORM':
                    Infected_HA += 1
                Hospital_A.append(person)
            elif person.Work == 3 and person.Town == 'B':
                if person.Status != 'NORM':
                    Infected_HB += 1
                Hospital_B.append(person)
         

def BuildingInfectivity(Building, NI, f): #determine if person in building got infected
    for person in Building:
        if person.Status == 'NORM':
            n = len(Building)
            r = NI/n
            x = r/f
            rand = random.random()
            if rand < x:
                person.Status = 'ASYMPT'
        

def RandWork():
    x = random.randint(0,100)
    if x<40:
        return 0 #works in TownA 
    elif x>40 and x<80:
        return 1 #works in TownB 
    elif x>80 and x<90:
        return 2 #works at school
    elif x>90:
        return 3 #works at hospital


class House: #fills houses with 4 people (At least 1 adult)
    people = []
    ppp = 4;
    def __init__(self, Town, HouseID):
        self.people.append(Person(STATUS[0], random.randint(2,8),Town, HouseID, RandWork()) #create 1 adult
        for x in range(1, ppp):
            self.people.append(Person(STATUS[0], random.randint(0,8), Town, HouseID, RandWork()) #create 3 other random people
        
def GenTown(): #Creates houses for each town
    global TOWNSIZE
    global HOUSES_A
    global HOUSES_B
    for x in TOWNSIZE:
        HOUSES_A.append(House('A',x));
        HOUSES_B.append(House('B',x));
                               
class Person: 
    def __init__(self, status, age, gender, town, home, work):
        self.Status = status #condition of person
        self.Age = age #age group of persion
        self.Gender = gender # gender of person
        self.Town = town # lives in town A or B
        self.Home = home # home id number (1-100)
        self.Work = work # workplace or school
        
