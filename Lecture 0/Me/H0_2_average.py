total = 0 
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
    print("You need to try harder.")