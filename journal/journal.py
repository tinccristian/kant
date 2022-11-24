
from pathlib import Path
import os

journalPath=Path("D:\projects\zeta")

def MakeJournal(user):
    print(f"Making journal of {user}\n")
    os.mkdir(os.path.join(journalPath,user))
    Journal(user)
    

def Journal(user):
    root, users, files = next(os.walk(journalPath), ([],[],[]))
    if user in users:
        print(f"JOURNAL OF {user.upper()}")
    else:
        makeJournal=input(str((f"{user}, you don't have a journal yet, would you like to make one?(yes/no)\n")))
        if(makeJournal==("yes"or"y")):MakeJournal(user)
        else: return
    