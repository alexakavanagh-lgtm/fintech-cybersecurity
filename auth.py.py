from security import passwordStrength


def login(users):
    print("You have selected login")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print("Login successful")
        accountMenu(username, users)
    elif username in users:
        print("Incorrect password. Try again.")
    else:
        print("Username not found")


def registration(users):
    print("You have selected to register")
    regUsername = input("Please enter your email address: ")

    # Check if the user already exists
    if regUsername in users:
        print("This user already exists. Please log in instead.")
        return

    while True:
        print("       !password must contain!")
        print("            - One number")
        print("            - One lowercase letter")
        print("            - One uppercase letter")
        print("            - One special character")
        print("            - At least eight characters long")

        regPassword = input("Please enter a password: ")
        regRePassword = input("Please re-enter your password: ")

        if regPassword != regRePassword:
            print("Passwords do not match, please retry.")
            continue

        if passwordStrength(regPassword):
            users[regUsername] = regPassword
            print("Registration successful")
            return
        else:
            print("Password is too weak, please try again.")


def accountMenu(username, users):
    while True:
        print("\nUSER MENU")
        print(f"Welcome, {username}")
        print("1)   view account")
        print("2)   reset password")
        print("3)   log out")

        choice = input("Please choose an option: ")

        if choice == "1":
            print(f"Logged in as: {username}")
            print("Password is hidden")
        elif choice == "2":
            while True:
                newPassword = input("Please insert new password: ")
                if passwordStrength(newPassword):
                    users[username] = newPassword
                    print("New password successful")
                    break
                else:
                    print("Password does not meet the requirements")
        elif choice == "3":
            print("Logging out")
            break
        else:
            print("Please choose a valid option")


def passwordReset(users):
    print("You have selected password reset")
    username = input("Enter your username: ")

    if username in users:
        while True:
            newPassword = input("Enter new password: ")
            if passwordStrength(newPassword):
                users[username] = newPassword
                print("Password reset was successful")
                break
            else:
                print("Password does not meet requirements")
    else:
        print("Username not found")