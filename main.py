################################################
#Lords and Ladies                              #
#v0.0.b3                                       #
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
  
  def populate_noble_children(self, number_of, gender):
    if gender == "male":
      self.noble_males = [
                     Nobility(get_name("noble", "male"), self.king.last_name,
                     "prince") for i in range(0, number_of)
                         ]
    elif gender == "female":
      self.noble_females = [
                     Nobility(get_name("noble", "female"), self.king.last_name,
                     "princes") for i in range(0, number_of)
                           ]
#Add prince and princess objects to kingdom.  

  def populate_landlords(self):
    pass
#Add lords and lady objects to the kingdom.  

  def populate_important_person(self):
    pass
#Add influential people objects to the kingdom 
 
  def create_locations(self):
    pass
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


def get_name(name_type, gender = "none"): 
  if name_type == "kingdom":
    with open("./Resources/kingdom_names.txt", "r") as opened_file:
      lines = opened_file.readlines()
      chosen_line = lines[randint(1, len(lines))]
      while dupe_check(namelist, chosen_line):
        chosen_line = lines[randint(1, len(lines))]
      else:
        return chosen_line
        namelist.append(chosen_line)

  elif name_type == "location":
    with open("./Resources/location_names.txt", "r") as opened_file:
      lines = opened_file.readlines()
      chosen_line = lines[randint(1, len(lines))]
      while dupe_check(namelist, chosen_line):
        chosen_line = lines[randint(1, len(lines))]
      else:
        return chosen_line
        namelist.append(chosen_line)

  elif name_type == "noble":
    if gender == "male":
      with open("./Resources/male_noble_names.txt", "r") as opened_file:
        lines = opened_file.readlines()
        chosen_line = lines[randint(1, len(lines))]
        while dupe_check(namelist, chosen_line):
          chosen_line = lines[randint(1, len(lines))]
        else:
          return chosen_line
          namelist.append(chosen_line)
    elif gender == "female":
      with open("./Resources/female_noble_names.txt", "r") as opened_file:
        lines = opened_file.readlines()
        chosen_line = lines[randint(1, len(lines))]
        while dupe_check(namelist, chosen_line):
          chosen_line = lines[randint(1, len(lines))]
        else:
          return chosen_line
          namelist.append(chosen_line)

  elif name_type == "common":
    if gender == "male":
      with open("./Resources/male_common_names.txt", "r") as opened_file:
        lines = opened_file.readlines()
        chosen_line = lines[randint(1, len(lines))]
        while dupe_check(namelist, chosen_line):
          chosen_line = lines[randint(1, len(lines))]
        else:
          return chosen_line
          namelist.append(chosen_line)
    elif gender == "female":
      with open("./Resources/female_common_names.txt", "r") as opened_file:
        lines = opened_file.readlines()
        chosen_line = lines[randint(1, len(lines))]
        while dupe_check(namelist, chosen_line):
          chosen_line = lines[randint(1, len(lines))]
        else:
          return chosen_line
          namelist.append(chosen_line)

  elif name_type == "last":
    with open("./Resources/last_names.txt", "r") as opened_file:
      lines = opened_file.readlines()
      chosen_line = lines[randint(1, len(lines))]
      while dupe_check(namelist, chosen_line):
        chosen_line = lines[randint(1, len(lines))]
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

Test_Kingdom = Kingdom("Test_Kingdom")
Test_Kingdom.populate_king_queen()
print(Test_Kingdom.king.last_name)
Test_Kingdom.populate_noble_children(1, "female")
print(Test_Kingdom.noble_females[0].last_name)

#Trying to figure out how to make generation of populants dynamic
#So that I can do it multiple times...
















