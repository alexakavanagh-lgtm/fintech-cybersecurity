# FinTech Authentication System
## language choice 
why was python chosen?
Python was chosen for this project because i have prior experiece with it, which has allowed me to implement basic fundamentals that i have previosly learned, for example basic looping and calling functions as seen throughout my code. As well as that python has a huge community allowing me to access rich amounts of tutorials and information, for example i used w3 school for a lot of the fundamental learning(https://www.w3schools.com/python/)
Additionlly i chose python over C becuase python has built in modules for secure proggramming. Modules such as hashlib - for password hashing, where in C these features would have to be implented manually, therefore increases the chance of mistakes. (https://docs.python.org/3/py-modindex.html#cap-h)

## implementing secure programming techniques
 1) password hashing 
    - hashing ensures passwords are never stored as plain characters
    - passwrods arw hashed using SHA-256 from pythons hashlib module
    - this prevents attackers from easily retreiving actuall passwords 
 2) password strength validation
    - passwords must include a series of speciic characters throughout   
      the password 
    -if passwords dont involve all specific characters their denied
     registration
    - weak passwords are regected to prevent brute force attacks
 3) account lockout
    - After three failed login attemps, accounts are locked
    - as a concepts after all three login attemps fail the user will be
     sent an email to then regain access
 4) data protection
    - passwords are never printed or logged
    - sensitive information is only displayed as necessary (username not 
      password)
 5) safe file operations
    - user data is stored in a JSON file
    - program will automatically create the file
6)  email validation
    - users can oly register using a valid company email (uwefintech ,
      @uwefintech.com)
    - prevents unauthorized users from registering


## vulnerbilities 
1) salted hashing 
   - currently, passwords are hashed using SHA-256, but no unique salt is added per user
   - without a salt, tow users with the same password will have the same
     hash, therefore attackers could use rainbow tables to crck common 
     passswords (https://www.geeksforgeeks.org/ethical-hacking/understanding-rainbow-table-attack/)
2) password visibility 
   - when users typw thir password during registration and login, te characters are visible on screen
   - shoulder surfing or screen recording could expose passwords for
     that account
3) Json file 
   - user data is stored in a plain JSON file
   - if the file is accessed by an attacker, users data could be exposed


## future improvements 
1) implement a unique random salt per user
2) use a masked input method to hide typed characters (getpass(https://
   docs.python.org/3/library/getpass.html))
3) encript the JSON file (https://www.geeksforgeeks.org/python/encrypt-and-decrypt-files-using-python/)
   

## example test cases 
   To test my programm, i used a range of invalid, valid and potentially malicios inputs to ensure my system behaves correctley and is secure.
   
   Valid test cases
   1) valid registration
      - entered the company email and a strong password
      - result - registration completed successfully and user was saved in the JSON
        file
   2) valid login
      - entered the correct email and password for an existing acount
      - result - login was successfull
   3) password reset
     - entered an existing username and a strong new password
     - result - password was updated successfully and account was unlocked

   invalid test cases
   1) invalid email 
      - tried to resister without using the company email
      - result - registration was rejected 
   2) weak password
      - tried to register with a weak password 
      - result - registration was rejected due to the password not meeting the 
        strenght requiremtns
   3) password mismatch
      - entered two different passwords during registration
      - result - program displayed an error and asked user to try again
   3) invalid menu input
      - entered a number or characters which was not option in the menu
      - result - program did not crash but asked for a valid choice
   
   security related cases
   1) incorrect password attempts (brute force simulation)
      - entered the wrong password three times during login
      - result - the account was locked after the third failed attempt
   2) attempt to access locked account
      - tried logging in again after account had been locked
      - result - access was denied until the password was reset

## Instructions 

   1) download and install python 
   2) clone the repository 
      - open terminal/pwershell and run:
        git clone https://github.com/alexakavanagh-lgtm/fintech-cybersecurity.git
   3) after cloning run:
      cd fintech-cybersecurity
   4) run the program:
      python menu.py

   5) !important! 
      - when creating email address include uwefintech.com
      
   
      