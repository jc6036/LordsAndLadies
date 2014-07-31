# Lords And Ladies refactor
# by jc6036
# python 3.2
# contact at jc6036@gmail.com

from random import randrange

class Kingdom(object):
    """The kingdom object."""

    def __init__(self, name):
        self.name = name
        self.full_name = "The Kingdom of {0}".format(name)
        self.at_war = False

        self.people = {
            "princes": [],
            "princesses": [],
            "lords": [],
            "ladies": [],
            "important_males": [],
            "important_females": [],
        }

class Location(Kingdom):
    """An object to represent locations such as villages and towns."""

    def __init__(self, name, variation):
        self.name = name
        self.variation = variation
        self.full_name = "The {0} of {1}".format(variation, name)

        self.people = { #Container for location-specific named people.
                       "landlord": [],
                       "important_males": [],
                       "important_females":[],
        }

        self.alive = True

class Person(object):
    """Object representing people."""

    def __init__(self, name, last_name, job):
        self.name = name
        self.last_name = last_name
        self.job = job
        self.alive = True  #Changed when drastic event kills the person.

class Nobility(Person):
    """An object representing nobles."""
  
    def __init__(self, name, last_name, job):
        self.name = name
        self.job = job              
        self.last_name = last_name
        self.full_name = "{0} {1} {2}".format(job, name, last_name)

class Commoner(Person):
    """An object representing common people."""
  
    def __init__(self, name, last_name, job):
        self.name = name
        self.job = job
        self.last_name = last_name
        self.full_name = "{0} {1} the {2}".format(name, last_name, job)

