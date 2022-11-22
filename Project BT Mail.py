# Email Backend Software
# Email class (reciever, sender, message)
# Account class (userId, password, name, age, question, answer)
# accountDatabase = {userid:Account Object}
# emailDatabase = {reciever:[List of Email Objects]}

class Email:
    def __init__ (self, reciever, sender, message):
        self.reciever = reciever
        self.sender = sender
        self.message = message

class Account:
    def __init__ (self, userId, password, name, age, question, answer):
        self.userId = userId
        self.password = password
        self.name = name
        self.age = age
        self.question = question
        self.answer = answer
    def changePassword (self): # This function changes the initial user's password
        # Verify Password
        current_password = input("Enter the current password : ")
        if current_password == self.password:
            print("Password Verified")
            new_password = input("Enter the new password : ")

            while len(new_password) < 6:
                print("Password is too short")
                new_password = input("Enter another new password : ")
            
            if len(new_password) >=6:
                print("New password Updated Successfully")
                self.password = new_password
        else:
            print("Incorrect Passoword")

    def forgotPassword (self): # This function helps the user to Reset his password only if he answers the question correctly
    
    def compose (self, emailDatabase, accountDatabase): # This function helps the user to compose an email
        return emailDatabase

    def inbox (self, emailDatabse): # This function shows all the emails that were sent to you


# used to display the user's personal homepage
def home (accountDatabase, emailDatabase, userid):

# used to login to an account:
def login (accountDatabase):
    return True / False / userid

# used to create an account:
def create (accountDatabase):
    return accountDatabase

# used to login / create an account
def landingPage (accountDatabase):

accountDatabase = {} # Initially Empty Dictionary
emailDatabase = {} # Initially Empty Dictionary
landingPage (accountDatabase, emailDatabase) # Landing Page will be used to login/create an account