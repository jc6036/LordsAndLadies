########################
#Lords and Ladies      #
#v0.0.a8               #
#Authored by jc6036    #
#Python 3.2 with       #
#Tkinter, ttk and      #
#Random modules        #
########################

from random import randint
from tkinter import *
import ttk

def get_name(name_type): 
  if name_type == "kingdom":
    with open("placeholder", -r) as opened_file:
      lines = opened_file.readlines()
      return lines[randint(0, 201)]

  elif name_type == "location":
    with open("placeholder", -r) as opened_file:
      lines = opened_file.readlines()
      return lines[randint(0, 201)]

  elif name_type == "person":
    with open("placeholder", -r) as opened_file:
      lines = opened_file.readlines()
      return lines[randint(0, 201)]
#Use this for random names at creation of place or person.


def create_base_kingdom(name):
  name = Kingdom(get_name("kingdom"))
#Creates the basic Kingdom. Expand using functions.Kingdom.


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
  
  def create_location(self, identifier):
    places = ["village", "town", "city", "castle"]
    chosen_place = places[randint(0, 5)]
    
    identifier = Location(get_name("location"), chosen_place)
#For creation of Kingdoms/Populatio/Locations.
  

class Location(Kingdom, name, variation):
  """Various functions for locations in kingdoms"""
  #Variation == village, town, city, or castle.
  
  def __init__(self, name, variation):
    name = self.name
    variation = self.variation
#Location creator.


class Person(object, name, name_type):
  """Function holder for people."""
  
  def __init__(self, name):
    name = self.name
    name_type = self.name_type

  def title_get(self, name_type):
    if name_type == "nobility":
      with open("placeholder", -r) as opened_file:
        lines = opened_file.readline()
        return lines[randint(1, 51)]

    elif name_type == "influential":
      with open("placeholder", -r) as opened_file:
        lines = opened_file.readline()
        return lines[randint(1, 51)]
#Grabs titles for the names of people.


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





#For main logic loop: figure out algorithm to generate
#multiple people with different identifiers for
#the ability to have more than one object of the same
#type generated automatically.