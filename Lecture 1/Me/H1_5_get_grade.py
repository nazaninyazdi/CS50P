grade = float(input("Enter your grade: "))
if 100 < grade or 0 > grade:
    print("Invalid grade! ")
elif 90 <=  grade <= 100:
    print("Grade: A")
elif 80 <= grade < 90:
    print("Grade: B")
elif 70 <= grade < 80:
    print("Grade: C")
elif 60 <= grade < 70:
    print("Grade: D")
else:
    print("Grade: F")