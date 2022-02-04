# pubg.py
from sqlite3 import SQLITE_UPDATE
from urllib.parse import uses_netloc
from attr import field
import requests
import json
import csvformat

#this has to be manually updated each time a season changes
current_season=15 
# This func takes the account id, and gets the lifetime/seasonal information from the account. Then it returns the KDR (it can be modified to output more information like top 10 or wins)
def get_lifetime(username, season=None):

    # This extracts the account.id from the website and returns it
    url = f"https://api.pubg.com/shards/steam/players?filter[playerNames]={username}" 

    header = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI3YzIzYzgyMC02NDExLTAxM2EtNGVjOC00MWFhNWM4ZDgwNTciLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjQzNTU3NDkwLCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6Im1heC10cmFja2VyIn0.8UEgWWqe-AplEY0uVw7ZxxIEs0JtN9pLEueqAW6ra3s",
    "Accept": "application/vnd.api+json"
    }

    #account id retrieved and stored on this variable. Checks if username is wrong
    try:
        r = requests.get(url, headers=header).text
        result = json.loads(r)
        accountid = result['data'][0]['id'] 
    except KeyError:
        return('```Wrong username, please try again(The username it\'s case-sensitive)```')
    #Fields for csv files
    fields = ['Username','KDR', 'Top 10s', 'Wins','Rounds Played','Longest Shot','Most Kills']

    if season == None:
        
        #This will get the lifetime information of the account
        url = f"https://api.pubg.com/shards/steam/players/{accountid}/seasons/lifetime?filter[gamepad]=false" 

        header = {
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI3YzIzYzgyMC02NDExLTAxM2EtNGVjOC00MWFhNWM4ZDgwNTciLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjQzNTU3NDkwLCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6Im1heC10cmFja2VyIn0.8UEgWWqe-AplEY0uVw7ZxxIEs0JtN9pLEueqAW6ra3s",
            "Accept": "application/vnd.api+json"
        }
        r = requests.get(url, headers=header).text
        result = json.loads(r)

        # Variables
        kills, deaths, top_10s, games_w, rounds_played, longest_shot, max_kills = 0, 0, 0, 0, 0, 0, 0
    
        #extract the information for squads, solos, duos, squads-fpp, solos-tpp, duos-tpp // NOT RANKED AT THE MOMENT 
        for key, value in result['data']['attributes']['gameModeStats'].items(): 
            for k, v in value.items():
                if k == 'kills':
                    kills+= v
                elif k == 'losses':
                    deaths+= v
                elif k == 'top10s':
                    top_10s+= v
                elif k == 'wins':
                    games_w+= v
                elif k == 'roundsPlayed':
                    rounds_played+=v
                elif k == 'longestKill' and longest_shot < v:
                    longest_shot = round(v,1)
                elif k == 'roundMostKills' and max_kills < v:
                    max_kills = v
        # Kills / deaths saved into a variable
        kdr = round(kills/deaths, 2)

        #CSV Info & function calls
        #Holds the name of the file
        filename = 'Information_lifetime.csv'
        #Holds the information collected from the API of the player as a list
        player_info = [username, str(kdr), str(top_10s),str(games_w), str(rounds_played), str(longest_shot), str(max_kills)]
        #Saves File path into a variable. Has to be manually inputted 
        file_path = f'C:/Users/maxim/Desktop/Python/{filename}'
        #creates or checks if the file its created
        csvformat.csvCreator(filename, fields, file_path, player_info)
        #adds the information into the file
        csvformat.add_csv(player_info, filename)
        #checks for duplicates
        csvformat.checkDup(filename)
        #updates with the given information
        csvformat.updateCsv(player_info, filename)

        return f'''```{username}\'s Overall Stats:\n
        Kill/Death Ratio (KDR): {kdr}
        Amount of Top 10 Placements: {top_10s} 
        Total Chicken Dinners: {games_w}
        Rounds Played: {rounds_played}
        Longest Shot: {longest_shot}
        Most Kills In A Round: {max_kills}
        ```'''

    else:
        season_url = f'division.bro.official.pc-2018-{season}'

        # example of how seasons go for pc division.bro.official.pc-2018-15 and for console division.bro.official.console-15
        url = f'https://api.pubg.com/shards/steam/players/{accountid}/seasons/{season_url}?filter[gamepad]=false' 
        
        header = {
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI3YzIzYzgyMC02NDExLTAxM2EtNGVjOC00MWFhNWM4ZDgwNTciLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjQzNTU3NDkwLCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6Im1heC10cmFja2VyIn0.8UEgWWqe-AplEY0uVw7ZxxIEs0JtN9pLEueqAW6ra3s",
            "Accept": "application/vnd.api+json"
        }
        r = requests.get(url, headers=header).text
        result = json.loads(r)
       
        # Variables
        kills, deaths, top_10s, games_w, rounds_played, longest_shot, max_kills = 0, 0, 0, 0, 0, 0, 0

        #extract the information for squads, solos, duos, squads-fpp, solos-tpp, duos-tpp // NOT RANKED AT THE MOMENT 
        for key, value in result['data']['attributes']['gameModeStats'].items(): 
            for k, v in value.items():
                if k == 'kills':
                    kills+= v
                elif k == 'losses':
                    deaths+= v
                elif k == 'top10s':
                    top_10s+= v
                elif k == 'wins':
                    games_w+= v
                elif k == 'roundsPlayed':
                    rounds_played+=v
                elif k == 'longestKill' and longest_shot < v:
                    longest_shot = round(v,1)
                elif k == 'roundMostKills' and max_kills < v:
                    max_kills = v
        # checks if there's information on the profile, if not returns a message. Also used as season checker
        try:
            kdr = round(kills/deaths, 2)
        except ZeroDivisionError:
            return(f"""
            ```
            Sorry, there is no information for season {season}. 
            You might have not played during this time or that season hasn't started yet
            (Current season is Season {current_season})```""")


        #CSV File
        #Holds the name of the file
        filename ='Information_seasonal.csv'
        #Holds the information collected from the API of the player as a list
        player_info = [username, str(kdr), str(top_10s),str(games_w), str(rounds_played), str(longest_shot), str(max_kills)]
         #Saves File path into a variable. Has to be manually inputted 
        file_path = f'C:/Users/maxim/Desktop/Python/{filename}'
        #creates or checks if the file its created
        csvformat.csvCreator(filename, fields, file_path, player_info)
        #adds the information into the file
        csvformat.add_csv(player_info, filename)
        #checks for duplicates
        csvformat.checkDup(filename)
        #updates with the given information
        csvformat.updateCsv(player_info, filename)

        return f'''```{username} Stats For Season {season}:\n
        Kill/Death Ratio (KDR): {kdr}
        Amount of Top 10 Placements: {top_10s} 
        Total Chicken Dinners: {games_w}
        Rounds Played: {rounds_played}
        Longest Shot: {longest_shot}
        Most Kills In A Round: {max_kills}
        ```'''




# my_info = get_lifetime('MaxOfCCNY')
# print(my_info)
