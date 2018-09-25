#This will be used to replace all the files in npc folder
from random import randrange
class NPC(object):
    def __init__(self):
        self.streak = 0 #Redundant but python didn't like a blank init
    def check(self, message, myStreak):
        #Will check streak to see which response it needs
        print("streak = " + str(myStreak))
        validCharacter = False
        id = -1
        npcInfo = open('npc.json','r')
        npcInfo = json.loads(npcInfo)
        print(npcInfo['anduin']['responses'])
        if validCharacter == True:
            if myStreak[id] < 7:
                myStreak[id] = myStreak[id] + 1
                return self.response()
            elif myStreak[id] >= 7 and myStreak[id] < 12:
                myStreak[id] = myStreak[id] + 1
                return self.pissed()
            else:
                myStreak[id] = 1
                return self.response()
    def response(self, name): #Regular responses
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
    def pissed(self, name): #Responses if pinged too many times without any interuptions
        responses = [
        'Now is not a time for that.',
        'You try my patience.',
        'You know I\'m king now, right?',
        'The light shall burn you!'
        ] #End array
        choice = randrange(len(responses))
        return responses[choice]
    def getStreak(self, myStreak, id): #Returns streak to detirmine if picture should be posted
        return myStreak[id]
    def resetStreak(self, myStreak, id): #Resets streak if interrupted
        myStreak[id] = 0