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

    self.people = {  #Container for the various named people
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
                         get_name("last", "none"), "King"
                        )
    self.queen = Nobility(
                          get_name("first", "female"),
                          get_name("last", "none"), "Queen"
                         )
#Add king and queen objects to kingdom. Only one each per kingdom.
  

  def populate_noble_children(self, number_of, gender):
    if gender == "male":
      self.princes = [
                    Nobility(get_name("first", "male"),
                    self.king.last_name, "Prince")
                    for i in range(0, number_of)
                     ]

    elif gender == "female":
      self.princesses = [
                    Nobility(get_name("first", "female"),
                    self.king.last_name,"Princess")
                    for i in range(0, number_of)
                        ]
#Add prince and princess objects to kingdom.  


  def populate_landlords(self, number_of, gender):
    if gender == "male":
      self.lords = [
                    Nobility(get_name("first", "male"),
                    get_name("last", "none"), "Lord")
                    for i in range(0, number_of)
                   ]

    elif gender == "female":
      self.ladies = [
                    Nobility(get_name("first", "female"),
                    get_name("last", "none"), "Lady")
                    for i in range(0, number_of)
                    ]
#Add lords and lady objects to the kingdom.  


  def populate_important_person(self, number_of, gender):
    jobs = ["Blacksmith", "Tailor", "Farmer", "Cobbler", "Baker"]

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
    variations = ["Town", "Village", "City", "Castle"]
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



class Location(Kingdom):
  """Various functions for locations in kingdoms"""
  #Variation == village, town, city, or castle.
  
  def __init__(self, name, variation):
    self.name = name
    self.variation = variation
    self.full_name = "The {0} of {1}".format(variation, name)

    self.people = {  #Container for location-specific named people.
                  "landlord": [],
                  "important_males": [],
                  "important_females":[],
    }

    self.alive = True


  def get_population(self): #Determine population in a location.
    if self.variation  == "Village":
      self.population = randrange(20, 301)
    elif self.variation == "Town":
      self.population = randrange(300, 1001)
    elif self.variation  == "City":
      self.population = randrange(1000, 5001)
    elif self.variation  == "Castle":
      self.population = randrange(5000, 10001)


  def living_check(self):
    if self.population <= 0:
      self.alive = False


  def get_local_people(self, num_of_male, num_of_female):
#num_of_male and num_of_male applies to commoners. Landlord is random gender.
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

  alive = True  #Changed when drastic event kills the person.

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

kingdoms = []  #Used to contain kingdom objects

def dupe_check(namelist, name):

  for i in namelist:
    if name == i:
      return True
    else:
      return False
#For seeing if a name is already in use.


def get_name(name_type, gender):
#Name_type can be kingdom, location, last, or first.
#Gender is either male or female if name_type is firt. Otherwise, use 'none'.

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
        if len(namelist) >= 200:  #Resets namelist if more than 200 names within
          namelist.remove(namelist[:])

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
        if len(namelist) >= 200:
          namelist.remove(namelist[:])

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
          if len(namelist) >= 200:
            namelist.remove(namelist[:])

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
          if len(namelist) >= 200:
            namelist.remove(namelist[:])
#Use this for random names at creation of place or person.


def kingdom_gen():
#Designed to run and allow user to determine some variables.
#index_num is the slice in 'kingdoms' this kingdom is located on.
  name_check = input("Please enter the name of the kingdom. 'random' will gen a random name.\n")

  if name_check == "random":
    Genned_Kingdom = Kingdom(get_name("kingdom", "none"))
  else:
    Genned_Kingdom = Kingdom(name_check)

  kingdoms.append(Genned_Kingdom)

  size = input("Please choose a size: XS, S, M, L, XL.\n").lower()

  if size == "xs":  #Extra Small
    Genned_Kingdom.create_locations(randrange(1, 6))
    Genned_Kingdom.populate_kingdom(randrange(1, 4),
                             randrange(1, 4),
                             randrange(5, 11),
                             randrange(5, 11),
                             randrange(10, 16),
                             randrange(10, 16))
    Genned_Kingdom.get_location_populations()
    Genned_Kingdom.get_total_population(Genned_Kingdom.locations)
  elif size == "s":  #Small
    Genned_Kingdom.create_locations(randrange(5, 11))
    Genned_Kingdom.populate_kingdom(randrange(2, 7),
                             randrange(2, 7),
                             randrange(10, 16),
                             randrange(10, 16),
                             randrange(15, 21),
                             randrange(15, 21))
    Genned_Kingdom.get_location_populations()
    Genned_Kingdom.get_total_population(Genned_Kingdom.locations)
  elif size == "m":  #Medium
    Genned_Kingdom.create_locations(randrange(10, 16))
    Genned_Kingdom.populate_kingdom(randrange(2, 10),
                             randrange(2, 10),
                             randrange(15, 21),
                             randrange(15, 21),
                             randrange(20, 26),
                             randrange(20, 26))
    Genned_Kingdom.get_location_populations()
    Genned_Kingdom.get_total_population(Genned_Kingdom.locations)
  elif size == "l":  #Large
    Genned_Kingdom.create_locations(randrange(15, 21))
    Genned_Kingdom.populate_kingdom(randrange(2, 16),
                             randrange(2, 16),
                             randrange(20, 26),
                             randrange(20, 26),
                             randrange(25, 31),
                             randrange(25, 31))
    Genned_Kingdom.get_location_populations()
    Genned_Kingdom.get_total_population(Genned_Kingdom.locations)
  elif size == "xl":  #Extra Large
    Genned_Kingdom.create_locations(randrange(20, 26))
    Genned_Kingdom.populate_kingdom(randrange(2, 21),
                             randrange(2, 21),
                             randrange(25, 31),
                             randrange(25, 31),
                             randrange(30, 36),
                             randrange(30, 36))
    Genned_Kingdom.get_location_populations()
    Genned_Kingdom.get_total_population(Genned_Kingdom.locations)
  else:  #Defaults to medium if no recognizable size entered.
    Genned_Kingdom.create_locations(randrange(10, 16))
    Genned_Kingdom.populate_kingdom(randrange(2, 10),
                             randrange(2, 10),
                             randrange(15, 21),
                             randrange(15, 21),
                             randrange(20, 26),
                             randrange(20, 26))
    Genned_Kingdom.get_location_populations()
    Genned_Kingdom.get_total_population(Genned_Kingdom.locations)


def output_kingdom_content(kingdom, filename):
#kingdom is object name being described in the text file.
#Filename is exactly what it says on the tin.
  with open("./Output/{0}".format(filename), "w") as opened_file:
    opened_file.write("{0}\nPopulation: {1}\n".format(kingdom.full_name, kingdom.population))

    king_name = kingdom.king.full_name
    queen_name = kingdom.queen.full_name
    opened_file.write("Your King is {0}. Your Queen is {1}.\n".format(king_name, queen_name))
    opened_file.write("\n")

    princes = kingdom.people["princes"]
    princesses = kingdom.people["princesses"]
    opened_file.write("The {0}'s noble children are as follows:\n".format(kingdom.full_name))
    for i in princes:
      opened_file.write("{0}\n".format(i.full_name))
    for i in princesses:
      opened_file.write("{0}\n".format(i.full_name))
    opened_file.write("\n")    

    lords = kingdom.people["lords"]
    ladies = kingdom.people["ladies"]
    opened_file.write("\nThe {0}'s lords and ladies are as follows:\n".format(kingdom.full_name))
    for i in lords:
      opened_file.write("{0}\n".format(i.full_name))
    for i in ladies:
      opened_file.write("{0}\n".format(i.full_name))
    opened_file.write("\n")

    males = kingdom.people["important_males"]
    females = kingdom.people["important_females"]
    opened_file.write("The {0}'s notable commoners are as follows:\n".format(kingdom.full_name))
    for i in males:
      opened_file.write("{0}\n".format(i.full_name))
    for i in females:
      opened_file.write("{0}\n".format(i.full_name))
    opened_file.write("\n")


    opened_file.write("The {0}'s locations are as follows:\n".format(kingdom.full_name))
    for i in kingdom.locations:
      opened_file.write("{0}, with a population of {1}.\n".format(i.full_name, i.population))
      opened_file.write("Landlord: {0}\n".format(i.people["landlord"][0].full_name))
      opened_file.write("Notable males and females:\n")
      for people in i.people["important_males"]:
        opened_file.write("{0}\n".format(people.full_name))
      for people in i.people["important_females"]:
        opened_file.write("{0}\n".format(people.full_name))

      opened_file.write("\n")

kingdom_gen()
output_kingdom_content(kingdoms[0], "Kingdom_Contents_Demo")












