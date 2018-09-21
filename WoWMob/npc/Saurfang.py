from random import randrange
class Saurfang(object):
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
        'I am Saurfang, brother of Broxigar.',
        'Lok\'tar.',
        'Throm\'ka.',
        'I serve the Horde.',
        'Now is not the time for pleasantries.',
        'Speak quickly and speak the truth.',
        'What would you ask of me?'
        ] #End array
        choice = randrange(len(responses))
        return responses[choice]
    def pissed(self): #Responses if pinged too many times without any interuptions
        responses = [
        'I\'m too old for this nonsense.',
        'If you knew how much blood has stained my axe, you would not be so quick to pester me!',
        'Why do you keep prodding me? Is there another war to fight? Ugh, what am I saying... there is always another war to fight.',
        'I have served many warchiefs. Go travel the world a bit. No doubt you will run into a number of them.'
        ] #End array
        choice = randrange(len(responses))
        return responses[choice]
    def getStreak(self, myStreak, id): #Returns streak to detirmine if picture should be posted
        return myStreak[id]
    def resetStreak(self, myStreak, id): #Resets streak if interrupted
        myStreak[id] = 0