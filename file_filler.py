#Using this to simply fill up a text file with placeholder names

def fill_names(filename, num_of_names, variation):

  if variation == "noble":
    with open("./%s" % str(filename), "w") as opened_file:
      for i in range(1, num_of_names + 1):
        opened_file.write("Royal_Name %s\n" % str(i))
  
  elif variation == "common":
    with open("./%s" % str(filename), "w") as opened_file:
      for i in range(1, num_of_names + 1):
        opened_file.write("Common_Name %s\n" % str(i))

  elif variation == "last":
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




#fill_names("noble_names.txt", 200, "noble")
#fill_names("common_names.txt", 200, "common")
#fill_names("last_names.txt", 200, "last")
#fill_locations("location_names.txt", 200)
fill_names("kingdom_names.txt", 200, "kingdom")