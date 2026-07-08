name = input("What's your name? ")
match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Gryfindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who? ")