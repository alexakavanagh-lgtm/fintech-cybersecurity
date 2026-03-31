from security import passwordStrength, hashPassword
from storage import saveUsers   #imports all functions that are needed
from security import validateCompanyEmail


def login(users):       #handles user login,password checking and account lockout
    print("You have selected login") 
    username = input("Enter your username: ")

    if username not in users:  #checks users existance
        print("Username not found")
        return

    if users[username]["locked"]:  # prevents login if account has been locoked after failed attemps
        print("Account is locked. You will need to check your email to attempt again.")
        return

    attempts = 0 #tracks failed login attemps !brute force attacks!

    while attempts < 3:
        password = input("Enter your password: ")

        if users[username]["password"] == hashPassword(password): #hashes the entered password and compares it to stored hash
            print("Login successful")
            accountMenu(username, users)
            return
        else:
            attempts += 1  #increases failed attempt count 
            print(f"Incorrect password. Attempt {attempts}/3")

    users[username]["locked"] = True
    saveUsers(users)                      #locks account after 3 failed attemps
    print("Too many failed attempts.")
    print("Password reset sent to email.")  # only a concept 
    print("You will need to check your email to attempt again.")


def registration(users):     # handles new user registration
    print("You have selected to register")
    regUsername = input("Please enter your email address: ")
    isValid, msg = validateCompanyEmail(regUsername)   #checks for valid email formar
    if not isValid:                                 #   includes company name  
        print(msg)
        return  

    
    

    
    if regUsername in users:      
        print("This user already exists. Please log in instead.")  
        return

    while True:  # repeats asking for a password until the user enters one that meets security requirements
        print("       !password must contain!")
        print("            - One number")
        print("            - One lowercase letter")
        print("            - One uppercase letter")
        print("            - One special character")
        print("            - At least eight characters long")

        regPassword = input("Please enter a password: ")
        regRePassword = input("Please re-enter your password: ")

        if regPassword != regRePassword:  #ensures passwords match
            print("Passwords do not match, please retry.")
            continue

        if passwordStrength(regPassword):   #security.py
            users[regUsername] = {     # stores new user with hashed password 
             "password": hashPassword(regPassword),
             "locked": False
             }
            saveUsers(users)
            print("Registration successful")
            return
        else:
            print("Password is too weak, please try again.")


def accountMenu(username, users):   #displays the logged in user menu
    while True:   #keeps user inside account menu until they choose logout
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
                newPassword = input("Please insert new password: ")   #lets user set a new password if it meets stregnth rules
                if passwordStrength(newPassword):
                    users[username]["password"] = hashPassword(newPassword)
                    saveUsers(users)
                    print("New password successful")
                    break
                else:
                    print("Password does not meet the requirements")
        elif choice == "3":
            print("Logging out")
            break
        else:
            print("Please choose a valid option")


def passwordReset(users):  #allows user to reset password
    print("You have selected password reset")
    username = input("Enter your username: ")

    if username in users:   #only allows reset if the account exists
        while True:
            newPassword = input("Enter new password: ")
            if passwordStrength(newPassword):
                users[username]["password"] = hashPassword(newPassword)
                users[username]["locked"] = False
                print("Password reset was successful")
                break
            else:
                print("Password does not meet requirements")   #checks, hashes
    else:
        print("Username not found")