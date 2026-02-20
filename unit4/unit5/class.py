import random

class Insta_profile:
    def __init__(self, username,email,location,skills):
        self.username = username
        self.email =email
        self.location = location
        self.skills = skills
        self.usernameCharacterCount =14
Profile_1= Insta_profile('EmilTheBoss','etb@gmail.com',0,0)
Profile_2= Insta_profile('Thelocater','thelocater@gmail.com',0,0)

def checkusernamecount(self, usernameCharacterCount):
    for x in usernameCharacterCount:
        if len(usernameCharacterCount) > 14:
            print('Username is too long')
        else:
            print('Username is valid')  
    

print(Profile_1.username)
print(Profile_2.email)
print(Profile_2)


def sayHello(self):
    print('hello')

sayHello(self=Profile_1)

checkusernamecount(self=Profile_1, usernameCharacterCount=Profile_1.usernameCharacterCount)

