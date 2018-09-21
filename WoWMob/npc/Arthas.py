#This is Arthas before becoming the Lich King
from random import randrange
class Arthas(object):
    def __init__(self):
        self.streak = 0
    def check(self, message, myStreak, id):
       #Will check streak to see which response it needs
        print("streak = " + str(myStreak))
        if myStreak[id] < 7:
            myStreak[id] = myStreak[id] + 1
            return self.response()
        elif myStreak[id] >= 7 and myStreak[id] < 12:
            myStreak[id] = myStreak[id] + 1
            return self.pissed()
        else:
            myStreak[id] = 1
            return self.response()
    def response(self): #Regular responses
        responses = [
        'May the light have mercy, for I will not.',
        'I will not allow this plague to spread.',
        'Lordearon will be saved.',
        'This city will be cleased!',
        'A small sacrifice for the greater good.'
        ] #End array
        choice = randrange(len(responses))
        return responses[choice]
    def pissed(self): #Responses if pinged too many times without any interuptions
        responses = [
        'Are you looking to be... culled??',
        'Focus on the task at hand!',
        'Do interruptions never seize?!',
        'You have your orders, now follow them!'
        ] #End array
        choice = randrange(len(responses))
        return responses[choice]
    def getStreak(self, myStreak, id): #Returns streak to detirmine if picture should be posted
        return myStreak[id]
    def resetStreak(self, myStreak, id): #Resets streak if interrupted
        myStreak[id] = 0