################################################
#Lords and Ladies                              #
#v0.0.b8                                       #
#Authored by jc6036                            #
#Python 3.2 with tkinter and random            #
################################################

from random import randrange
from tkinter import *

class Kingdom(object):
  """Contains the kingdoms and fucntions to populate."""

  def __init__(self, name):
    self.name = name
    self.full_name = "The Kingdom of {0}".format(name)


  people = {  #Container for the various named people
            "princes": [],
            "princesses": [],
            "lords": [],
            "ladies": [],
            "important_males": [],
            "important_females": [],
  }


  def populate_king_queen(self):
    self.king = Nobility(
                         get_name("first", "male"),
                         get_name("last", "none"), "king"
                        )
    self.queen = Nobility(
                          get_name("first", "female"),
                          get_name("last", "none"), "queen"
                         )
#Add king and queen objects to kingdom. Only one each per kingdom.
  

  def populate_noble_children(self, number_of, gender):
    if gender == "male":
      self.princes = [
                    Nobility(get_name("first", "male"),
                    self.king.last_name, "prince")
                    for i in range(0, number_of)
                     ]

    elif gender == "female":
      self.princesses = [
                    Nobility(get_name("first", "female"),
                    self.king.last_name,"princess")
                    for i in range(0, number_of)
                        ]
#Add prince and princess objects to kingdom.  


  def populate_landlords(self, number_of, gender):
    if gender == "male":
      self.lords = [
                    Nobility(get_name("first", "male"),
                    get_name("last", "none"), "lord")
                    for i in range(0, number_of)
                   ]

    elif gender == "female":
      self.ladies = [
                    Nobility(get_name("first", "female"),
                    get_name("last", "none"), "lady")
                    for i in range(0, number_of)
                    ]
#Add lords and lady objects to the kingdom.  


  def populate_important_person(self, number_of, gender):
    jobs = ["blacksmith", "tailor", "farmer", "cobbler", "baker"]
    if gender == "male":
      self.important_males = [
                    Commoner(get_name("first", "male"),
                    get_name("last", "none"),
                    jobs[randrange(0, 5)])
                    for i in range(0, number_of)
                             ]

    elif gender == "female":
      self.important_females = [
                    Commoner(get_name("first", "female"),
                    get_name("last", "none"),
                    jobs[randrange(0, 5)])
                    for i in range(0, number_of)
                               ]
#Add influential people objects to the kingdom 
 

  def create_locations(self, number_of):
    variations = ["town", "village", "city", "castle"]
    self.locations = [
                    Location(get_name("location", "none"),
                    variations[randrange(0, 4)])
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
    self.people["princes"] = self.princes
    self.people["princesses"] = self.princesses
    self.people["lords"] = self.lords
    self.people["ladies"] = self.ladies
    self.people["important_males"] = self.important_males
    self.people["important_females"] = self.important_females
    for i in self.locations:
      i.get_local_people(randrange(1, 6), randrange(1, 6))


  def get_location_populations(self):
    for i in self.locations:
      i.get_population()
#Use to generate population numbers for all locations in kingdom.


  def get_total_population(self, location_list):
    self.population = 0
    for i in self.locations:
      self.population += i.population
#Gets the total population of the kingdom

  
  def get_full_name(self):
    self.full_name = "The Kingdom of " + self.name
#Gets the full name of the kingdom.


class Location(Kingdom):
  """Various functions for locations in kingdoms"""
  #Variation == village, town, city, or castle.
  
  def __init__(self, name, variation):
    self.name = name
    self.variation = variation
    self.full_name = "The {0} of {1}".format(variation, name)


  alive = True

  people = {  #Container for location-specific named people.
            "landlord": [],
            "important_males": [],
            "important_females":[],
  }


  def get_population(self): #Determine population in a location.
    if self.variation  == "village":
      self.population = randrange(20, 301)
    elif self.variation == "town":
      self.population = randrange(300, 1001)
    elif self.variation  == "city":
      self.population = randrange(1000, 5001)
    elif self.variation  == "castle":
      self.population = randrange(5000, 10001)


  def living_check(self):
    if self.population <= 0:
      self.alive = False


  def get_full_name(self):
    if self.variation == "village":
      self.full_name = "The Village of {0}".format(self.name)
    elif self.variation == "town":
      self.full_name = "The Town of {0}".format(self.name)
    elif self.variation == "city":
      self.full_name = "The City of {0}".format(self.name)
    elif self.variation == "castle":
      self.full_name = "The Castle of {0}".format(self.name)


  def get_local_people(self, num_of_male, num_of_female):
    random_gender = ["male", "female"][randrange(0, 2)]
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
  
  def __init__(self, name, last_name, job):
    self.name = name
    self.last_name = last_name
    self.job = job

  alive = True

  def get_title(self):
    with open("./Resources/title_subfixes.txt", "r") as opened_file:
      lines = opened_file.readlines()
      nu_lines = []
      for i in lines:
        new = i.rstrip("\n")
        nu_lines.append(new)
      chosen_line = nu_lines[randrange(0, len(nu_lines))]
      self.title = chosen_line
      self.full_name = "{0} {1}".format(self.full_name, self.title)
#Grabs titles for people as subfixes


class Nobility(Person):
  """Specific actions for Nobility."""
  
  def __init__(self, name, last_name, job):
    self.name = name
    self.job = job              
    self.last_name = last_name
    self.full_name = "{0} {1} {2}".format(job, name, last_name)



class Commoner(Person):
  """Specific actions for Common People."""
  
  def __init__(self, name, last_name, job):
    self.name = name
    self.job = job
    self.last_name = last_name
    self.full_name = "{0} {1} the {2}".format(name, last_name, job)


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
      nu_lines = []
      for i in lines:
        new = i.rstrip("\n")
        nu_lines.append(new)
      chosen_line = nu_lines[randrange(0, len(nu_lines))]
      while dupe_check(namelist, chosen_line):
        chosen_line = nu_lines[randrange(0, len(nu_lines))]
      else:
        return chosen_line
        namelist.append(chosen_line)

  elif name_type == "location":
    with open("./Resources/location_names.txt", "r") as opened_file:
      lines = opened_file.readlines()
      nu_lines = []
      for i in lines:
        new = i.rstrip("\n")
        nu_lines.append(new)
      chosen_line = nu_lines[randrange(0, len(nu_lines))]
      while dupe_check(namelist, chosen_line):
        chosen_line = nu_lines[randrange(0, len(nu_lines))]
      else:
        return chosen_line
        namelist.append(chosen_line)

  elif name_type == "last":
    with open("./Resources/last_names.txt", "r") as opened_file:
      lines = opened_file.readlines()
      nu_lines = []
      for i in lines:
        new = i.rstrip("\n")
        nu_lines.append(new)
      chosen_line = nu_lines[randrange(0, len(nu_lines))]
      return chosen_line

  if name_type == "first":
    if gender == "male":
      with open("./Resources/male_names.txt", "r") as opened_file:
        lines = opened_file.readlines()
        nu_lines = []
        for i in lines:
          new = i.rstrip("\n")
          nu_lines.append(new)
        chosen_line = nu_lines[randrange(0, len(nu_lines))]
        while dupe_check(namelist, chosen_line):
          chosen_line = nu_lines[randrange(0, len(nu_lines))]
        else:
          return chosen_line
          namelist.append(chosen_line)

    elif gender == "female":
      with open("./Resources/female_names.txt", "r") as opened_file:
        lines = opened_file.readlines()
        nu_lines = []
        for i in lines:
          new = i.rstrip("\n")
          nu_lines.append(new)
        chosen_line = nu_lines[randrange(0, len(nu_lines))]
        while dupe_check(namelist, chosen_line):
          chosen_line = nu_lines[randrange(0, len(nu_lines))]
        else:
          return chosen_line
          namelist.append(chosen_line)
#Use this for random names at creation of place or person.

Test_Kingdom = Kingdom(get_name("kingdom", "none"))
Test_Kingdom.create_locations(5)
Test_Kingdom.populate_kingdom(5, 5, 5, 5, 5, 5)
Test_Kingdom.get_location_populations()
Test_Kingdom.get_total_population(Test_Kingdom.locations)
Test_Kingdom.king.get_title()

print(Test_Kingdom.king.full_name)
print(Test_Kingdom.queen.full_name)
for i in Test_Kingdom.people["princes"]:
  print(i.full_name)
for i in Test_Kingdom.people["princesses"]:
  print(i.full_name)

#print(Test_Kingdom.population)







