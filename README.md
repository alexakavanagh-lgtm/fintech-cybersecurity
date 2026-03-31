# FinTech Authentication System
## language choice 
why was python chose?
Python was chosen for this project because i have prior experiece with it, which has allowed me to implement basic fundamentals that i have previosly learned, for example basic looping and calling functions as seen throughout my code. As well as that python has a huge community allowing me to access rich amounts of tutorials and information, for example i used w3 school for a lot of the fundamental learning(https://www.w3schools.com/python/)
Additionlly i chose python over C becuase python has built in modules for secure proggramming. Modules such as hashlib - for password hashing, where in C these features would have to be implented manually, therefore increases the chance of mistakes. (https://docs.python.org/3/py-modindex.html#cap-h)

## implenting secure programming techniques
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
   

## example