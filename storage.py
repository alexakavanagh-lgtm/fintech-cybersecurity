import json   #save user data into a file
import os  #ensure file exists
FILE_PATH = 'users_json.json'  #file used to store users


def loadUsers():   # loads users account data from the JSON file
    if not os.path.exists(FILE_PATH):  #checks file exists
        return {}
    with open(FILE_PATH, "r") as f:  # opens JSON file in readmode !safe!
        try:   
            users = json.load(f)
            return users
        except json.JSONDecodeError:  # if file is empty it returns an emtpty disctoary instead of crashing
            return {}

def saveUsers(users):  # saves the current users dictionary into the JSON file
    with open(FILE_PATH, "w") as f:
        json.dump(users, f, indent=4)  #indent formats it