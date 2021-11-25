from passwordGenerator import random_pass as rp

# ***************************  MAIN APP  ***************************************
print("Hello this is a simple random password generator. You may use this or not.")
print('''
COMMANDS:
start - generate a new random password
help - displays the help section
quit - exits the app
''')

command = ""
while command.lower() != "quit":
    command = input("> ")
    if command.lower() == "start":
        try:
            size = int(input("Enter characters size of random password: "))
            password = rp.generate_random_pass(size)
            print(f"Random password: {password}")
        except ValueError:
            print(f"Please enter a valid number (int)")

    elif command.lower() == "help":
        print('''
        COMMANDS:
        start - generate a new random password
        help - displays the help section
        quit - exits the app
        ''')

    elif command.lower() == "quit":
        print("Thank you for using the app!")
        break

    else:
        print("Sorry, I do not understand that")
