# pubg.py
from sqlite3 import SQLITE_UPDATE
import requests
import json


# This func takes the account id, and gets the lifetime/seasonal information from the account. 
def get_lifetime(username, season=None):

    # This extracts the account.id from the website and returns it
    url = f"https://api.pubg.com/shards/steam/players?filter[playerNames]={username}" 

    header = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI3YzIzYzgyMC02NDExLTAxM2EtNGVjOC00MWFhNWM4ZDgwNTciLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjQzNTU3NDkwLCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6Im1heC10cmFja2VyIn0.8UEgWWqe-AplEY0uVw7ZxxIEs0JtN9pLEueqAW6ra3s",
    "Accept": "application/vnd.api+json"
    }

    #account id retrieved and stored on this variable. Checks if username is wrong and outputs a wrong username message
    try:
        r = requests.get(url, headers=header).text
        result = json.loads(r)
        accountid = result['data'][0]['id'] 
    except KeyError:
        return('Wrong username, please try again(The username it\'s case-sensitive)')

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
        kills = 0
        deaths= 0
        top_10s = 0
        games_w = 0
        rounds_played = 0
        longest_shot = 0
        max_kills = 0

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

        fields = ['Username','KDR', 'Top 10s', 'Wins','Rounds Played','Longest Shot','Most Kills']

        return f'''```{username}\'s Overall Stats:\n
    Kill/Death Ratio (KDR): {kdr}
    Amount of Top 10 Placements: {top_10s} 
    Total Chicken Dinners: {games_w}
    Rounds Played: {rounds_played}
    Longest Shot: {longest_shot}
    Most Kills in A Round: {max_kills}
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
        kills = 0
        deaths= 0
        top_10s = 0
        games_w = 0
        rounds_played = 0
        longest_shot = 0
        max_kills = 0

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

        kdr = round(kills/deaths, 2)

        return f'''```{username} Stats For Season {season}:\n
    Kill/Death Ratio (KDR): {kdr}
    Amount of Top 10 Placements: {top_10s} 
    Total Chicken Dinners: {games_w}
    Rounds Played: {rounds_played}
    Longest Shot: {longest_shot}
    Most Kills in A Round: {max_kills}
        ```'''