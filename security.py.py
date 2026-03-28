import re

def passwordStrength(password):
    
    if not re.search(r"[0-9]", password):
        print("password must constain a number")    #re 
        return False
    if not re.search(r"[a-z]", password):
        print("password must contain a lowercase letter")
        return False
    if not re.search(r"[A-Z]", password):
        print("password must contain a uppercase letter")
        return False
    if not re.search(r"[$&*?!@#]", password):
        print("password must contain a special character")
        return False
    if len(password)<8:
        print("password is too short")
        return False
    return True