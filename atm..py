#Initializing the system
import random

database = {}

def init():

    isValidOptionSelected = False   #while loop created to avoid system shut down if wrong option is selected
    print ("Welcome To Thrift Bank")

    while isValidOptionSelected == False: #what this does is to bring them back to Account_Details whenever wrong value is selected

        Account_Details = int(input("Do you have a registered account with us?: 1 (Yes) 2 (No) \n"))

        if(Account_Details == 1):
            isValidOptionSelected = True
            login()
    
        elif(Account_Details == 2):
            isValidOptionSelected = True
            register()

        else:
            print("Error! Invalid Option Selected")





def login():
    print("Login your account details")

def register():
    print("**** Register as new customer ****")
    Email = input("Please enter a valid email address \n")
    First_Name = input("Please enter your first name \n")
    Last_Name = input("Please enter your last name \n")
    Password = input("Create new password \n")
    
    accountNumber = AccountNumberGeneration()
    
    database[accountNumber] = [ First_Name, Last_Name, Email, Password ]

    print ("Your account has been succesfully created")
    print("******************************")
    print("Your account number is: %d" % accountNumber)
    print("This is your access to your spondulicks, keep it safe")

    login()

def bankOperation(user):

    print("Welcome %s " % ( user[0], user[1] ) )
    
    option = input("What Operaations would you ike to carry out? (1) Deposit (2) Withdrawal (3) Logout (4) Exit \n")

    if (option == 1):
        DepositOperation()
    elif(option == 2):
        WithdrawalOperation()	
    elif(option == 3):
        login()
    elif(option == 4):
        exit()
    else:
        print("Invalid Option Selected")

def WithdrawalOperation():
    print("Withdrawal Operation")

def DepositOperation():
    print("Deposit Operation")

def AccountNumberGeneration():

    return random.randrange(1111111111,9999999999)


### SYSTEM INITIALIZING ###



init()

#print(AccountNumberGeneration())

