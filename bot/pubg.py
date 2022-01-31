# pubg.py
from sqlite3 import SQLITE_UPDATE
import requests
import json

# This func takes the account id, and gets the lifetime/seasonal information from the account. Then it returns the KDR (it can be modified to output more information like top 10 or wins)
def get_lifetime(username, playercount, season=None):

    # This extracts the account.id from the website and returns it
    url = f"https://api.pubg.com/shards/steam/players?filter[playerNames]={username}" 

    header = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI3YzIzYzgyMC02NDExLTAxM2EtNGVjOC00MWFhNWM4ZDgwNTciLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjQzNTU3NDkwLCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6Im1heC10cmFja2VyIn0.8UEgWWqe-AplEY0uVw7ZxxIEs0JtN9pLEueqAW6ra3s",
    "Accept": "application/vnd.api+json"
    }

    r = requests.get(url, headers=header).text
    result = json.loads(r)
    accountid = result['data'][0]['id'] #account id retrieved and stored on this variable

    if season == None:

        url = f"https://api.pubg.com/shards/steam/players/{accountid}/seasons/lifetime?filter[gamepad]=false" #This will get the lifetime information of the account

        header = {
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI3YzIzYzgyMC02NDExLTAxM2EtNGVjOC00MWFhNWM4ZDgwNTciLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjQzNTU3NDkwLCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6Im1heC10cmFja2VyIn0.8UEgWWqe-AplEY0uVw7ZxxIEs0JtN9pLEueqAW6ra3s",
            "Accept": "application/vnd.api+json"
        }
        r = requests.get(url, headers=header).text
        result = json.loads(r)

        kills = 0
        deaths= 0

        for key, value in result['data']['attributes']['gameModeStats'][playercount].items(): #extract the information for squads, solos, duos, squads-fpp, solos-tpp, duos-tpp // NOT RANKED AT THE MOMENT 
            if key == 'kills':
                kills = value
            elif key == 'losses':
                deaths = value

        kdr = round(kills/deaths, 2)
        games_w = result['data']['attributes']['gameModeStats'][playercount]['wins']
        top_10s = result['data']['attributes']['gameModeStats'][playercount]['top10s']

        return f'''{username}\'s OVERALL INFORMATION:
        KDR: {kdr}. 
        Reached TOP 10: {top_10s} times. 
        Total WINS: {games_w}'
        Great job!
        '''

    else:
        season_url = f'division.bro.official.pc-2018-{season}'

        url = f'https://api.pubg.com/shards/steam/players/{accountid}/seasons/{season_url}?filter[gamepad]=false' # example of how seasons go for pc division.bro.official.pc-2018-15 and for console division.bro.official.console-15
        
        header = {
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI3YzIzYzgyMC02NDExLTAxM2EtNGVjOC00MWFhNWM4ZDgwNTciLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjQzNTU3NDkwLCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6Im1heC10cmFja2VyIn0.8UEgWWqe-AplEY0uVw7ZxxIEs0JtN9pLEueqAW6ra3s",
            "Accept": "application/vnd.api+json"
        }
        r = requests.get(url, headers=header).text
        result = json.loads(r)

        kills = 0
        deaths= 0

        for key, value in result['data']['attributes']['gameModeStats'][playercount].items(): #extract the information for squads, solos, duos, squads-fpp, solos-tpp, duos-tpp // NOT RANKED AT THE MOMENT 
            if key == 'kills':
                kills = value
            elif key == 'losses':
                deaths = value
        kdr = round(kills/deaths, 2)

        games_w = result['data']['attributes']['gameModeStats'][playercount]['wins']
        top_10s = result['data']['attributes']['gameModeStats'][playercount]['top10s']

        return f'''{username} INFORMATION FOR SEASON {season}:
        KDR: {kdr}.
        Reached TOP 10: {top_10s} times. 
        Total WINS: {games_w}'
        Keep it up!
        '''


# my_info = get_lifetime('MaxOfCCNY', 'squad', 15)

# print(my_info)
# user_message = '!stats MaxOfCCNY squad'
# if '!stats' in user_message:
#     new_message=user_message.split()
#     print(new_message)
# else:
#     print('is not here :(')

