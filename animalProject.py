#First hunting process then breeding process 
# The animals can be locate same location.
# Hunting order: Hunter, Lion, Wolf
# Breeding order: Sheep,Cow,Chicken,Wolf Lion
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
        

def show_data(Animal):
  print("***************************************************")
  print("Tür:", Animal.animalType)
  print("LocateX:", Animal.locateX)
  print("LocateY:", Animal.locateY)
  print("MotionUnitNumber:", Animal.motionUnitNumber)
  print("Gender:", Animal.gender)

allAnimals=[]
allHunters=[]

def createFirstAnimals(hunter, sheepF, sheepM, cowF, cowM, chickenF, chickenM, wolfF, wolfM, lionF, lionM):
   #createFirstAnimals(hunter, sheepFemale, sheepMale, CowF, CowM, ChickenF, ChickenM, WolfF, WolfM, LionF, LionM):
  #1, 15, 15, 10, 10, 10, 10, 5, 5, 4, 4
  
  for i in range(hunter):
    yeni_nesne = Animal(animalType="Hunter", locateX=chooseRandomLocation(),locateY=chooseRandomLocation(),gender="F")
    allAnimals.append(yeni_nesne)
    allHunters.append(yeni_nesne)
  
  for i in range(sheepF):
    yeni_nesne = Animal(animalType="Sheep", locateX=chooseRandomLocation(),locateY=chooseRandomLocation(),gender="F")
    allAnimals.append(yeni_nesne)

  for i in range(sheepM):
    yeni_nesne = Animal(animalType="Sheep", locateX=chooseRandomLocation(),locateY=chooseRandomLocation(),gender="M")
    allAnimals.append(yeni_nesne)

  for i in range(cowF):
    yeni_nesne = Animal(animalType="Cow", locateX=chooseRandomLocation(),locateY=chooseRandomLocation(),gender="F")
    allAnimals.append(yeni_nesne)

  for i in range(cowM):
    yeni_nesne = Animal(animalType="Cow", locateX=chooseRandomLocation(),locateY=chooseRandomLocation(),gender="M")
    allAnimals.append(yeni_nesne)

  for i in range(chickenF):
    yeni_nesne = Animal(animalType="Chicken", locateX=chooseRandomLocation(),locateY=chooseRandomLocation(),gender="F")
    allAnimals.append(yeni_nesne)
  
  for i in range(chickenM):
    yeni_nesne = Animal(animalType="Chicken", locateX=chooseRandomLocation(),locateY=chooseRandomLocation(),gender="M")
    allAnimals.append(yeni_nesne)

  for i in range(lionF):
    yeni_nesne = Animal(animalType="Lion", locateX=chooseRandomLocation(),locateY=chooseRandomLocation(),gender="F")
    allAnimals.append(yeni_nesne)
    allHunters.append(yeni_nesne)
    
  for i in range(lionM):
    yeni_nesne = Animal(animalType="Lion", locateX=chooseRandomLocation(),locateY=chooseRandomLocation(),gender="M")
    allAnimals.append(yeni_nesne)
    allHunters.append(yeni_nesne)
    
  for i in range(wolfF):
    yeni_nesne = Animal(animalType="Wolf", locateX=chooseRandomLocation(),locateY=chooseRandomLocation(),gender="F")
    allAnimals.append(yeni_nesne)
    allHunters.append(yeni_nesne)
    
  for i in range(wolfM):
    yeni_nesne = Animal(animalType="Wolf", locateX=chooseRandomLocation(),locateY=chooseRandomLocation(),gender="M")
    allAnimals.append(yeni_nesne)
    allHunters.append(yeni_nesne)
    
createFirstAnimals(1, 2, 3, 1, 2, 4, 2, 5, 6, 2, 1)


for i in allAnimals:
  if i.animalType=="Lion":
     show_data(i)

