"""
scripts that checks for new files being received. 

> Creating temporary folders.
> Deleteing them after userinput on website? 

"""


"""
Imports
"""
import os

def checkNewRequest():
    # idk yet 
    
    pass


def cretaeTempFolder(req_number):
    x = os.path.exists(f"data/req/{req_number}/")

    if x == True:
        pass
    if x != True:
        os.mkdir(f"data/req/{req_number}/")
    


def deleteTempFolder(req_number):
    x = os.path.exists(f"data/req/{req_number}/")

    if x == True:
        os.rmdir(f"data/req/{req_number}/")
    if x != True:
        pass



