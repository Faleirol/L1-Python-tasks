name = ["Evi", "Madeleine", "Aaron", "Kelsey", "Noah", "Hayley", "Darian"]
name.sort()
print(name)

Check_name = input("What name do you want to check?").strip().title()
if Check_name == Check_name:
    print("{} is already in the list".format(Check_name))
else:
    print("{} is not in the in the list".format(Check_name))
repeat = True
while repeat == True:
  Add_name = input("What name do you want to add?").strip().lower()

