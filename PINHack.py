pin = int(input("Please enter your pin number"))
i = 0
while i < pin:
    print(str(i).zfill(4))
    i += 1
pin = str(i).zfill(4)
print("Your pin is {}".format(pin))
