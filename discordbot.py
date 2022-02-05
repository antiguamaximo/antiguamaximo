from tracemalloc import start
import discord
import pubgbot
import dotenv
import os
import pathlib
import csvformat

#gets token from a .env file
dotenv_path = pathlib.Path('C:/Users/maxim/Desktop/Python/bot.env')
dotenv.load_dotenv(dotenv_path=dotenv_path)
DISCORD_TOKEN=os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#all the commands are here
@client.event
async def on_message(message): 
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    # print(f'{username}: {user_message} ({channel})')
    ##Please provide the path where you will like to have the file created. Use functions on csvformat.py
    paths = ''
    
    if message.author == client.user:
        return
    
    # Gives information extracted from PUBG server
    if user_message.startswith('!stats'):
        new_message = user_message.split()
        #checks if an username is provided with the command
        try:
            user = new_message[1]
        except IndexError:
            await message.channel.send('```Please provide an username```')

        # if message passes previous try, then it proceeds to be compared in an if statement
        if len(new_message) > 2:
            season = new_message[2]
            response1 = pubgbot.get_lifetime(user,season)
            await message.channel.send(response1)
        else:
            response = pubgbot.get_lifetime(user)
            await message.channel.send(response)

    #sets discord user to a username
    elif user_message.startswith('!set'):
        try:
            user = user_message[1]
        except IndexError:
            await message.channel.send('```Please provide an username```')
        username2 = str(message.author)
        csvformat.user_info('Discord_UserInfo.csv', ['Discord', 'Username'], paths, {username2: user})
        await message.channel.send('Your information has been saved!')    
        # deletes an entry from the file saved
    elif user_message.startswith('!setdel'):
        try:
            user = user_message[1]
        except IndexError:
            await message.channel.send('```Please provide an username```')
        username2 = str(message.author)
        csvformat.del_user('Discord_UserInfo.csv', paths, username2)
        await message.channel.send('Your information was deleted!')
            

        #displays how to use the available commands 
    elif user_message.startswith('!help'):
        await message.channel.send("""```
            !stats[space][Pubg-Username][space][Season(optional)]
            Ex. !stats MaxOfCCNY or !stats MaxOfCCNY 15
            !set[space][Pubg-Username]
            Ex. !set MaxOfCCNY
            !setdel[space][DiscordUsername](Include # and 4 numbers)
            Ex. !set QUADMax#9578
            !rank[space][KDR/Most Kills/Longest Shot/Wins/Top 10s/Rounds Played(choose one)][space][Season(optional)]
            Ex. : !rank KDR or !rank KDR 15
            !help - Provides information regarding how to use the available commands for the bot
           ``` """)

client.run(DISCORD_TOKEN)
