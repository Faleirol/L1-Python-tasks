number = int(input("Enter a number"))

if number > 1:
    for i in range(2, number):
        if(number % i) == 0:
            print(f"{number} not a prime number")
            break
elif:
     print(f"{number} is a prime number")
