import discord

#Due to this bot being available on Github, for security the token is parsed in from an excluded file.
file = open('token.txt','r')
TOKEN = file.read()

client = discord.Client()

boolQuestionAsked = False #Default value

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    #if message.content.startswith('!hello'):
    #    msg = 'Hello {0.author.mention}'.format(message)
    #    await client.send_message(message.channel, msg)
    #    print('Message sent.')

    if message.content.startswith('!image'): #Debug only, delete later
        image = "img/sorry.png"
        await client.send_file(message.channel, image)
        print("Debug Image sent.")

    inMessage = message.content
    global boolQuestionAsked
    #Checks if the message is a question, and if a question has already been asked.
    if inMessage[len(inMessage)-1]== '?' and boolQuestionAsked == False:
        print ("Question recognized, awaiting response.")
        boolQuestionAsked = True

    #Checks if next message is an acceptable reply, only if a question was asked first.
    #TO-DO, Make this only happen if the next message has a different author.
    elif acceptableWhat(message.content) and boolQuestionAsked == True:
        image = "img/sorry.png"
        await client.send_file(message.channel, image)
        print("Strange thing to ask detected. Image sent.")
        boolQuestionAsked = False

@client.event
async def on_ready():
    print('------------------------------------')
    print(client.user.name + " Online!")
    print(client.user.id)
    print('------------------------------------')

def acceptableWhat(inMessage):
    #Disgusting list of if else spam I hate it
    inMessage = inMessage.lower()
    if inMessage == "what?":
        return True
    elif inMessage == "what?":
        return True
    elif inMessage == "wat?":
        return True
    elif inMessage == "wat":
        return True
    elif inMessage == "?":
        return True
    else:
        return False

client.run(TOKEN)