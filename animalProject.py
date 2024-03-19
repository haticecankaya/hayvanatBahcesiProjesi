#First hunting process then breeding process 
# The animals can be locate same location.
# Hunting order: Hunter, Lion, Wolf
# Breeding order: Sheep,Cow,Chicken, Lion
# Process continue until  the number 1000 is exceeded.
# For controling the process, program write every step console.
# OOP will be used for the maintenance process
# huntingUnitNumber=None, breedingUnitNumber=None, MotionUnitNumber=None, isAlive=None,
import random

def chooseRandomLocation():
    return random.randint(1, 500)

def chooseRandomGender():
    x=random.randint(0, 1) 
    if x==0:
     return "M"
    else:
     return "F"

class Animal:
    def __init__(self, animalType=None, locateX=None,locateY=None,gender=None):
        if  animalType == "Hunter":
            self.animalType ="Hunter"
            self.locateX = locateX
            self.locateY = locateY
            self.gender = gender
            self.isAlive = True
            self.huntingUnitNumber=8
            self.breedingUnitNumber=3
            self.motionUnitNumber=1
        elif  animalType == "Lion":
            self.animalType ="Lion"
            self.locateX = locateX
            self.locateY = locateY
            self.gender = gender
            self.isAlive = True
            self.huntingUnitNumber=5
            self.breedingUnitNumber=3
            self.motionUnitNumber=4
        elif  animalType == "Wolf":
            self.animalType ="Wolf"
            self.locateX = locateX
            self.locateY = locateY
            self.gender = gender
            self.isAlive = True
            self.huntingUnitNumber=4
            self.breedingUnitNumber=3
            self.motionUnitNumber=3
        elif  animalType == "Sheep":
            self.animalType ="Sheep"
            self.locateX = locateX
            self.locateY = locateY
            self.gender = gender
            self.isAlive = True
            self.breedingUnitNumber=3
            self.motionUnitNumber=2
        elif  animalType == "Cow":
            self.animalType ="Cow"
            self.locateX = locateX
            self.locateY = locateY
            self.gender = gender
            self.isAlive = True
            self.breedingUnitNumber=3
            self.motionUnitNumber=2
        elif  animalType == "Chicken":
            self.animalType ="Chicken"
            self.locateX = locateX
            self.locateY = locateY
            self.gender = gender
            self.isAlive = True
            self.breedingUnitNumber=3
            self.motionUnitNumber=1
        
    def show_data(self):
        print("Tür:", self.animalType)
        print("LocateX:", self.locateX)
        print("LocateY:", self.locateY)
        print("MotionUnitNumber:", self.motionUnitNumber)
        print("Gender:", self.)

# Örnek kullanım
obj1=Animal(animalType="Wolf", locateX="8",locateY=0,gender=chooseRandomGender())
obj1.show_data()

obj1=Animal(animalType="Hunter", locateX=chooseRandomLocation(),locateY=chooseRandomLocation(),gender=chooseRandomGender())
obj1.show_data()

obj1=Animal(animalType="Lion", locateX=0,locateY=0,gender="F")
obj1.show_data()

obj1=Animal(animalType="Sheep", locateX=0,locateY=0,gender="F")
obj1.show_data()

obj1=Animal(animalType="Cow", locateX=0,locateY=0,gender="F")
obj1.show_data()

obj1=Animal(animalType="Chicken", locateX=0,locateY=0,gender="F")
obj1.show_data()

