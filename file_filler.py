#Using this to simply fill up a text file with placeholder names

def fill_names(filename, num_of_names, variation, gender = "none"):

  if gender == "male":

    if variation == "noble":
      with open("./%s" % str(filename), "w") as opened_file:
        for i in range(1, num_of_names + 1):
          opened_file.write("Male_Royal_Name %s\n" % str(i))
  
    elif variation == "common":
      with open("./%s" % str(filename), "w") as opened_file:
        for i in range(1, num_of_names + 1):
          opened_file.write("Male_Common_Name %s\n" % str(i))

  elif gender == "female":

    if variation == "noble":
      with open("./%s" % str(filename), "w") as opened_file:
        for i in range(1, num_of_names + 1):
          opened_file.write("Female_Royal_Name %s\n" % str(i))
  
    elif variation == "common":
      with open("./%s" % str(filename), "w") as opened_file:
        for i in range(1, num_of_names + 1):
          opened_file.write("Female_Common_Name %s\n" % str(i))

  else:
    if variation == "last":
      with open("./%s" % str(filename), "w") as opened_file:
        for i in range(1, num_of_names + 1):
          opened_file.write("Last_Name %s\n" % str(i))

    elif variation == "kingdom":
      with open("./%s" % str(filename), "w") as opened_file:
        for i in range(1, num_of_names + 1):
          opened_file.write("Kingdom_Name %s\n" % str(i))




def fill_locations(filename, num_of_names):

  with open("./%s" % str(filename), "w") as opened_file:
    for i in range(1, num_of_names + 1):
      opened_file.write("Test_Location %s\n" % str(i))



fill_names("male_common_names.txt", 200, "common", "male")
fill_names("female_common_names.txt", 200, "common", "female")
fill_names("male_noble_names.txt", 200, "noble", "male")
fill_names("female_noble_names.txt", 200, "noble", "male")