from math import *

def poundsToKG(pounds):
   kilograms = pounds * 0.453592
   return kilograms

def getMassObject(object):
   if object == "t":
      mass = 0.1
   elif object == "p":
      mass = 1.0
   elif object == "r":
      mass = 3.0
   elif object == "g":
      mass = 5.3
   elif object == "l":
      mass = 9.07
   else:
      mass = 0.0
   return mass
   
def getVelocityObject(d):
   return sqrt((9.8 * d) / 2)

def getVelocitySkater(massSkater, massObject, velObject):
   return (massObject * velObject) / massSkater