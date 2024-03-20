#First hunting process then breeding process 
# The animals can be locate same location.
# Hunting order: The first to be created is the first to be hunted.
# Breeding order: The first to be created is the first to breed. 
# Process continue until  the number 1000 is exceeded.
# For controling the process, program write every step console.
# OOP will be used for the maintenance process
# I choose the camelCase style.

#At first, I tried to make a simple interface so that it would be easy to control. 
#This made it easier for me to check while writing code. 
#However, the project eventually caused problems. That's why I put those parts in the comment line.

#Sometimes it can take a long time for the project to yield results. Not because of this mistake. 
#This is happening because the number of animals increases. Please wait. 

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
  print("IsAlive:", Animal.isAlive)

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
    
createFirstAnimals(1, 15, 15, 10, 10, 10, 10, 5, 5, 4, 4)

#createFirstAnimals() Test Block
# for i in allAnimals:
#   if i.animalType=="Lion":
#      show_data(i)

def findDistance(firstAnimal,secondAnimal):
   x=abs(firstAnimal.locateX -secondAnimal.locateX )
   y=abs(firstAnimal.locateY -secondAnimal.locateY )
   return x+y

#findDistance() Test Block
# obj1=Animal(animalType="Wolf", locateX=0,locateY=7,gender="F")
# obj2=Animal(animalType="Wolf", locateX=2,locateY=0,gender="F")
# print(findDistance(obj1,obj2))

def killAnimal(animal,animalList):
   animal.isAlive= False
   animalList.remove(animal)

# killAnimal() Test Block
# change **this areas** and try this code for control
# obj1=Animal(**animalType="Wolf", locateX=0,locateY=7,gender="F"**)
# obj2=Animal(**animalType="Wolf", locateX=2,locateY=0,gender="F"**)
# obj3=Animal(**animalType="Sheep", locateX=2,locateY=0,gender="F"**)
# exampleList=[obj1,obj2,obj3]
# for i in exampleList:
#    if i.**locateX**==0:
#       killAnimal(i,exampleList)
# print(exampleList)
# print(exampleList[0].**locateX**)
# print(exampleList[1].**locateX**)
# print(**obj1**.isAlive)

def huntingTime(animalList, hunterList):  
   deadNumber=0
  #  print("****START HUNTING TIME****")
  #  print("The wolf can hunt at a distance of 4 and less than 4 units, the lion at a distance of 5 and less than 5 units, and the hunter at a distance of only 8 units.")
   for i in hunterList:
      if i.animalType=="Wolf":
         for j in animalList:
            if j.animalType=="Sheep" or j.animalType=="Chicken":
               if findDistance(i,j)<=i.huntingUnitNumber:
                  killAnimal(j,allAnimals)
                  deadNumber=deadNumber+1
                  # show_data(i)
                  # show_data(j)
                  # print("**********")
      if i.animalType=="Lion":
         for j in animalList:
            if j.animalType=="Sheep" or j.animalType=="Cow":
               if findDistance(i,j)<=i.huntingUnitNumber:
                  killAnimal(j,allAnimals)
                  deadNumber=deadNumber+1
                  # show_data(i)
                  # show_data(j)
                  # print("**********")
      if i.animalType=="Hunter":
         for j in animalList:
            if findDistance(i,j)==i.huntingUnitNumber:
               #The hunter is an archer woman, so she can only kill the animal from a distance of 8 units. 
               #Because that's how I imagined it.
               killAnimal(j,allAnimals)
               deadNumber=deadNumber+1
               if j.animalType=="Lion" or j.animalType=="Wolf":
                  killAnimal(j,allHunters)
  #              show_data(i)
  #              show_data(j)
  #              print("**********")         
  #  print("****FINISH HUNTING TIME****")
   return deadNumber

#huntingTime() works but the code is difficult to maintain and control. There is a danger of being affected by any change.

def checkBreedingConditions(one,two):
  if one.animalType == two.animalType and one.gender != two.gender:
     if findDistance(one,two) <=one.breedingUnitNumber:
        return True
     else:
        return False
  else:
     return False
  
# checkBreedingConditions() Test Block
# change **this areas** and try this code for control
# obj1=Animal(**animalType="Wolf", locateX=0,locateY=7,gender="M"**)
# obj2=Animal(**animalType="Wolf", locateX=3,locateY=7,gender="F"**)
# print(checkBreedingConditions(obj1,obj2))
  

def breedingTime(mainAnimalList):
   babyNumber=0
  #  print("****START BREEDİNG TIME****")
   breedingList=[]
   babyList=[]
   for i in mainAnimalList:
      breedingList.append(i)
   for j in breedingList:
      for k in breedingList:
         if checkBreedingConditions(j,k)==True:
            # show_data(j)
            # show_data(k)
            breedingList.remove(k)
            baby=Animal(animalType=j.animalType, locateX=chooseRandomLocation(),locateY=chooseRandomLocation(),gender=chooseRandomGender())
            babyList.append(baby)
  #  print("***Baby List***")
   for baby in babyList:
      # show_data(baby)
      allAnimals.append(baby)
      babyNumber=babyNumber+1
      if baby.animalType=="Wolf" or baby.animalType=="Lion":
         allHunters.append(baby)
  #  print("****FINISH BREEDİNG TIME****")
   return babyNumber

#breedingTime() works but the code is difficult to control.

def chooseAndMotion(animalList):
   x=random.randint(0,len(animalList)-1) #choose random animal for motion
   y=animalList[x]
   z=random.randint(0,1) #choose x or y axis
   p=random.randint(0,1) #choose positive or negative side
  #  print("BEFORE MOTION")
  #  show_data(y)
   if z==0 and p==0:
      y.locateX= y.locateX-y.motionUnitNumber
   elif z==0 and p==1:
      y.locateX= y.locateX+y.motionUnitNumber
   elif z==1 and p==0:
      y.locateY= y.locateY-y.motionUnitNumber
   elif z==1 and p==1:
      y.locateY= y.locateY+y.motionUnitNumber
  #  print("AFTER MOTION")
  #  show_data(y)
   return y.motionUnitNumber

totalUnits=0
deadAnimalNumber=0
newBabyNumber=0

while totalUnits<1000:
   deadAnimalNumber=deadAnimalNumber+huntingTime(allAnimals, allHunters)
   newBabyNumber=newBabyNumber+breedingTime(allAnimals)
   totalUnits=totalUnits+chooseAndMotion(allAnimals)

huntingTime(allAnimals, allHunters)

print("*********************************")
print("Süreç Sonunda Toplam Hayvan Sayısı:")
print(len(allAnimals))
print("Süreç Sonunda Ölen Toplam Hayvan Sayısı:")
print(deadAnimalNumber)
print("Süreç Sonunda Doğan Toplam Hayvan Sayısı:")
print(newBabyNumber)
print("Başlangıçtaki Hayvan Sayısı")
startNumber=len(allAnimals)+deadAnimalNumber-newBabyNumber
print(startNumber)
print("Toplam Hareket:")
print(totalUnits)