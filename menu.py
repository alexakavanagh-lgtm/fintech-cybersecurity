from auth import registration, login, passwordReset   #cd "C:\Users\pc\OneDrive\Desktop\fintech project"
#integration of hashing                            #
from storage import loadUsers  

users = loadUsers()  #loads all existing users from JSON when programm starts

while True:  #infinite loop
    print("\nACCOUNT MENU")
    print("1)   register")
    print("2)   login")
    print("3)   password reset")
    print("4)   quit")

    menuOption = input("Please select an option: 1 2 3 4: ") 

    if menuOption == "1":
        registration(users)   #runs each proccess depending on what user picks
    elif menuOption == "2":
        login(users)
    elif menuOption == "3":
        passwordReset(users)
    elif menuOption == "4":
        print("Exited")         #exits programm
        break
    else:
        print("please select one of the four options")

