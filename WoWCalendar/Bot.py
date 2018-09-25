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
    serverID = message.server

    # Creation of an event
    # !create <name> <date> <time> <description>
    # eventID is created via count of readLines in server's file
    if inMessage.startswith("!create "):
        parameters = inMessage.split()
        print(parameters) #DEBUG
        if len(parameters) == 5:
            return #DEBUG
        else:
            await client.send_message(message.channel, "Invalid entry, type \"!create\" for help.")
        return #Stop rest of script from running
    #Usage explanation
    elif inMessage == "!create":
        await client.send_message(message.channel, "__**Usage:**__\n!create <name> <date> <server time> <description>\
        \nName example: Awesome-Guild-Meeting\nDate example: 1-1-2000")
        return #Stop rest of script from running

    #Authorize members of non-automated ranks
    #Parameters = !authorize <@User>
    if inMessage.startswith("!authorize "):
        parameters = inMessage.split()
        if len(parameters) == 2:
            print(*message.mentions)
            serverID = 'data/users' + str(serverID) + ".txt"
            myWriteFile = open(serverID, "w+")
            myReadFile = open(serverID, "r")
            for line in myReadFile:
                if line in message.mentions:
                    await client.send_message(message.channel, str(line) + " is already an authorized user.")
                    message.mentions.remove(line)
            #End for
            for i in range(len(message.mentions)):
                myWriteFile.write(str(message.mentions[i]))
                await client.send_message(message.channel, "Added " + message.mentions[i] + " as an authorized user.")
        else:
            await client.send_message(message.channel, "Invalid entry, type \"!authorize\" for help.")
        #Authorize users here
        return #Debug
    elif inMessage == "!authorize":
        #Usage explaination
        await client.send_message(message.channel, "__**Usage:**__\n!authorize <@user>")

@client.event
async def on_ready():
    print('------------------------------------')
    print(client.user.name + " Online!")
    print(client.user.id)
    print('------------------------------------')

client.run(TOKEN)