################################################
#Lords and Ladies                              #
#v0.0.c2                                       #
#Authored by jc6036                            #
#Python 3.2 with the random module             #
################################################

from random import randrange


class Kingdom(object):
    """Contains the kingdoms and fucntions to populate."""

    def __init__(self, name):
        self.name = name
        self.full_name = "The Kingdom of {0}".format(name)
        self.at_war = False

        self.people = {  #Needed for randomization.
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
#Adds princes/princesses of an unlimited number, one gender at a time.


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
#Adds princes/princesses of an unlimited number, one gender at a time.


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
 #Adds important commoners. Job i randomized; infinite number can be genned,
 #one gender at a time.
 

    def create_locations(self, number_of):
        variations = ["Town", "Village", "City", "Castle"]
        self.locations = [
                          Location(get_name("location", "none"),
                          variations[randrange(0, 4)])
                          for i in range(0, number_of)
                         ]
#Provides an infinite number of genned locations.

# Note that despite usage of the word infinite, using very large numbers is not
# recommended for the sake of speed and health of your processor.


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
#Mainly used for an all-in-one population option.


    def get_location_populations(self):
        for i in self.locations:
            i.get_population()
#Must be used before get_total_population


    def get_total_population(self, location_list):
        self.population = 0
        for i in self.locations:
            self.population += i.population


#Functions that write to file are below
#####

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
#Didn't use with open() as var here for sake of line length.


class Location(Kingdom):
    """Various functions for locations in kingdoms
     Variation == 'village', 'town', 'city', or 'castle'
    """

  
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


#Functions that write to file are below
#####

    def natural_disaster(self, filename):
        disasters = ["a tornado", "a hurricane", "a blizzard",
                     "a lightning storm", "flooding",
                     "an earthquake", "a tsunami"]

        with open("./Output/{0}".format(filename), "w") as opened_file:
            self.population = self.population - randrange(50, 5000)
            if self.population <= 0:
                opened_file.write(
                "{0} was destroyed by {1}\n" \
                .format(self.full_name, disasters[randrange(0, 7)]
                ))

                self.alive = False
                for i in self.people:
                    for item in i:
                        item.alive = False
            else:
                opened_file.write(
            "{0} was damaged by {1}, reducing the population to {2}\n".format(
            self.full_name, disasters[randrange(0, 7)], self.population)
            )
#Be sure to use get_total_population for the kingdom after using this.


    def local_fill_position(self):
#Same as fill_position, but does so for the local lords and ladies.
        genders = ["male", "female"]
        gender = genders[randrange(0, 2)]

        if gender == "male":
            males = self.people["important_males"]
            chosen_male = males[randrange(0, len(males))]
            self.people["landlord"] = chosen_male
            self.people["important_males"].remove(chosen_male)

        elif gender == "female":
            females = self.people["important_females"]
            chosen_female = females[randrange(0, len(males))]
            self.people["landlord"] = chosen_female
            self.people["important_males"].remove(chosen_female)



class Person(object):
    """Function holder for people."""
  
    def __init__(self, name, last_name, job):
        self.name = name
        self.last_name = last_name
        self.job = job
        self.alive = True  #Changed when drastic event kills the person.


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

#Functions that write to file are below
#####

    def kill_person(self, filename, killer):
# Killer describes the way the person dies. killer takes 'assassination',
# 'illness', 'war', and 'natural_disaster' currently.
        if killer == "assassination":
            self.alive = False
            with open("./Output/{0}".format(filename), "w") as opened_file:
                opened_file.write("{0} was assassinated.\n".format(
                self.full_name))

        elif killer == "illness":
            self.alive = False
            with open("./Output/{0}".format(filename), "w") as opened_file:
                opened_file.write("{0} died due to illness.\n".format(
                self.full_name))

        elif killer == "war":
            self.alive = False
            with open("./Output/{0}".format(filename), "w") as opened_file:
                opened_file.write("{0} died as a casulty of war.".format(
                self.full_name))

        elif killer == "natural_disaster":
            self.alive = False
            with open("./Output/{0}".format(filename), "w") as opened_file:
                opened_file.write("{0} died in a natural disaster.".format(
                self.full_name))



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

kingdoms = []  #Used to contain kingdom objects for randomization reasons


def dupe_check(namelist, name):

    for i in namelist:
        if name == i:
            return True
        else:
            return False
#For seeing if a name is already in use.


def get_name(name_type, gender):
#Name_type can be kingdom, location, last, or first.
#Gender is either male or female if name_type is first. Otherwise, use 'none'.

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
                if len(namelist) >= 200: 
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
# Use this for random names at creation of place or person. get_name clears
# 'namelist' after it has 200 names in it automatically.


def kingdom_gen(index_num):
# Designed to run and allow user to determine some variables.
# index_num is the slice in 'kingdoms' this kingdom is located on and will be
# needed for randomization reasons.
    name_check = input(
    "Please enter the name of the kingdom. 'random' will gen a random name.\n"
    )

    if name_check == "random":
        Genned_Kingdom = Kingdom(get_name("kingdom", "none"))
    else:
        Genned_Kingdom = Kingdom(name_check)

    kingdoms.append(Genned_Kingdom)

    size = input("Please choose a size: XS, S, M, L, XL.\n").lower()

    if size == "xs":
        Genned_Kingdom.create_locations(randrange(1, 6))
        Genned_Kingdom.populate_kingdom(randrange(1, 4),
                                        randrange(1, 4),
                                        randrange(5, 11),
                                        randrange(5, 11),
                                        randrange(10, 16),
                                        randrange(10, 16))
        Genned_Kingdom.get_location_populations()
        Genned_Kingdom.get_total_population(Genned_Kingdom.locations)
    elif size == "s":
        Genned_Kingdom.create_locations(randrange(5, 11))
        Genned_Kingdom.populate_kingdom(randrange(2, 7),
                                        randrange(2, 7),
                                        randrange(10, 16),
                                        randrange(10, 16),
                                        randrange(15, 21),
                                        randrange(15, 21))
        Genned_Kingdom.get_location_populations()
        Genned_Kingdom.get_total_population(Genned_Kingdom.locations)
    elif size == "m":
        Genned_Kingdom.create_locations(randrange(10, 16))
        Genned_Kingdom.populate_kingdom(randrange(2, 10),
                                        randrange(2, 10),
                                        randrange(15, 21),
                                        randrange(15, 21),
                                        randrange(20, 26),
                                        randrange(20, 26))
        Genned_Kingdom.get_location_populations()
        Genned_Kingdom.get_total_population(Genned_Kingdom.locations)
    elif size == "l":
        Genned_Kingdom.create_locations(randrange(15, 21))
        Genned_Kingdom.populate_kingdom(randrange(2, 16),
                                        randrange(2, 16),
                                        randrange(20, 26),
                                        randrange(20, 26),
                                        randrange(25, 31),
                                        randrange(25, 31))
        Genned_Kingdom.get_location_populations()
        Genned_Kingdom.get_total_population(Genned_Kingdom.locations)
    elif size == "xl":
        Genned_Kingdom.create_locations(randrange(20, 26))
        Genned_Kingdom.populate_kingdom(randrange(2, 21),
                                        randrange(2, 21),
                                        randrange(25, 31),
                                        randrange(25, 31),
                                        randrange(30, 36),
                                        randrange(30, 36))
        Genned_Kingdom.get_location_populations()
        Genned_Kingdom.get_total_population(Genned_Kingdom.locations)
    else:
        Genned_Kingdom.create_locations(randrange(10, 16))
        Genned_Kingdom.populate_kingdom(randrange(2, 10),
                                        randrange(2, 10),
                                        randrange(15, 21),
                                        randrange(15, 21),
                                        randrange(20, 26),
                                        randrange(20, 26))
        Genned_Kingdom.get_location_populations()
        Genned_Kingdom.get_total_population(Genned_Kingdom.locations)
# If no size is defined or the input doesn't match the logic, the genner
# defaults to 'm' or 'medium' as the size.


def multiple_kingdom_gen():
    for i in range(0, int(input("How many kingdoms?\n"))):
        kingdom_gen(i)



def output_kingdom_content(kingdom, filename):
# kingdom is object name being described in the text file.
# Currently kingdom should be passed as kingdoms[index_num] for randomization
# reasons.
    with open("./Output/{0}".format(filename), "w") as opened_file:
        opened_file.write("{0}\nPopulation: {1}\n".format(
                           kingdom.full_name, kingdom.population))

        king_name = kingdom.king.full_name
        queen_name = kingdom.queen.full_name
        opened_file.write(
            "Your King is {0}. Your Queen is {1}.\n".format(
             king_name, queen_name)
        )
        opened_file.write("\n")
        opened_file.write("----------\n")
        opened_file.write("\n")  

        princes = kingdom.people["princes"]
        princesses = kingdom.people["princesses"]
        opened_file.write(
            "The {0}'s noble children are as follows:\n".format(
             kingdom.full_name)
        )
        for i in princes:
            opened_file.write("{0}\n".format(i.full_name))
        for i in princesses:
            opened_file.write("{0}\n".format(i.full_name))
        opened_file.write("\n")
        opened_file.write("----------\n")
        opened_file.write("\n")

        lords = kingdom.people["lords"]
        ladies = kingdom.people["ladies"]
        opened_file.write(
            "\nThe {0}'s lords and ladies are as follows:\n".format(
             kingdom.full_name)
        )
        for i in lords:
            opened_file.write("{0}\n".format(i.full_name))
        for i in ladies:
            opened_file.write("{0}\n".format(i.full_name))
        opened_file.write("\n")
        opened_file.write("----------\n")
        opened_file.write("\n")

        males = kingdom.people["important_males"]
        females = kingdom.people["important_females"]
        opened_file.write(
            "The {0}'s notable commoners are as follows:\n".format(
             kingdom.full_name)
        )
        for i in males:
            opened_file.write("{0}\n".format(i.full_name))
        for i in females:
            opened_file.write("{0}\n".format(i.full_name))
        opened_file.write("\n")
        opened_file.write("----------\n")
        opened_file.write("\n")


        opened_file.write(
            "The {0}'s locations are as follows:\n".format(
             kingdom.full_name)
        )
        for i in kingdom.locations:
            opened_file.write(
                "{0}, with a population of {1}.\n".format(
                i.full_name, i.population)
            )
            opened_file.write(
                "Landlord: {0}\n".format(
                 i.people["landlord"][0].full_name)
            )
            opened_file.write("\n")
            opened_file.write("Notable males and females:\n")
            for people in i.people["important_males"]:
                opened_file.write("{0}\n".format(people.full_name))
            for people in i.people["important_females"]:
                opened_file.write("{0}\n".format(people.full_name))
            opened_file.write("\n")
            opened_file.write("----------\n")
            opened_file.write("\n")

        opened_file.write("\n")
        opened_file.write("\n")
        opened_file.write("----------==========----------\n")
        opened_file.write("\n")
        opened_file.write("\n")


def create_war(kingdom_1, kingdom_2, filename):
#This creates a war between two kingdoms and outputs it to the output file.
    kingdom_1.at_war = True
    kingdom_2.at_war = True
    
    with open("/Output/{0}".format(filename), "w") as opened_file:
        opened_file.write(
            "The war of {0} and {1} began.\n".format(
            kingdom_1.full_name, kingdom_2.full_name
        ))


def war_destruction(filename):
#This chooses a random location in each kingdom that's currently at war and
#destroys it.
    for kingdom in kingdoms:
        if kingdom.at_war == True:
            location = kingdom.locations[randrange(0, len(locations))]
            location.alive = False
            with open("/Output/{0}".format(filename), "w") as opened_file:
                opened_file.write(
                    "{0} was destroyed as a result of war.\n".format(
                    location.full_name)
                )


def end_wars(filename):
#Ends all wars going on.
    for kingdom in kingdoms:
        kingdom.at_war = False
    with open("/Output/{0}".format(filename), "w") as opened_file:
        opened_file.write(
            "The kingdoms came to an agreement and ended the wars going on.\n"
        )


def revolution(kingdom, filename):
#Causes revolution, usurps current king and queen with commoners.
    kingdom.king.alive = False
    kingdom.queen.alive = False
    new_male = kingdom.people["important_males"][randrange(
               0, len(kingdom.people["important_males"]))]
    new_female = kingdom.people["important_females"][randrange(
                 0, len(kingdom.people["important_female"]))]
    with open("/Output/{0}".format(filename), "w") as opened_file:
        opened_file.write(
          "{0} underwent a coupe. {1} and {2} replaced the king and queen.\n" \
            .format(kingdom.full_name,
                    new_male.full_name,
                    new_female.full_name)
        )
    kingdom.king = new_male
    kingdom.queen = new_female
    kingdom.people["important_males"].remove(new_male)
    kingdom.people["important_females"].remove(new_female)


def cleanup_lists():
#Loops through every list and removes objects that are dead (alive == False)
    for kingdom in kingdoms:
        for people in kingdom.people:
            for item in people:
                if item.alive == False:
                    people.remove(item)
        for location in kingdom.locations:
            for people in location.people:
                for item in people:
                    if item.alive == False:
                        people.remove(item)
            if location.alive == False:
                locations.remove(location)


def adultery(kingdom, variation, filename):
#Variation = king, queen, lord, or lady
    with open("/Output/{0}".format(filename), "w") as opened_file:
        if variation == "king":
            cheater = kingdom.people["important_females"][
                      randrange(0, len(kingdom.people["important_females"]))]
            opened_file.write(
                "{0} was caught in an act of infidelity with {1}.\n".format(
                kingdom.king.full_name, cheater.full_name)
            )
        
        elif variation == "queen":
            cheater = kingdom.people["important_males"][
                      randrange(0, len(kingdom.people["important_males"]))]
            opened_file.write(
                "{0} was caught in an act of infidelity with {1}.\n".format(
                 kingdom.queen.full_name, cheater.full_name)
            )

        elif variation == "lord":
            cheater = kingdom.people["important_males"][
                      randrange(0, len(kingdom.people["important_females"]))]
            lord = kingdom.people["lords"][
                   randrange(0, len(kingdom.people["lords"]))]
            opened_file.write(
                "{0} was caught in an act of infidelity with {1}\n".format(
                 lord.full_name, cheater.full_name)
            )

        elif variation == "lady":
            cheater = kingdom.people["important_males"][
                      randrange(0, len(kingdom.people["important_males"]))]
            lady = kingdom.people["ladies"][
                   randrange(0, len(kingdom.people["ladies"]))]
            opened_file.write(
                "{0} was caught in an act of infidelity with {1}\n".format(
                 lady.full_name, cheater.full_name)
            )


def output_year_of_drama(upper_limit, filename):
#upper_limit is the maximum events in this single year.
    global kingdoms
    length = len(kingdoms)
    ordinary_drama_types = ["adultery", "illness_death"]
    rare_drama_types = ["natural_disaster", "war_destruction"]
    ultra_rare_drama_types = ["assassination_death", "start_war", "revolution"]
#Uses a roll of 100 to determine drama rarity

    for drama in range(0, upper_limit):
        roll = randrange(0, 101)
        if roll <= 60:
            random_drama_type = ordinary_drama_types[
                                    randrange(0, len(ordinary_drama_types))
                                ]
        elif roll >= 61 and roll <= 85:
            random_drama_type = rare_drama_types[
                                    randrange(0, len(rare_drama_types))
                                ]
        elif roll >= 86:
            random_drama_type = ultra_rare_drama_types[
                                    randrange(0, len(ultra_rare_drama_types))
                                ]

        if random_drama_type == "natural_disaster":
            affected_loc = kingdoms[randrange(0, length)].locations[
                           randrange(0, len(locations))]
            affected_loc.natural_disaster(filename)
            affected_group = kingdoms[randrange(0, length)].people[[
                             "lords", "ladies", "important_males",
                             "important_females"][randrange(0, 4)]]
            affected_person = affected_group[randrange(0, len(affected_group))
                              ]
            affected_person.kill_person(filename, "natural_disaster")
            cleanup_lists()
#natural_disasters can't kill kings or queens currently

        elif random_drama_type == "illness_death":            
            roll = randrange(0, 101)
            if roll > 80:
                choice = ["king", "queen"][randrange(0, 2)]
                if choice == "king":
                    kingdom = kingdoms[randrange(0, length)
                                      ]
                    affected_person = kingdom.king
                    affected_person.kill_person(filename, "illness")
                    kingdom.fill_position(filename, "king")
                elif choice == "queen":
                    kingdom = kingdoms[randrange(0, length)
                                      ]
                    affected_person = kingdom.queen
                    affected_person.kill_person(filename, "illness")
                    kingdom.fill_position(filename, "queen")
            else:
                affected_group = kingdoms[randrange(0, length)].people[
                                 ["lords", "ladies", "important_males",
                                 "important_females", "princes", "princesses"][
                                 randrange(0, 6)]
                                 ]
                affected_person = affected_group[
                                  randrange(0, len(affected_group))
                                  ]
                affected_person.kill_person(filename, "illness")
            cleanup_lists()
#illness can kill anybody. Dead kings and queens will be replaced.

        elif random_drama_type == "assassination_death":
            roll = randrange(0, 101)
            if roll > 75:
                choice = ["king", "queen"][randrange(0, len(choice))]
                if choice == "king":
                    kingdom = kingdoms[randrange(0, length)
                    ]
                    affected_person = kingdom.king
                    affected_person.kill_person(filename, "assassination")
                    kingdom.fill_position(filename, "king")
                elif choice == "queen":
                    kingdoms = kingdoms[randrange(0, length)
                    ]
                    affected_person = kingdom.queen
                    affected_person.kill_person(filename, "assassination")
                    kingdom.fill_position(filename, "queen")
            else:
                affected_group = kingdoms[randrange(0, length)].people[
                                 ["lords", "ladies", "princes", "princesses"][
                                 randrange(0, 4)]
                                 ]
                affected_person = affected_group[randrange(0, len(
                                  affected_group))]
                affected_person.kill_person(filename, "assassination")
            cleanup_lists()
#commoners are spared from assassinations. Everyone else is fair game.

        elif random_drama_type == "revolution":
            revolution(kingdoms[randrange(0, length)], filename)
            cleanup_lists()

        elif random_drama_type == "adultery":
            kingdom = kingdoms[randrange(0, length)]
            roll = randrange(0, 500)
            if roll < 425:
                adultery(kingdom, ["lord", "lady"][randrange(0, 2)], filename)
            elif roll >= 425:
                adultery(kingdom, ["king", "queen"][randrange(0, 2)], filename)
            cleanup_lists()

        elif random_drama_type == "start_war":
            all_at_war = False
            for kingdom in kingdoms:
                if kingdom.at_war == False:
                    kingdom = kingdom_1
                    break
            else:
                all_at_war = True
            for kingdom in kingdoms:
                if kingdom.at_war == False:
                    kingdom = kingdom_2
                    break
            else:
                if all_at_war == True:
                    end_wars(filename)
            if all_at_war == False:
                create_war(kingdom_1, kingdom_2, filename)
            elif all_at_war == True:
                all_at_war == False
#this will actually end all current wars if there aren't two kingdoms
#available to begin a new war

        elif random_drama_type == "war_destruction":
            war_destruction(filename)
            for kingdom in kingdoms:
                if kingdom.at_war == True:
                    roll = randrange(0, 101)
                    if roll > 80:
                        affected_person = [kingdom.king, kingdom.queen][
                                           randrange(0, 2)]
                    else:
                        affected_group = kingdom.people[["lords",
                                         "ladies",
                                         "important_males",
                                         "important_females"][
                                         randrange(0, 4)]
                                         ]
                        affected_person = affected_group[randrange(0, len(
                                          affected_group))
                                          ]
                affected_person.kill_person(filename, "war")
                if kingdom.king.alive == False:
                    kingdom.fill_position(filename, "king")
                elif kingdom.queen.alive == False:
                    kingdom.fill_position(filename, "queen")
            cleanup_lists()
#Kills a random person for each kingdom at war and destroys a location each.


def main_output(filename):
    multiple_kingdom_gen()
    choice = input(
    "Would you like to create files listing the contents of the kingdoms?y/n\n"
    )
    if choice == "y" or choice == "Y":
        for i in kingdoms:
            output_kingdom_content(i, "Contents_{0}".format(i.name))


multiple_kingdom_gen()
for i in kingdoms:
    output_kingdom_content(i, "Contents_{0}".format(i.name))
#for i in kingdoms:
#    output_kingdom_content(i, "Contents_{0}".format(i.name))



#Current issues|
#1. For whatever reason, my output functions overwrite what's already
#   in a file instead of adding to it. This is going to need fixed somehow.










