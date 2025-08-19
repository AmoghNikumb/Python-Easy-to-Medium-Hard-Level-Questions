Coders = {"Arnav", "Goransh", "Mani", "Parul"}
Analysts = {"Krish", "Mehak", "Shiv", "Goransh", "Mani"}

# People who are both Coders and Analysts
code_analyst = Coders.intersection(Analysts)
print("List of coders as well as analysts:", code_analyst)

# People who are Coders or Analysts (union)
code_or_analyst = Coders.union(Analysts)
print("List of coders or analysts:", code_or_analyst)

# People who are Analysts but not Coders
only_analysts = Analysts.difference(Coders)
print("List of people who are Analysts but not Coders:", only_analysts)

# People who are Coders but not Analysts
only_coders = Coders.difference(Analysts)
print("List of people who are Coders but not Analysts:", only_coders)

# People working in only one of the groups (symmetric difference)
only_one_group = Coders.symmetric_difference(Analysts)
print("List of people working in only one of the groups:", only_one_group)
