from funcs import *

def main():
   weight = int(input("How much do you weigh (pounds)? "))
   distance = int(input("How far away is your professor (meters)? "))
   object_mass = input("Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ight saber, or lawn (g)nome? ")

   print("\nNice throw! ", end = '')

   skater_mass = poundsToKG(weight)
   new_object_mass = getMassObject(object_mass)
   object_velocity = getVelocityObject(distance)
   skater_velocity = getVelocitySkater(skater_mass, new_object_mass, object_velocity)

   if new_object_mass <= 0.1:
      print("You're going to get an F!")
   elif new_object_mass > 0.1 and new_object_mass <= 1.0:
      print("Make sure your professor is OK.")
   elif new_object_mass > 1.0:
      if distance < 20:
         print("How far away is the hospital?")
      elif distance >= 20:
         print("RIP professor.")

   print("Velocity of skater: %.3f m/s" % (skater_velocity))

   if skater_velocity < 0.2:
      print("My grandmother skates faster than you!")
   elif skater_velocity >= 1.0:
      print("Look out for that railing!!!")
   elif skater_velocity >= 0.2 and skater_velocity < 1.0:
      pass


if __name__ == '__main__':
   main()