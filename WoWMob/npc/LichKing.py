from random import randrange
class LichKing(object):
    def __init__(self):
        self.streak = 0
    def check(self, message, myStreak, id):
        #Will check streak to see which response it needs
        if self.streak < 7:
            self.streak = self.streak + 1
            return self.response()
        elif self.streak == 7: #Changed because only one pissed off line exists
            self.streak = self.streak + 1
            return self.pissed()
        else:
            self.streak = 1
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
    def getStreak(self): #Returns streak to detirmine if picture should be posted
        return self.streak
    def resetStreak(self): #Resets streak if interrupted
        self.streak = 0