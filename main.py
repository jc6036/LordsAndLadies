########################
#Lords and Ladies      #
#v0.0.a5               #
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
  king = Nobility(get_name("person"))
  queen = Nobility(get_name("person"))
#Creates the basic Kingdom. Expand using functions.Kingdom.


class Kingdom(object, name):
  """Contains the kingdoms"""
  
  def __init__(self, name):
    name = self.name
#For creation of Kindoms.
  


class Location(Kingdom, name, variation):
  """Various functions for locations in kingdoms"""
  #Variation == village, town, city, or castle.
  
  def __init__(self, name, variation):
    name = self.name
    variation = self.variation
#Location creator.



class Person(object, name, name_type):
  """Function holder for people."""
  
  def __init__(self, name, job):
    name = self.name
    job = self.job

  def title_get(self, name_type):
    if self.name_type == "nobility":
      with open("placeholder", -r) as line:
        return line
    elif self.name_type == "influential":
      with open("placeholder", -r) as line:
        return line
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













