name = input("What's your name? ")
age = int(input("How old are you? "))
if age < 18:
    print("You're still a student! ")
elif age >= 18:
    print("Good luck! ")
print(f"Have a good day, {name}!")