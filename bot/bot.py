import discord
import random
import pubg

DISCORD_TOKEN='OTM2Mjg3Mjc2ODU2NjY0MDc0.YfK_eg.HhcV0Nt2et6pqb6KVhrIOwicJ_I'

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

    if message.channel.name == 'bot-testing-channel': # Gives information extracted from PUBG servers regarding KDR, TOP10, and WINS!
        if user_message.startswith('!stats'):
            new_message = user_message.split()
            user = new_message[1]
            mode = new_message[2]
        
            if len(new_message) > 3:
                season = new_message[3]
                response1 = pubg.get_lifetime(user, mode, season)
                await message.channel.send(response1)
            else:
                response = pubg.get_lifetime(user, mode)
                await message.channel.send(response)
            

    if message.channel.name == 'bot-testing-channel': # Basic BOT testing information
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