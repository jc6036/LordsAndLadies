################################################
#Lords and Ladies                              #
#v0.0.b1                                       #
#Authored by jc6036                            #
#Python 3.2 with tkinter, ttk, and random      #
################################################

from random import randint
from tkinter import *
import ttk

class Kingdom(object, name):
  """Contains the kingdoms and fucntions to populate."""
  
  def __init__(self, name):
    name = self.name
  
  def populate_king_queen(self):
    king = Nobility(get_name("person"), "king")
    queen = Nobility(get_name("person"), "queen")
  
  def populate_noble_children(self, identifier):
    gender = ["male", "female"]
    chosen_gender = gender[randint(0, 2)]

    if chosen_gender == "male":
      identifier = Nobility(get_name("person"), "prince")

    elif chosen_gender == "female":
      identifier = Nobility(get_name("person"), "princess")
  
  def populate_landlords(self, identifier):
    gender = ["male", "female"]
    chosen_gender = gender[randint(0, 2)]

    if chosen_gender == "male":
      identifier = Nobility(get_name("person"), "lord")

    elif chosen_gender == "female":
      identifier = Nobility(get_name("person"), "lady")
  
  def populate_important_person(self, identifier):
    job = ["artisan", "blacksmith", "painter", "mathmetician",
           "inventor", "thief", "bandit", "alchemist"]
    chosen_job = job[randint(0, 9)]
    
    identifier = InfluentialPerson(get_name("person"), chosen_job)
  
  def create_locations(self, identifier):
    places = ["village", "town", "city"]
    chosen_place = places[randint(0, 4)]
    
    identifier = Location(get_name("location"), chosen_place)
#For creation of Kingdoms/Population/Locations.
  

class Location(Kingdom, name, variation):
  """Various functions for locations in kingdoms"""
  #Variation == village, town, city, or castle.
  
  def __init__(self, name, variation):
    name = self.name
    variation = self.variation
#Location functions.


class Person(object, name, name_type):
  """Function holder for people."""
  
  def __init__(self, name):
    name = self.name
    name_type = self.name_type


  def title_get(self, place, name_type):
    if place == "subfix":
      if name_type == "nobility":
        with open("placeholder", -r) as opened_file:
          lines = opened_file.readline()
          return lines[randint(1, 51)]

      elif name_type == "influential":
        with open("placeholder", -r) as opened_file:
          lines = opened_file.readline()
          return lines[randint(1, 51)]
 
    elif place == "prefix":
      if name_type == "nobility":
        with open("placeholder", -r) as opened_file:
          lines = opened_file.readline()
          return lines[randint(1, 51)]

      elif name_type == "influential":
        with open("placeholder", -r) as opened_file:
          lines = opened_file.readline()
          return lines[randint(1, 51)]
#Grabs titles for people as prefixes/subfixes

class Nobility(Person, name, job):
  """Specific actions for Nobility."""
  
  name_type = "nobility"
  
  def __init__(self, name, job):
    name = self.name
    job = self.job


class InfluentialPerson(Person, name, job):
  """Specific actions for Influential People."""
  
  name_type = "influential"
  
  def __init__(self, name, job):
    name = self.name
    job = self.job



namelist = []


def dupe_check(namelist, name):

  for i in namelist:
    if name == i:
      return True
    else:
      return False
#For seeing if a name is already in use.


def get_name(name_type): 
  if name_type == "kingdom":
    with open("placeholder", -r) as opened_file:
      lines = opened_file.readlines()
      chosen_line = lines[randint(0, 201)]
      while dupe_check(namelist, chosen_line):
        chosen_line = lines[randint(0, 201)]
      else:
        return chosen_line

  elif name_type == "location":
    with open("placeholder", -r) as opened_file:
      lines = opened_file.readlines()
      chosen_line = lines[randint(0, 201)]
      while dupe_check(namelist, chosen_line):
        chosen_line = lines[randint(0, 201)]
      else:
        return chosen_line

  elif name_type == "person":
    with open("placeholder", -r) as opened_file:
      lines = opened_file.readlines()
      chosen_line = lines[randint(0, 201)]
      while dupe_check(namelist, chosen_line):
        chosen_line = lines[randint(0, 201)]
      else:
        return chosen_line
#Use this for random names at creation of place or person.


def create_kingdom(kingdom_number):
#All-in-one function to both create and populate a kingdom.

  check = raw_input("""
                    Type 'random', or input your own name.
                    """)
  
  if check == "random":
    kingdom_number = Kingdom(get_name("kingdom"))
  else:
    kingdom_number = Kingdom(check)
  kingdom_number.populate_king_queen()
  
  print("The king of your kingdom is ", kingdom_one.king, ".")
  print("The queen of your kingdom is ", kingdom_one.queen, ".")
  print("Now we have to populate it.")
  
  number_of_children = raw_input("""
                                 How many noble children will there be?
                                 """)

  if number_of_children > 10:
    print("No more than ten.")    
  elif number_of_children <= 10:
    for i in range(1, number_of_children):
      kingdom_number.populate_noble_children("child_" + str(i))
  else:
    print("Input a number please.")
    

  number_of_landlords = raw_input("""
                                  How many lords and ladies will ther be?
                                  """)

  if number_of_landlords > 20:
    print("No more than twenty.")
  elif number_of_landlords <= 20:
    for i in range(1, number_of_landlords + 1):
      kingdom_number.populate_landlords("landlord_" + str(i))
  else:
    print("Numbers only, please.")

  number_of_locations = raw_input("""
                      How many locations? These are Villages, cities, and towns.
                                  """)

  if number_of_locations > 20:
    print("No more than twenty.")
  elif number_of_locations >= 20:
    for i in range(1, number_of_locations + 1):
      kingdom_number.create_locations("location_" + str(i))
  else:
    print("Numbers only, please.")


print("""
      Welcome to Lords and Ladies!
      Prepare yourself for drama.
      Wars, crazy weather, and assassination abound!
      """)

print("""
      Create your first kingdom to get started.
      """)

create_kingdom("kingdom_1")

amount_new = raw_input("""
                       How many more Kingdoms would you like to add?
                       """)

for i in range(2, amount_new + 1):
  create_kingdom("kingdom_" + str(i))