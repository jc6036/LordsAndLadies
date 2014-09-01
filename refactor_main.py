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

    def populate_king_queen(self):
        self.king = Nobility(
                             get_name("first", "male"),
                             get_name("last", "none"), "King"
                            )
        self.queen = Nobility(
                              get_name("first", "female"),
                              get_name("last", "none"), "Queen"
                             )
# Add king and queen objects to kingdom. Only one each per kingdom.
  

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
# Adds princes/princesses of an unlimited number, one gender at a time.


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
# Adds princes/princesses of an unlimited number, one gender at a time.


    def populate_important_person(self, number_of, gender):
        jobs = ["Blacksmith", "Tailor", "Farmer", "Cobbler", "Baker",
                "Scholar", "Barkeep", "Potter", "Butcher", "Bard"]

        if gender == "male":
            self.important_males = [
                                   Commoner(get_name("first", "male"),
                                   get_name("last", "none"),
                                   jobs[randrange(0, len(jobs))])
                                   for i in range(0, number_of)
                                   ]

        elif gender == "female":
            self.important_females = [
                                   Commoner(get_name("first", "female"),
                                   get_name("last", "none"),
                                   jobs[randrange(0, len(jobs))])
                                   for i in range(0, number_of)
                                     ]
 # Adds important commoners. Job i randomized; infinite number can be genned,
 # one gender at a time.
 

    def create_locations(self, number_of):
        variations = ["Town", "Village", "City", "Castle"]
        self.locations = [
                          Location(get_name("location", "none"),
                          variations[randrange(0, 4)])
                          for i in range(0, number_of)
                         ]
# Provides an infinite number of genned locations.

    def populate_kingdom(self, *args):
# Args is number of male children, female children, lords,
# ladies, male commoners, then female commoners. Use integers.
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
# Mainly used for an all-in-one population option.


    def get_location_populations(self):
        for i in self.locations:
            i.get_population()
# Must be used before get_total_population


    def get_total_population(self, location_list):
        self.population = 0
        for i in self.locations:
            self.population += i.population

    def fill_position(self, filename, place_filled):
# place_filled == either 'king' or 'queen'. Use to choose random prince
# Or princess to replace either the king or queen, respecitvely.
        if place_filled == "king":
            replacement = self.people["princes"] \
                          [randrange(0, len(self.people["princes"]))]
            self.king = replacement
            self.people["princes"].remove(replacement)
            opened_file = open("{0}".format(filename), "w")
            opened_file.write(
                "{0} succeeded his father on the throne.\n".format(
                replacement.full_name))  
            opened_file.close()

        elif place_filled == "queen":
            replacement = self.people["princesses"] \
                          [randrange(0, len(self.people["princesses"]))]
            self.queen = replacement
            self.people["princesses"].remove(replacement)
            opened_file = open("{0}".format(filename), "w")
            opened_file.write(
                "{0} succeeded her mother on the throne\n".format(
                replacement.full_name))
            opened_file.close()
# Didn't use with open() as var here for sake of line length.


class Location(Kingdom):
    """An object to represent locations such as villages and towns.
       Variation == 'village', 'town', 'city', or 'castle'"""

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

