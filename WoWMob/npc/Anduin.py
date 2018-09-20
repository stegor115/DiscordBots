from random import randrange
class Anduin(object):
    def __init__(self):
        self.streak = 0
    def check(self, message):
        #Will check streak to see which response it needs
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
        'For the Alliance above all.',
        'A just cause is always worth fighting for.',
        'Greetings friend.',
        'A king is only as noble as the cause that he serves.',
        'Stormwind will endure.',
        'Sometimes we must fight for what we believe in.',
        'Stormwind honors your service to the Alliance.'
        ] #End array
        choice = randrange(len(responses))
        return responses[choice]
    def pissed(self): #Responses if pinged too many times without any interuptions
        responses = [
        'Now is not a time for that.',
        'You try my patience.',
        'You know I\'m king now, right?',
        'The light shall burn you!'
        ] #End array
        choice = randrange(len(responses))
        return responses[choice]
    def getStreak(self): #Returns streak to detirmine if picture should be posted
        return self.streak
    def resetStreak(self): #Resets streak if interrupted
        self.streak = 0