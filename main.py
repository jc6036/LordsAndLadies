################################################
#Lords and Ladies                              #
#v0.0.b2                                       #
#Authored by jc6036                            #
#Python 3.2 with tkinter and random            #
################################################

from random import randint
from tkinter import *

class Kingdom(object):
  """Contains the kingdoms and fucntions to populate."""
  
  def __init__(self, name):
    self.name = name
  
  def populate_king_queen(self):
    self.king = Nobility(get_name("noble"), get_name("last"), "king")
    self.queen = Nobility(get_name("noble"), get_name("last"), "queen")
#Add king and queen objects to kingdom
  
  def populate_noble_children(self, identifier):
    gender = ["male", "female"]
    chosen_gender = gender[randint(0, 1)]
    if chosen_gender == "male":
      self.identifier = Nobility(get_name("noble"), get_name("last"), "prince")
    elif chosen_gender == "female":
      self.identifier = Nobility(get_name("noble"), get_name("last"), "princess")
#Add prince and princess objects to kingdom.  

  def populate_landlords(self, identifier):
    gender = ["male", "female"]
    chosen_gender = gender[randint(0, 1)]
    if chosen_gender == "male":
      self.identifier = Nobility(get_name("noble"), get_name("last"), "lord")
    elif chosen_gender == "female":
      self.identifier = Nobility(get_name("noble"), get_name("last"), "lady")
#Add lords and lady objects to the kingdom.  

  def populate_important_person(self, identifier):
    job = ["artisan", "blacksmith", "painter", "mathmetician",
           "inventor", "thief", "bandit", "alchemist"]
    chosen_job = job[randint(0, 8)]
    self.identifier = InfluentialPerson(get_name("common"), get_name("last"), chosen_job)
#Add influential people objects to the kingdom 
 
  def create_locations(self, identifier):
    places = ["village", "town", "city"]
    chosen_place = places[randint(0, 3)]
    self.identifier = Location(get_name("location"), chosen_place)
#Add location objects to the kingdom.
  

class Location(Kingdom):
  """Various functions for locations in kingdoms"""
  #Variation == village, town, city, or castle.
  
  def __init__(self, name, variation):
    self.name = name
    self.variation = variation
#Location functions.


class Person(object):
  """Function holder for people."""
  
  def __init__(self, name, name_type, title):
    self.name = name
    self.name_type = name_type
    self.title = title


  def title_get(self, place, name_type):
    if place == "subfix":    #Grab sufixes
      if name_type == "nobility": #Noble sufixes
        with open("placeholder", -r) as opened_file:
          lines = opened_file.readline()
          title = lines[randint(1, 51)]

      elif name_type == "influential": #Commoner sufixes
        with open("placeholder", -r) as opened_file:
          lines = opened_file.readline()
          title = lines[randint(1, 51)]
 
    elif place == "prefix":   #Grab prefixes
      if name_type == "nobility": #Noble Prefixes
        with open("placeholder", -r) as opened_file:
          lines = opened_file.readline()
          title = lines[randint(1, 51)]

      elif name_type == "influential": #Commoner prefixes
        with open("placeholder", -r) as opened_file:
          lines = opened_file.readline()
          title = lines[randint(1, 51)]
#Grabs titles for people as prefixes/subfixes


class Nobility(Person):
  """Specific actions for Nobility."""
  
  def __init__(self, name, last_name, job):
    self.name = name
    self.job = job
    self.last_name = last_name


class InfluentialPerson(Person):
  """Specific actions for Influential People."""
  
  def __init__(self, name, last_name, job):
    self.name = name
    self.job = job
    self.last_name = last_name



namelist = []  #Used names are added to this


def dupe_check(namelist, name):

  for i in namelist:
    if name == i:
      return True
    else:
      return False
#For seeing if a name is already in use.


def get_name(name_type): 
  if name_type == "kingdom":
    with open("./Resources/kingdom_names.txt", "r") as opened_file:
      lines = opened_file.readlines()
      chosen_line = lines[randint(0, len(lines))]
      while dupe_check(namelist, chosen_line):
        chosen_line = lines[randint(0, len(lines))]
      else:
        return chosen_line
        namelist.append(chosen_line)

  elif name_type == "location":
    with open("./Resources/location_names.txt", "r") as opened_file:
      lines = opened_file.readlines()
      chosen_line = lines[randint(0, len(lines))]
      while dupe_check(namelist, chosen_line):
        chosen_line = lines[randint(0, len(lines))]
      else:
        return chosen_line
        namelist.append(chosen_line)

  elif name_type == "noble":
    with open("./Resources/noble_names.txt", "r") as opened_file:
      lines = opened_file.readlines()
      chosen_line = lines[randint(0, len(lines))]
      while dupe_check(namelist, chosen_line):
        chosen_line = lines[randint(0, len(lines))]
      else:
        return chosen_line
        namelist.append(chosen_line)

  elif name_type == "common":
    with open("./Resources/common_names.txt", "r") as opened_file:
      lines = opened_file.readlines()
      chosen_line = lines[randint(0, len(lines))]
      while dupe_check(namelist, chosen_line):
        chosen_line = lines[randint(0, len(lines))]
      else:
        return chosen_line
        namelist.append(chosen_line)

  elif name_type == "last":
    with open("./Resources/last_names.txt", "r") as opened_file:
      lines = opened_file.readlines()
      chosen_line = lines[randint(0, len(lines))]
      while dupe_check(namelist, chosen_line):
        chosen_line = lines[randint(0, len(lines))]
      else:
        return chosen_line
        namelist.append(chosen_line)

#Use this for random names at creation of place or person.


def create_kingdom(kingdom_number):
#All-in-one function to both create and populate a kingdom.
#Currently set up for debugging and testing
#Not intended to be used at this point. Impending deletion.

  check = raw_input("""
                    Type 'random', or input your own name.
                    """)
  
  if check == "random":
    kingdom_number = Kingdom(get_name("kingdom"))
  else:
    kingdom_number = Kingdom(check)
  kingdom_number.populate_king_queen()
  
  print("The king of your kingdom is ", kingdom_number.king, ".")
  print("The queen of your kingdom is ", kingdom_number.queen, ".")
  print("Now we have to populate it.")
  
  number_of_children = raw_input("""
                                 How many noble children will there be?
                                 """)

  if number_of_children > 10:
    print("No more than ten.")    
  elif number_of_children <= 10:
    for i in range(1, number_of_children + 1):
      kingdom_number.populate_noble_children("child_%s" % str(i))
  else:
    print("Input a number please.")
    

  number_of_landlords = raw_input("""
                                  How many lords and ladies will ther be?
                                  """)

  if number_of_landlords > 20:
    print("No more than twenty.")
  elif number_of_landlords <= 20:
    for i in range(1, number_of_landlords + 1):
      kingdom_number.populate_landlords("landlord_%s" % str(i))
  else:
    print("Numbers only, please.")

  number_of_locations = raw_input("""
                      How many locations? These are Villages, cities, and towns.
                                  """)

  if number_of_locations > 20:
    print("No more than twenty.")
  elif number_of_locations >= 20:
    for i in range(1, number_of_locations + 1):
      kingdom_number.create_locations("location_%s" % str(i))
  else:
    print("Numbers only, please.")
#Use for creation of kingdoms. Auto queries user-defined numbers.

Test_Kingdom = Kingdom("Test_Kingdom")
Test_Kingdom.populate_noble_children()
print(Test_Kingdom.Child_1.name)
#Trying to figure out how to do populate_bahbla multiple times
#Perhaps putting the objects in a list? Seems like a bad idea.
















