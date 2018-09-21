from random import randrange
class LichKing(object):
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
        'All life... must end.',
        'Speak...',
        'Your will... is not your own.',
        'Frostmourne hungers.',
        'Bow to your master.',
        'All. Must. Die.'
        ] #End array
        choice = randrange(len(responses))
        return responses[choice]
    def pissed(self): #Responses if pinged too many times without any interuptions
        #Only has one pissed off line
        return "Remember who owns your soul, Death Knight!"
    def getStreak(self, myStreak, id): #Returns streak to detirmine if picture should be posted
        return myStreak[id]
    def resetStreak(self, myStreak, id): #Resets streak if interrupted
        myStreak[id] = 0