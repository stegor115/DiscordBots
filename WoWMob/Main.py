import discord
from random import randrange

#Custom imports
from npc import HumanGuard
from npc import OrcPeon

#Due to this bot being available on Github, for security the token is parsed in from an excluded file.
file = open('token.txt','r')
TOKEN = file.read()

client = discord.Client()

#Global Variable List
lastMessage = ""
#Global NPC Variables
orcPeon = OrcPeon.OrcPeon()
humanGuard = HumanGuard.HumanGuard()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    inMessage = message.content.lower()
    #global list
    global humanGuard
    global orcPeon

    #List of potential targets (Alphabetical Order)
    #Orc Peon
    if inMessage.startswith("/target orc peon"):
        if orcPeon.getStreak() == 0:
            await client.send_file(message.channel, "img/orcpeon.jpg")
        await client.send_message(message.channel, orcPeon.check(inMessage))
        return
    else:
        orcPeon.resetStreak()
    #Stormwind Guard
    if inMessage.startswith("/target stormwind guard"):
        if humanGuard.getStreak() == 0:
            await client.send_file(message.channel, "img/stormwindguard.png")
        await client.send_message(message.channel, humanGuard.check(inMessage))
        return
    else:
        humanGuard.resetStreak()
        

@client.event
async def on_ready():
    print('------------------------------------')
    print(client.user.name + " Online!")
    print(client.user.id)
    print('------------------------------------')

client.run(TOKEN)