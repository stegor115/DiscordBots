from random import randrange
class HumanGuard(object):
    def __init__(self):
        self.streak = 0
    def check(self, message):
        #Will check streak to see which response it needs
        #Add If another / exists in phrase
        if not "/wave" in message and not "/salute" in message:
            if self.streak < 7:
                self.streak = self.streak + 1
                return self.response()
            elif self.streak >= 7 and self.streak < 12:
                self.streak = self.streak + 1
                return self.pissed()
            else:
                self.streak = 1
                return self.response()
        else:
            return self.emote(message)
    def response(self): #Regular responses
        responses = [
        'Greetings.',
        'Hey there.',
        'What can I do for you?',
        'Light be with you.',
        'Well met.',
        'Hello!',
        'Light bless you.',
        'King\'s honor, friend',
        'Forget something?'
        ] #End array
        choice = randrange(len(responses))
        return responses[choice]
    def pissed(self): #Responses if pinged too many times without any interuptions
        responses = [
        'I\'m kinda busy.',
        'Quit it!',
        'What\'s your problem?',
        'Knock it off!',
        'You\'re getting on my nerves.'
        ] #End array
        choice = randrange(len(responses))
        return responses[choice]
    def emote(self, message): #Responses if the NPC has emotes it does back to players
        if self.streak == 0: #Stop potential image spam
            self.streak = 1
        if "/wave" in message:
            return '/wave'
        elif "/salute" in message:
            return '/salute'
    def getStreak(self): #Returns streak to detirmine if picture should be posted
        return self.streak
    def resetStreak(self): #Resets streak if interrupted
        self.streak = 0