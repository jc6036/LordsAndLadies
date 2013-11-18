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
    self.king = Nobility(get_name("first", "male"), get_name("last", "none"), "king")
    self.queen = Nobility(get_name("first", "female"), get_name("last", "none"), "queen")
#Add king and queen objects to kingdom
  
  def populate_noble_children(self, number_of, gender):
    if gender == "male":
      self.princes = [
                     Nobility(get_name("first", "male"), self.king.last_name,
                     "prince") for i in range(0, number_of)
                     ]
    elif gender == "female":
      self.princesses = [
                     Nobility(get_name("first", "female"), self.king.last_name,
                     "princess") for i in range(0, number_of)
                        ]
#Add prince and princess objects to kingdom.  

  def populate_landlords(self, number_of, gender):
    if gender == "male":
      self.lords = [
                   Nobility(get_name("first", "male"), get_name("last", "none"),
                   "lord") for i in range(0, number_of)
                   ]
    elif gender == "female":
      self.ladies = [
                    Nobility(get_name("first", "female"), get_name("last", "none"),
                    "lady", "female") for i in range(0, number_of)
                    ]
#Add lords and lady objects to the kingdom.  

  def populate_important_person(self, number_of, gender):
    jobs = ["blacksmith", "tailor", "farmer", "cobbler", "baker"]
    if gender == "male":
      self.important_males = [
                              Commoner(get_name("first", "male"),
                              get_name("last", "none"), jobs[randint(0, 4)])
                              for i in range(1, number_of)
                             ]
    elif gender == "female":
      self.important_females = [
                                Commoner(get_name("first", "female"),
                                get_name("last", "none"), jobs[randint(0, 4)])
                                for i in range(1, number_of)
                               ]
#Add influential people objects to the kingdom 
 
  def create_locations(self, number_of):
    variations = ["town", "village", "city"]
    self.locations = [
                Location(get_name("location", "none"), variations[randint(0, 2)])
                for i in range(0, number_of)
                ]
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
  
  def __init__(self, name, name_type, title, gender):
    self.name = name
    self.name_type = name_type
    self.title = title
    self.gender = gender


  def title_get(self, place, name_type):
    if place == "subfix":    #Grab sufixes
      if name_type == "nobility": #Noble sufixes
        with open("./Resources/noble_title_subfixes.txt", "r") as opened_file:
          lines = opened_file.readline()
          self.title = lines[randint(1, len(lines))]

      elif name_type == "influential": #Commoner subfixes
        with open("./Resources/common_title_subfixes", "r") as opened_file:
          lines = opened_file.readline()
          self.title = lines[randint(1, len(lines))]
 
    elif place == "prefix":   #Grab prefixes
      if name_type == "nobility": #Noble Prefixes
        with open("./Resources/noble_title_prefixes", "r") as opened_file:
          lines = opened_file.readline()
          self.title = lines[randint(1, len(lines))]

      elif name_type == "influential": #Commoner prefixes
        with open("./Resources/common_title_prefixes", "r") as opened_file:
          lines = opened_file.readline()
          self.title = lines[randint(1, len(lines))]
#Grabs titles for people as prefixes/subfixes


class Nobility(Person):
  """Specific actions for Nobility."""
  
  def __init__(self, name, last_name, job):
    self.name = name
    self.job = job
    self.last_name = last_name


class Commoner(Person):
  """Specific actions for Common People."""
  
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


def get_name(name_type, gender):
  if gender == "none":
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

    elif name_type == "last":
      with open("./Resources/last_names.txt", "r") as opened_file:
        lines = opened_file.readlines()
        chosen_line = lines[randint(1, len(lines))]
        while dupe_check(namelist, chosen_line):
          chosen_line = lines[randint(1, len(lines))]
        else:
          return chosen_line
          namelist.append(chosen_line)

  elif gender == "male":
    if name_type == "first":
        with open("./Resources/male_names.txt", "r") as opened_file:
          lines = opened_file.readlines()
          chosen_line = lines[randint(1, len(lines))]
          while dupe_check(namelist, chosen_line):
            chosen_line = lines[randint(1, len(lines))]
          else:
            return chosen_line
            namelist.append(chosen_line)

  elif gender == "female":
    if name_type == "first":
      with open("./Resources/female_names.txt", "r") as opened_file:
        lines = opened_file.readlines()
        chosen_line = lines[randint(1, len(lines))]
        while dupe_check(namelist, chosen_line):
          chosen_line = lines[randint(1, len(lines))]
        else:
          return chosen_line
          namelist.append(chosen_line)

#Use this for random names at creation of place or person.

Test_Kingdom = Kingdom("Test")
Test_Kingdom.populate_king_queen()
print(Test_Kingdom.king.name)
print(Test_Kingdom.queen.name)
print(Test_Kingdom.queen.last_name)














