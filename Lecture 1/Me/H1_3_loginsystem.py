username = "admin"
password = "python123"
u = input("Enter username: ")
p = input("Enter your password: ")
if u == username and p == password:
    print("Welcome admin! ")
elif u == username and p != password:
    print("Wrong password!")
elif u != username and p == password:
    print("Wrong username!") 
else:
    print("Both username and password are wrong!")