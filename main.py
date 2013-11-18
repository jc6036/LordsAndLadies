################################################
#Lords and Ladies                              #
#v0.0.b7                                       #
#Authored by jc6036                            #
#Python 3.2 with tkinter and random            #
################################################

from random import randrange
from tkinter import *

class Kingdom(object):
  """Contains the kingdoms and fucntions to populate."""

  def __init__(self, name):
    self.name = name


  people = {
            "male_children": [],
            "female_children": [],
            "lords": [],
            "ladies": [],
            "important_males": [],
            "important_females": [],
  }


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
                    "lady") for i in range(0, number_of)
  ]
#Add lords and lady objects to the kingdom.  


  def populate_important_person(self, number_of, gender):
    jobs = ["blacksmith", "tailor", "farmer", "cobbler", "baker"]
    if gender == "male":
      self.important_males = [
                    Commoner(get_name("first", "male"),
                    get_name("last", "none"), jobs[randrange(0, 4)])
                    for i in range(1, number_of)
  ]

    elif gender == "female":
      self.important_females = [
                    Commoner(get_name("first", "female"),
                    get_name("last", "none"), jobs[randrange(0, 4)])
                    for i in range(1, number_of)
  ]
#Add influential people objects to the kingdom 
 

  def create_locations(self, number_of):
    variations = ["town", "village", "city", "castle"]
    self.locations = [
                    Location(get_name("location", "none"), variations[randrange(0, 3)])
                    for i in range(0, number_of)
  ]
#Add location objects to the kingdom.


  def populate_kingdom(self, *args):
#Args is number of male children, female children, lords,
#ladies, male commoners, then female commoners. Use integers.
    self.populate_king_queen()
    self.populate_noble_children(args[0], "male")
    self.populate_noble_children(args[1], "female")
    self.populate_landlords(args[2], "male")
    self.populate_landlords(args[3], "female")
    self.populate_important_person(args[4], "male")
    self.populate_important_person(args[5], "female")
    self.people["male_children"] = self.princes
    self.people["female_children"] = self.princesses
    self.people["lords"] = self.lords
    self.people["ladies"] = self.ladies
    self.people["important_males"] = self.important_males
    self.people["important_females"] = self.important_females


  def get_location_populations(self):
    for i in self.locations:
      i.get_population(variation)
#Use to generate population numbers for all locations in kingdom.


  def get_total_population(self, location_list):
    self.population = 0
    for i in self.locations:
      self.population += i.population
#Gets the total population of the kingdom


class Location(Kingdom):
  """Various functions for locations in kingdoms"""
  #Variation == village, town, city, or castle.
  
  def __init__(self, name, variation):
    self.name = name
    self.variation = variation


  alive = True

  people = {
            "landlord": [],
            "important_males": [],
            "important_females":[],
  }


  def get_population(self): #Determine population in a location.
    if self.variation == "town":
      self.population = randrange(300, 1000)
    elif self.variation  == "village":
      self.population = randrange(20, 300)
    elif self.variation  == "city":
      self.population = randrange(1000, 5000)
    elif self.variation  == "castle":
      self.population = randrange(5000, 10000)


  def living_check(self):
    if self.population <= 0:
      self.alive = False


  def get_full_name(self):
    if self.variation == "village":
      self.name = "Village %s" % self.name
    elif self.variation == "town":
      self.name = "Town %s" % self.name
    elif self.variation == "city":
      self.name = "City %s" % self.name
    elif self.variation == "castle":
      self.name = "Castle %s" % self.name


  def get_local_people(self, num_of_male, num_of_female):
    random_gender = ["male", "female"][randrange(0, 1)]
    self.populate_landlords(1, random_gender)
    self.populate_important_person(num_of_male, "male")
    self.populate_important_person(num_of_female, "female")
    if random_gender == "male":
      self.people["landlord"] = self.lords
    elif random_gender == "female":
      self.people["landlord"] = self.ladies
    self.people["important_males"] = self.important_males
    self.people["important_females"] = self.important_females


class Person(object):
  """Function holder for people."""
  
  def __init__(self, name, gender):
    self.name = name
    self.gender = gender  #Usually needed for get_name

  alive = True

  def title_get(self, place, name_type):
    if place == "subfix":              #Grab sufixes
      if name_type == "nobility":      #Noble sufixes
        with open("./Resources/noble_title_subfixes.txt", "r") as opened_file:
          lines = opened_file.readline()
          self.title = lines[randrange(1, len(lines))]

      elif name_type == "influential": #Commoner subfixes
        with open("./Resources/common_title_subfixes", "r") as opened_file:
          lines = opened_file.readline()
          self.title = lines[randrange(1, len(lines))]
 
    elif place == "prefix":            #Grab prefixes
      if name_type == "nobility":      #Noble Prefixes
        with open("./Resources/noble_title_prefixes", "r") as opened_file:
          lines = opened_file.readline()
          self.title = lines[randrange(1, len(lines))]

      elif name_type == "influential": #Commoner prefixes
        with open("./Resources/common_title_prefixes", "r") as opened_file:
          lines = opened_file.readline()
          self.title = lines[randrange(1, len(lines))]
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
      chosen_line = lines[randrange(0, len(lines))]
      while dupe_check(namelist, chosen_line):
        chosen_line = lines[randrange(0, len(lines))]
      else:
        return chosen_line
        namelist.append(chosen_line)

  elif name_type == "location":
    with open("./Resources/location_names.txt", "r") as opened_file:
      lines = opened_file.readlines()
      chosen_line = lines[randrange(0, len(lines))]
      while dupe_check(namelist, chosen_line):
        chosen_line = lines[randrange(0, len(lines))]
      else:
        return chosen_line
        namelist.append(chosen_line)

  elif name_type == "last":
    with open("./Resources/last_names.txt", "r") as opened_file:
      lines = opened_file.readlines()
      chosen_line = lines[randrange(0, len(lines))]
      return chosen_line

  if name_type == "first":
    if gender == "male":
      with open("./Resources/male_names.txt", "r") as opened_file:
        lines = opened_file.readlines()
        chosen_line = lines[randrange(0, len(lines))]
        while dupe_check(namelist, chosen_line):
          chosen_line = lines[randrange(0, len(lines))]
        else:
          return chosen_line
          namelist.append(chosen_line)

    elif gender == "female":
      with open("./Resources/female_names.txt", "r") as opened_file:
        lines = opened_file.readlines()
        chosen_line = lines[randrange(0, len(lines))]
        while dupe_check(namelist, chosen_line):
          chosen_line = lines[randrange(0, len(lines))]
        else:
          return chosen_line
          namelist.append(chosen_line)
#Use this for random names at creation of place or person.









