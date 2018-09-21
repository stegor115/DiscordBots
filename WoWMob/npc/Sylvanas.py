from random import randrange
class Sylvanas(object):
    def __init__(self):
        self.streak = 0
    def check(self, message, myStreak, id):
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
        'We are the Forsaken. We will slaughter anyone who stands in our way.',
        'What are we if not slaves to this torment?',
        'What joy is there in this curse?',
        'State your business to your Warchief.',
        'I trust you will not waste my time.',
        'Come forward.',
        'Greetings, champion.',
        'Our true work is just beginning.',
        'There will be a new future for the Horde.',
        'Serve me well, and you will be rewarded.'
        ] #End array
        choice = randrange(len(responses))
        return responses[choice]
    def pissed(self): #Responses if pinged too many times without any interuptions
        responses = [
        'No doubt I am your favorite Windrunner sister... right? Right?',
        'I have taken note of your progress. It seems I may have to send you to Nathanos for remedial training.',
        'Did you think I would not notice the way you leer at my dark rangers? I suggest you keep your eyes--and thoughts--to yourself.',
        'Plans, little old me? What sort of plans could I possibly have?'
        ] #End array
        choice = randrange(len(responses))
        return responses[choice]
    def getStreak(self): #Returns streak to detirmine if picture should be posted
        return self.streak
    def resetStreak(self): #Resets streak if interrupted
        self.streak = 0