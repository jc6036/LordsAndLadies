#Using this to simply fill up a text file with placeholder names

def fill_names(filename, num_of_names, variation, gender = "none"):

  if gender == "male":

    if variation == "first":
      with open("./%s" % str(filename), "w") as opened_file:
        for i in range(1, num_of_names + 1):
          opened_file.write("Male_Name %s\n" % str(i))

  elif gender == "female":

    if variation == "first":
      with open("./%s" % str(filename), "w") as opened_file:
        for i in range(1, num_of_names + 1):
          opened_file.write("Female_Name %s\n" % str(i))

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



def fill_titles(filename, num_of_titles, fix, job_type):
  
  if job_type == "noble":
    if fix == "prefix":
      with open("./%s" % str(filename), "w") as opened_file:
        for i in range(1, num_of_titles + 1):
          opened_file.write("Prefix_Title_Noble %s\n" % str(i))

    elif fix == "subfix":
      with open("./%s" % str(filename), "w") as opened_file:
        for i in range(1, num_of_titles + 1):
          opened_file.write("Subfix_Title_Noble %s\n" % str(i))

  elif job_type == "common":
    if fix == "prefix":
      with open("./%s" % str(filename), "w") as opened_file:
        for i in range(1, num_of_titles + 1):
          opened_file.write("Prefix_Title_Common %s\n" % str(i))

    elif fix == "subfix":
      with open("./%s" % str(filename), "w") as opened_file:
        for i in range(1, num_of_titles + 1):
          opened_file.write("Subfix_Title_Common %s\n" % str(i))


fill_names("male_names.txt", 500, "first", "male")
fill_names("female_names.txt", 500, "first", "female")
fill_names("last_names.txt", 250, "last", "none")

