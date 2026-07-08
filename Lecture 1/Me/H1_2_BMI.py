name = input("Enter your name: ")
height = float(input("Enter your height (m): "))
weight = float(input("Enter your weight (kg): "))

bmi = weight / (height ** 2)


if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obese")

print(f"Your BMI is {bmi:.2f}, dear {name}.")

print("Division by zero!")