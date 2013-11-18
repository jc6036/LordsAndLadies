################################################
#Lords and Ladies                              #
#v0.0.b7                                       #
#Authored by jc6036                            #
#Python 3.2 with tkinter and random            #
################################################

from random import randint
from tkinter import *

class Kingdom(object):
  """Contains the kingdoms and fucntions to populate."""

  def __init__(self, name):
    self.name = name


  people = []     #Only 7 lists of people in here.


  def populate_king_queen(self):
    self.king = Nobility(get_name("first", "male"), get_name("last", "none"), "king")
    self.queen = Nobility(get_name("first", "female"), get_name("last", "none"), "queen")
#Add king and queen objects to kingdom. Only one each per kingdom.
  
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

  def get_population(loc_type): #Determine population in a location.
    if loc_type == "town":
      self.population = randint(300, 1000)

    elif loc_type == "village":
      self.population = randint(20, 300)
  
    elif loc_type == "city":
      self.population = randint(1000, 5000)
#Location functions.


class Person(object):
  """Function holder for people."""
  
  def __init__(self, name, gender):
    self.name = name
    self.gender = gender        #Mores stuff with get_name

  alive = True

  def title_get(self, place, name_type):
    if place == "subfix":              #Grab sufixes
      if name_type == "nobility":      #Noble sufixes
        with open("./Resources/noble_title_subfixes.txt", "r") as opened_file:
          lines = opened_file.readline()
          self.title = lines[randint(1, len(lines))]

      elif name_type == "influential": #Commoner subfixes
        with open("./Resources/common_title_subfixes", "r") as opened_file:
          lines = opened_file.readline()
          self.title = lines[randint(1, len(lines))]
 
    elif place == "prefix":            #Grab prefixes
      if name_type == "nobility":      #Noble Prefixes
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
    self.last_name = last_name  #Determines stuff for get_name


class Commoner(Person):
  """Specific actions for Common People."""
  
  def __init__(self, name, last_name, job):
    self.name = name
    self.job = job
    self.last_name = last_name  #More get_name stuff



namelist = []  #Used names are added to this


def dupe_check(namelist, name):

  for i in namelist:
    if name == i:
      return True
    else:
      return False
#For seeing if a name is already in use.


def get_name(name_type, gender):

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
      return chosen_line


  if name_type == "first":
    if gender == "male":
      with open("./Resources/male_names.txt", "r") as opened_file:
        lines = opened_file.readlines()
        chosen_line = lines[randint(1, len(lines))]
        while dupe_check(namelist, chosen_line):
          chosen_line = lines[randint(1, len(lines))]
        else:
          return chosen_line
          namelist.append(chosen_line)

    elif gender == "female":
      with open("./Resources/female_names.txt", "r") as opened_file:
        lines = opened_file.readlines()
        chosen_line = lines[randint(1, len(lines))]
        while dupe_check(namelist, chosen_line):
          chosen_line = lines[randint(1, len(lines))]
        else:
          return chosen_line
          namelist.append(chosen_line)


def populate_kingdom(kingdom, args):
#Args is male children, female children, lords, ladies,
#male commoners, then female commoners. Use integers.
  kingdom.populate_king_queen()
  kingdom.populate_noble_children(args[0], "male")
  kingdom.populate_noble_children(args[1], "female")
  kingdom.populate_landlords(args[2], "male")
  kingdom.populate_landlords(args[3], "female")
  kingdom.populate_important_person(args[4], "male")
  kingdom.populate_important_person(args[5], "female")
  kingdom.people.append([kingdom.king, kingdom.queen])
  kingdom.people.append(kingdom.princes)
  kingdom.people.append(kingdom.princesses)
  kingdom.people.append(kingdom.lords)
  kingdom.people.append(kingdom.ladies)
  kingdom.people.append(kingdom.important_males)
  kingdom.people.append(kingdom.important_females)

#Use this for random names at creation of place or person.
#Put objects into lists for each kingdom for random retrieval.
#Objects have statuses on whether or not something happened, they are alive, etc.
#Kingdoms and locations have populations
#Kingdoms and locations can be destroyed or deserted if enough people dead










