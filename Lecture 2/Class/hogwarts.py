students = [
    {"Name": "Hermione", "House": "Gryffindor", "Patronus": "Other" },
    {"Name": "Harry", "House": "Gryffindor", "Patronus": "Stag"},
    {"Name": "Ron", "House": "Fryffindor", "Patronus": "Jack Russel terrier"},
    {"Name": "Draco", "House": "Slytherin", "Patronus": None}
]
for student in students:
    print(student["Name"], student["House"], student["Patronus"], sep = " ")
