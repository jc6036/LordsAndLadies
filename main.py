########################
#Lords and Ladies      #
#v0.0.a2               #
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


class Kingdom(object, name):
  """Contains the kingdoms"""
  
  def __init__(self, name):
    name = self.name
  

class Location(Kingdom, name, variation):
  """Various functions for locations in kingdoms"""
  
  def __init__(self, name, variation):
    name = self.name
    variation = self.variation


class ImportantPerson(object, name, job):
  """Standard template for a person"""
  
  def __init__(self, name, job):
    name = self.name
    job = self.job
