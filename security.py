import re
import hashlib    #hashing library, and to securely hash and store passwords

def passwordStrength(password):   # ensure users password meet my security rules
    
    if not re.search(r"[0-9]", password):
        print("password must constain a number")    #re.search = search string to see if it contains []
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
    if len(password)<8:  #counts password
        print("password is too short")
        return False   #ensures passwords meets reqirements 
    return True #if password passes security measures

def hashPassword(password):
    return hashlib.sha256(password.encode()).hexdigest() # hashes the password before saving it 
                           # SHA-256 hashing algorithm
                           #coverts string into bytes
                           #coverts hash into readable hexadecimal string 
def validateCompanyEmail(email, companyName="uwefintech"):
    # makes sure when entering email its correctly formated
    
    
    email = email.strip()  # strip = removes spaces before an after email
    
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email): # checks email to make sure theres: text before@
                                                                            #          text after@             
                                                                            #          a dot
        return False, "Please use company email"                            #          text after the dot            
    
    
    if companyName.lower() not in email.lower(): #lower used to ensure its all lowercase
        return False, f"Email must include the company name"
    
    return True, ""

