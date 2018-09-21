import discord
import os
from random import randrange

#Custom imports
from npc import Anduin
from npc import Arthas
from npc import HumanGuard
from npc import LichKing
from npc import OrcPeon
from npc import Saurfang
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
saurfang = Saurfang.Saurfang()
sylvanas = Sylvanas.Sylvanas()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    inMessage = message.content.lower()

    #Raider.io commands
    if inMessage.startswith("/raider"):
        #Parameter 1 = Character or command, if character Parameter 2 = Realm
        splitMessage = inMessage.split(" ", 3) #["/raider", "<name>", <server>, <region>]
        #if character search command (i.e. Euralyian WrymrestAccord US)
        if(len(splitMessage) == 4):
            hyperlink = "https://raider.io/characters/"
            #United States and Oceania
            if splitMessage[3] == 'us' or splitMessage[3] == 'oc' or splitMessage == 'united states' or splitMessage == 'oceania':
                with open("realmlists/us.txt", "r") as ins:
                    servers = []
                    for line in ins:
                        servers.append(line.rstrip('\n'))
                print(servers) #DEBUG
                if splitMessage[2] in servers:
                    hyperlink = hyperlink + splitMessage[3] + "/" + splitMessage[2] + "/" + splitMessage[1]
                    await client.send_message(message.channel, hyperlink)
                else:
                    hyperlink = "Could not find " + splitMessage[2] + " in US/OC server list."
                    await client.send_message(message.channel, hyperlink)
        else:
            #Incorrect usage message
            print("splitMessage was not 4 long")
        return #stops rest of script from running
    
    #Fun stuff below---------------------------------------------------------
    #global list
    global myMap
    global anduin
    global humanGuard
    global orcPeon
    global saurfang
    global sylvanas

    npcDir = str(os.getcwd()) + "/npc" # So it works on any machine
    potato = os.listdir(npcDir)
    totalIDs = len(potato) - 2 #2 files aren't actually npcs

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

    #Lich King
    myID = myID + 1
    if inMessage.startswith("/target lich king") or inMessage.startswith("/target the lich king"):
        if lichKing.getStreak(myMap[serverID], myID) == 0:
            await client.send_file(message.channel, "img/lichking.jpg")
        await client.send_message(message.channel, lichKing.check(inMessage, myMap[serverID], myID))
    else:
        lichKing.resetStreak(myMap[serverID], myID)

    #Orc Peon
    myID = myID + 1
    if inMessage.startswith("/target orc peon"):
        if orcPeon.getStreak(myMap[serverID], myID) == 0:
            await client.send_file(message.channel, "img/orcpeon.jpg")
        await client.send_message(message.channel, orcPeon.check(inMessage, myMap[serverID], myID))
    else:
        orcPeon.resetStreak(myMap[serverID], myID)
    
    #Varok Saurfang
    myID = myID + 1
    if inMessage.startswith("/target saurfang") or inMessage.startswith("/target varok saurfang"):
        if saurfang.getStreak(myMap[serverID], myID) == 0:
            await client.send_file(message.channel, "img/saurfang.jpg")
        await client.send_message(message.channel, saurfang.check(inMessage, myMap[serverID], myID))
    else:
        saurfang.resetStreak(myMap[serverID], myID)

    #Sylvanas Windrunner
    myID = myID + 1
    if inMessage.startswith("/target sylvanas"):
        if sylvanas.getStreak(myMap[serverID], myID) == 0:
            await client.send_file(message.channel, "img/sylvanas.jpg")
        await client.send_message(message.channel, sylvanas.check(inMessage, myMap[serverID], myID))
    else:
        sylvanas.resetStreak(myMap[serverID], myID)
        

@client.event
async def on_ready():
    print('------------------------------------')
    print(client.user.name + " Online!")
    print(client.user.id)
    print('------------------------------------')

client.run(TOKEN)