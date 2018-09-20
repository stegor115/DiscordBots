import discord
from random import randrange

#Custom imports
from npc import Anduin
from npc import Arthas
from npc import HumanGuard
from npc import LichKing
from npc import OrcPeon
from npc import Sylvanas

#Due to this bot being available on Github, for security the token is parsed in from an excluded file.
file = open('token.txt','r')
TOKEN = file.read()

client = discord.Client()

#Global Variable List
lastMessage = ""
#Global NPC Variables
anduin = Anduin.Anduin()
arthas = Arthas.Arthas()
orcPeon = OrcPeon.OrcPeon()
humanGuard = HumanGuard.HumanGuard()
lichKing = LichKing.LichKing()
sylvanas = Sylvanas.Sylvanas()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    inMessage = message.content.lower()
    #global list
    global anduin
    global humanGuard
    global orcPeon
    global sylvanas

    #List of potential targets (Alphabetical Order)
    #King Anduin Wrynn
    if inMessage.startswith("/target anduin") or inMessage.startswith("/target king anduin"):
        if anduin.getStreak() == 0:
            await client.send_file(message.channel, "img/anduin.jpg")
        await client.send_message(message.channel, anduin.check(inMessage))
    else:
        anduin.resetStreak()
    #Arthas Menethil
    if inMessage.startswith("/target arthas") or inMessage.startswith("/target prince arthas"):
        if arthas.getStreak() == 0:
            await client.send_file(message.channel, "img/arthas.jpg")
        await client.send_message(message.channel, arthas.check(inMessage))
    else:
        arthas.resetStreak()
    #Orc Peon
    if inMessage.startswith("/target orc peon"):
        if orcPeon.getStreak() == 0:
            await client.send_file(message.channel, "img/orcpeon.jpg")
        await client.send_message(message.channel, orcPeon.check(inMessage))
    else:
        orcPeon.resetStreak()
    #Lich King
    if inMessage.startswith("/target lich king") or inMessage.startswith("/target the lich king"):
        if lichKing.getStreak() == 0:
            await client.send_file(message.channel, "img/lichking.jpg")
        await client.send_message(message.channel, lichKing.check(inMessage))
    else:
        lichKing.resetStreak()
    #Stormwind Guard
    if inMessage.startswith("/target stormwind guard"):
        if humanGuard.getStreak() == 0:
            await client.send_file(message.channel, "img/stormwindguard.png")
        await client.send_message(message.channel, humanGuard.check(inMessage))
    else:
        humanGuard.resetStreak()
    #Sylvanas Windrunner
    if inMessage.startswith("/target sylvanas"):
        if sylvanas.getStreak() == 0:
            await client.send_file(message.channel, "img/sylvanas.jpg")
        await client.send_message(message.channel, sylvanas.check(inMessage))
    else:
        sylvanas.resetStreak()
        

@client.event
async def on_ready():
    print('------------------------------------')
    print(client.user.name + " Online!")
    print(client.user.id)
    print('------------------------------------')

client.run(TOKEN)