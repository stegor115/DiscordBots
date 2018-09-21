import discord
import os
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
myMap = dict()
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

    #Raider.io commands
    if inMessage.startswith("!raider"):
        #Parameter 1 = Character or command, if character Parameter 2 = Realm
        #if character search command (i.e. Euralyian WrymrestAccord)
            #if raider.io already knows that character
                #Construct link to profile
                #Send as message
            #else
                #if character exists in WoW Armory
                    #if scan finds character
                        #Construct link to profile
                        #Send as message
                    #else
                        #Send "Raider.io could not find character."
                #else
                    # Send "character does not exist"
        #elif help command
            #Produce list of commands, including parameters (!raider <name> <server>)
            #Include explainations of what each command does.
        
        return #Prevents the rest of the script from running
    
    #global list
    global myMap
    global anduin
    global humanGuard
    global orcPeon
    global sylvanas

    #DEBUG
    potato = os.listdir('C:/Users/Stephen/Desktop/Folders/Code/Projects/Python/DiscordBots/WoWMob/npc') # dir is your directory path
    totalIDs = len(potato) - 2 #2 files aren't actually npcs
    #DEBUG

    #Get serverID of message
    serverID = message.server.id
    if serverID not in myMap:
        #Create and fill streaks array for new server
        streaks = [0 for i in range(totalIDs)]
        #Store streak values in map. Key = Server ID, Content = integer array
        myMap[serverID] = streaks

    myID = 0 #Used to keep track of IDs with less hardcoding
    #List of potential targets (Alphabetical Order)
    #King Anduin Wrynn
    if inMessage.startswith("/target anduin") or inMessage.startswith("/target king anduin"):
        if anduin.getStreak(myMap[serverID], myID) == 0:
            await client.send_file(message.channel, "img/anduin.jpg")
        await client.send_message(message.channel, anduin.check(inMessage, myMap[serverID], myID))
    else:
        anduin.resetStreak(myMap[serverID], myID)
    
    #Arthas Menethil
    myID = myID + 1
    if inMessage.startswith("/target arthas") or inMessage.startswith("/target prince arthas"):
        if arthas.getStreak(myMap[serverID], myID) == 0:
            await client.send_file(message.channel, "img/arthas.jpg")
        await client.send_message(message.channel, arthas.check(inMessage, myMap[serverID], myID))
    else:
        arthas.resetStreak(myMap[serverID], myID)
    
    #Human Guard
    myID = myID + 1
    if inMessage.startswith("/target stormwind guard"):
        if humanGuard.getStreak(myMap[serverID], myID) == 0:
            await client.send_file(message.channel, "img/stormwindguard.png")
        await client.send_message(message.channel, humanGuard.check(inMessage, myMap[serverID], myID))
    else:
        humanGuard.resetStreak(myMap[serverID], myID)
    #Orc Peon
    myID = myID + 1
    if inMessage.startswith("/target orc peon"):
        if orcPeon.getStreak() == 0:
            await client.send_file(message.channel, "img/orcpeon.jpg")
        await client.send_message(message.channel, orcPeon.check(inMessage, myMap[serverID], myID))
    else:
        orcPeon.resetStreak()
    
    #Lich King
    myID = myID + 1
    if inMessage.startswith("/target lich king") or inMessage.startswith("/target the lich king"):
        if lichKing.getStreak() == 0:
            await client.send_file(message.channel, "img/lichking.jpg")
        await client.send_message(message.channel, lichKing.check(inMessage, myMap[serverID], myID))
    else:
        lichKing.resetStreak()
    
    #Sylvanas Windrunner
    myID = myID + 1
    if inMessage.startswith("/target sylvanas"):
        if sylvanas.getStreak() == 0:
            await client.send_file(message.channel, "img/sylvanas.jpg")
        await client.send_message(message.channel, sylvanas.check(inMessage, myMap[serverID], myID))
    else:
        sylvanas.resetStreak()
        

@client.event
async def on_ready():
    print('------------------------------------')
    print(client.user.name + " Online!")
    print(client.user.id)
    print('------------------------------------')

client.run(TOKEN)