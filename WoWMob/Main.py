import discord
from random import randrange

#Custom imports
from src import HumanGuard

#Due to this bot being available on Github, for security the token is parsed in from an excluded file.
file = open('token.txt','r')
TOKEN = file.read()

client = discord.Client()

#Global Variable List
lastMessage = ""
humanGuard = HumanGuard

def Human_Guard_Response():
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

def Human_Guard_Pissed():
    responses = [
        'I\'m kinda busy.',
        'Quit it!',
        'What\'s your problem?',
        'Knock it off!',
        'You\'re getting on my nerves.'
    ] #End array
    choice = randrange(len(responses))
    return responses[choice]

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
        await client.send_message(message.channel, humanGuard.response(inMessage))
        #if streak < 7:
        #    await client.send_message(message.channel, Human_Guard_Response())
        #    streak = streak + 1
        #elif streak >= 7 and streak < 12:
        #    await client.send_message(message.channel, Human_Guard_Pissed())
        #    streak = streak + 1
        #else:
        #    await client.send_message(message.channel, Human_Guard_Response())
        #    streak = 1 #Not zero because a message gets sent
    
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