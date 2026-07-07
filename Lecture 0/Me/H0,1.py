'''name = input("What's your name? ")
age = int(input("How old are you? "))
place = input("Where are you from? ")
major = input("What's your favorite major? ")
print(f"Hello, {name}! You are {age} years old and you are from {place}, and also your favorite major is {major}. Nice to meet you!")'''

'''total = 0 
g = int(input("How many grades do you have? "))
for i in range (g):
    grade = float(input("Enter your grade: "))
    total += grade
a = total / g
if a >= 18:
    print("Well done!")
elif 15 <= a and a < 18:
    print("Good!")
else:
    print("You need to try harder.")'''

'''password = input("Enter your password: ")
for i in password:
    print("*", end = "")'''

'''password = input("Password: ")
if password:
    print("You entered something.")
else:
    print("Password is empty.")'''

name = input("What's your name? ")
age = int(input("How old are you? "))
if age < 18:
    print("You're still a student! ")
elif age >= 18:
    print("Good luck! ")
print(f"Have a good day, {name}!")