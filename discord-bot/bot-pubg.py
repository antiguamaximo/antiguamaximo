import discord
import pubg #takes from another file in the directory
import bot #where the token for the discord is saved

DISCORD_TOKEN=bot.token()

client = discord.Client()

@client.event
async def on_ready():
    print('We have alogged in as {0.user}'.format(client))

#extracts the username, message and channel where such message was sent.
@client.event
async def on_message(message): 
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
        
    # Gives information extracted from PUBG servers regarding KDR, TOP10, WINS and More!
    if user_message.startswith('!stats'):
        new_message = user_message.split()
        user = new_message[1]
        
        if len(new_message) > 2:
            season = new_message[2]
            response1 = pubg.get_lifetime(user,season)
            await message.channel.send(response1)
        else:
            response = pubg.get_lifetime(user)
            await message.channel.send(response)


client.run(DISCORD_TOKEN)