import time
import sys
from tqdm import tqdm
import journal
from journal import Journal
class Console:

    global Greet
    global Talk
    global params
    global user
    params= "\nAvailable functions are: journal,exit"
    
    def __init__(self,user):
        self.user = user
        
    def Greet(user):
        if (user == "ghl"):
            print(f"\nWelcome {user}! \U0001F9E0")
        time.sleep(1.2)
            
    def Talk():
        choice=True
        while(choice):
            
            userinput=str(input(f"\nWhat would you like to do today {user}?\n"))
            if(userinput=="journal"):
                print(f"Opening {user}'s journal!")
                for i in tqdm(range(100)):
                    time.sleep(.0001)
                journal
                Journal(user)
                choice=False
                print("Empty for now..")
                
            elif(userinput=="exit"):
                print("Exiting..")
                for i in tqdm(range(100)):
                    time.sleep(.0025)
                    choice=False
                sys.exit
            else:
                print(params)         
        
        
if __name__ == "__main__":
    
    user= str(input("user: "))
    c=Console(user)
    Greet(user)
    Talk()
    