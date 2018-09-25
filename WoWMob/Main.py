import discord
import os
import requests
import json

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
            region = "error"
            #Get Regions
            if splitMessage[3] == 'us' or splitMessage[3] == 'oc' or splitMessage == 'united states' or splitMessage == 'oceania':
                region = "us"
            elif splitMessage[3] == 'eu' or splitMessage[3] == 'europe':
                region = "eu"
            elif splitMessage[3] == 'ko' or splitMessage[3] == 'korea':
                region = "ko"
            elif splitMessage[3] == 'tw' or splitMessage[3] == 'taiwan' or splitMessage[3] == 'ch' or splitMessage[3] == 'china':
                region = "tw"
            #Construct link
            if region != 'error':
                realmList = "realmlists/" + region + ".txt"
                with open(realmList, "r") as ins:
                    servers = []
                    for line in ins:
                        servers.append(line.rstrip('\n'))
                
                if "'" in splitMessage[2]: #Removes apostrophies from server name if it was present
                    splitMessage[2] = splitMessage[2].replace("'","")

                if splitMessage[2] in servers: #Server is possible!
                    #Raider.io API ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                    apiParameters = {"region":region, "realm":str(splitMessage[2]), "name":str(splitMessage[1]), "fields":"gear,mythic_plus_scores,raid_progression"} #region, server, name, optional fields
                    charInfo = requests.get("http://raider.io/api/v1/characters/profile", params=apiParameters)
                    charInfo = charInfo.json()

                    if 'statusCode' not in charInfo:
                        #Summary string. It's big and ugly but it's nice when it's in the chat.
                        summary = "__**" + charInfo['name'] +"'s Player Summary " + "(" + charInfo['active_spec_role'] + ")**__\n\
" + charInfo['gender'].capitalize() + " " + charInfo['race'] + " " + charInfo['active_spec_name'] + " " + charInfo['class'] + "\n\
" + "Equipped Item Level: " + str(charInfo['gear']['item_level_equipped']) + "\n\
" + "Total Item Level: " + str(charInfo['gear']['item_level_total']) + "\n\
" + "Uldir Progression: " + charInfo['raid_progression']['uldir']['summary'] + "| Normal: " + str(charInfo['raid_progression']['uldir']['normal_bosses_killed']) + "/8 \
" + "Heroic: " + str(charInfo['raid_progression']['uldir']['heroic_bosses_killed']) + "/8 Mythic: " + str(charInfo['raid_progression']['uldir']['mythic_bosses_killed']) + "/8 \n\
" + "Mythic+ Score: " + str(charInfo['mythic_plus_scores']['all']) + "| DPS: " + str(charInfo['mythic_plus_scores']['dps']) + " Healer: " + str(charInfo['mythic_plus_scores']['healer']) + " Tank: \
" + str(charInfo['mythic_plus_scores']['tank']) + "\n\
" + charInfo['profile_url']

                        await client.send_message(message.channel, summary)
                    else:
                        await client.send_message(message.channel, "Raider.io does not know this character.")

                else:
                    msg = "Could not find " + splitMessage[2] + " in "+ splitMessage[3] + " server list."
                    await client.send_message(message.channel, msg + "\n \
For servers with spaces in their name, replace the spaces with dashes\"-\".")
        else:
            #Incorrect usage message
            await client.send_message(message.channel, "/raider usage: \"/raider <name> <server> <region>\" \n \
For servers with spaces in their name, replace the spaces with dashes\"-\".")
        return #stops rest of script from running
    
    #Fun stuff below---------------------------------------------------------
    #global listr
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