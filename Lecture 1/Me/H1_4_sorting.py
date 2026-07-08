first = float(input("Enter your first number: "))
second = float(input("Enter your second number: "))
third = float(input("Enter your third number: "))
if first <= second and first <= third:
    print(f"Your smallest number is {first}")
elif second <= first and second <= third:
    print(f"Your smallest number is {second}")
elif third <= first and third <= second:
    print(f"Your smallest number is {third}")
