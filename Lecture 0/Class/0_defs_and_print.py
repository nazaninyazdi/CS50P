'''name = input("What's your name? ")# or .strip().title()
#Remove whitespace frpm str and capitalize user's name
name = name.strip().title() #method
#L strip or R strip
#you can combain as many methods as you want'''
'''name = name.capitalize()'''
'''#split user's name into first and last name
first, last = name.split(" ")
print(f"Hello {first}")'''



'''def hello():
    name = input("What's your name? ")
    name = name.strip().title()
    print(f"Hello {name}")
hello()'''


'''def hello(to):
    print("Hello,", to)
name = input("What's your name? ")
hello(name) '''


'''def hello(to="World"):

    print("Hello,", to)
hello()
name = input("What's your name? ")
hello(name) '''

def main():
    x = float(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n ** 2

main()