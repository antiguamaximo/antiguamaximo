import discord
import random
import pubg

DISCORD_TOKEN='<place your key here>'

client = discord.Client()

@client.event
async def on_ready():
    print('We have alogged in as {0.user}'.format(client))

@client.event
async def on_message(message): #extracts the username, message and channel where such message was sent.
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    # Provides information given the username regarding multiple important details regarding the account.
    if message.channel.name == 'bot-testing-channel' or message.channel.name == 'comandos' or message.channel.name =='chat-general': 
        if user_message.startswith('!stats'):
            new_message = user_message.split()
            user = new_message[1]
            
            #test if the given message is properly set following the criteria on the bot description
            if len(new_message) > 2:
                season = new_message[2]
                response1 = pubg.get_lifetime(user,season)
                await message.channel.send(response1)
            else:
                response = pubg.get_lifetime(user)
                await message.channel.send(response)
            
    # Basic BOT testing information
    if message.channel.name == 'bot-testing-channel': 
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower()=='!random':
            response = f'This is your random number: {random.randrange(10000)}'
            await message.channel.send(response)

    if user_message.lower() == '!anywhere':
        await message.channel.send('This can be used anywhere!')


    
client.run(DISCORD_TOKEN)
