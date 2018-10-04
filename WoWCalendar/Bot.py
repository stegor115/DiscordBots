import discord
import os
import requests #Will need to retrieve information from WoW Armory
import json #Unsure if needed
import Event

#Due to this bot being available on Github, for security the token is parsed in from an excluded file.
file = open('token.txt','r')
TOKEN = file.read()

client = discord.Client()

#Iterate through ALL of events directory and load into mapServer
#Do the same for authorized user lists

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    inMessage = message.content
    serverID = message.server.id
    # Creation of an event
    # !create <name> <date> <time> <description>
    # eventID is created via count of readLines in server's file
    if inMessage.startswith("!create "):
        if authCheck(serverID, message.author) == False:
            await client.send_message(message.channel, "Unauthorized User.")
            return #Stop
        parameters = inMessage.split()
        print(parameters) #DEBUG
        if len(parameters) == 5:
            return #DEBUG
        else:
            await client.send_message(message.channel, "Invalid entry, type \"!create\" for help.")
            return #Stop rest of script from running
    #Usage explanation
    elif inMessage == "!create":
        if authCheck(serverID, message.author) == False:
            await client.send_message(message.channel, "Unauthorized User.")
            return #Stop
        await client.send_message(message.channel, "__**Usage:**__\n!create <name> <date> <server time> <description>\
        \nName example: Awesome-Guild-Meeting\nTime example: 1800 (Military Time)\nDate example: 1-1-2000")
        return #Stop rest of script from running

    #Authorize members of non-automated ranks
    #Parameters = !authorize <@User>
    if inMessage.startswith("!authorize "):
        if authCheck(serverID, message.author) == False:
            await client.send_message(message.channel, "Unauthorized User.")
            return #Stop
        #End auth check if
        parameters = inMessage.split()
        if len(parameters) == 2:
            serverID = 'data/users/' + str(serverID) + ".txt"
            myWriteFile = open(serverID, "a")
            myReadFile = open(serverID, "r")
            allMentions = [None] * len(message.mentions)
            for i in range(len(message.mentions)):
                allMentions[i] = str(message.mentions[i]) + "\n"
            #end for
            for line in myReadFile:
                if line in allMentions:
                    line = line.replace("\n","")
                    await client.send_message(message.channel, str(line) + " is already an authorized user.")
                    return #Stop everything
            #End for
            for i in range(len(message.mentions)):
                myWriteFile.write(str(message.mentions[i]) + "\n")
                await client.send_message(message.channel, "Added " + str(message.mentions[i]) + " as an authorized user.")
        else:
            await client.send_message(message.channel, "Invalid entry, type \"!authorize\" for help.")
        #Authorize users here
        return #Debug
    elif inMessage == "!authorize":
        #Usage explaination
        if authCheck(serverID, message.author) == False:
            await client.send_message(message.channel, "Unauthorized User.")
            return #Stop
        await client.send_message(message.channel, "__**Usage:**__\n!authorize <@user>")

@client.event
async def on_ready():
    print('------------------------------------')
    print(client.user.name + " Online!")
    print(client.user.id)
    print('------------------------------------')

def authCheck(serverID, author):
    serverID = 'data/users/' + str(serverID) + ".txt"
    myReadFile = open(serverID, "w+")
    if os.stat(serverID).st_size == 0:
        myReadFile.write(str(author) + "\n")
        return True
    for line in myReadFile:
        line = line.replace("\n","")
        if str(author) == line:
            return True
    #End for
    return False

client.run(TOKEN)