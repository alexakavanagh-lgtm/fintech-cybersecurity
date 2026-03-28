from auth import registration, login, passwordReset

users = {}

while True:
    print("\nACCOUNT MENU")
    print("1)   register")
    print("2)   login")
    print("3)   password reset")
    print("4)   quit")

    menuOption = input("Please select an option: 1 2 3 4")

    if menuOption == "1":
        registration(users)
    elif menuOption == "2":
        login(users)
    elif menuOption == "3":
        passwordReset(users)
    elif menuOption == "4":
        print("Exited")
        break
    else:
        print("please select one of the four options")