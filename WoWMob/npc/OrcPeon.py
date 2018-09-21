from random import randrange
class OrcPeon(object):
    def __init__(self):
        self.streak = 0
    def check(self, message, myStreak, id):
        #Will check streak to see which response it needs
        #Add If another / exists in phrase
        if self.streak < 7:
            self.streak = self.streak + 1
            return self.response()
        elif self.streak >= 7 and self.streak < 12:
            self.streak = self.streak + 1
            return self.pissed()
        else:
            self.streak = 1
            return self.response()
    def response(self): #Regular responses
        responses = [
        'Yes?',
        'Hmm?',
        'What you want?',
        'Something need doing?',
        'Work, work.'
        ] #End array
        choice = randrange(len(responses))
        return responses[choice]
    def pissed(self): #Responses if pinged too many times without any interuptions
        responses = [
        'Whaaaat?',
        'Me busy, leave me alone!!',
        'Me not that kind of orc!'
        ] #End array
        choice = randrange(len(responses))
        return responses[choice]
    def getStreak(self): #Returns streak to detirmine if picture should be posted
        return self.streak
    def resetStreak(self): #Resets streak if interrupted
        self.streak = 0