import discord
from random import randrange

#Custom imports
from npc import HumanGuard

#Due to this bot being available on Github, for security the token is parsed in from an excluded file.
file = open('token.txt','r')
TOKEN = file.read()

client = discord.Client()

#Global Variable List
lastMessage = ""
#Global NPC Variables
humanGuard = HumanGuard.HumanGuard()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    inMessage = message.content.lower()
    #global list
    global humanGuard

    #Checks if the message is a question, and if a question has already been asked.
    if inMessage.startswith("/target stormwind guard"):
        if humanGuard.getStreak == 0:
            await client.send_file(message.channel, "img/stormwindguard.png")
        await client.send_message(message.channel, humanGuard.check(inMessage))
    
   # elif inMessage == "/target stormwind guard /wave":
    #    print ("Wave request recognized.")
    #    msg = "/wave"
    #    await client.send_message(message.channel, msg)

    #elif inMessage == "/target stormwind guard /salute":
     #   print ("Salute request recognize.")
      #  msg = "/salute"
      #  await client.send_message(message.channel, msg)
    
   # else:
      #  print("Reseting streak.")
      #  streak = 0
        

@client.event
async def on_ready():
    print('------------------------------------')
    print(client.user.name + " Online!")
    print(client.user.id)
    print('------------------------------------')

client.run(TOKEN)