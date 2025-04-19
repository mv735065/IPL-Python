# // Find a player who has won the highest number of Player of the Match awards for each season

from data import dataMatches
# print(dataMatches[0])

result={}

for match in dataMatches:
    player_of_match=match['player_of_match']
    season=match['season']

    if season not in result:
        result[season]={}

    if player_of_match not in result[season]:
        result[season][player_of_match]={
            'name':player_of_match,
            'count':1
        }
    else: result[season][player_of_match]['count']+=1


playerInEachSeason={}

for key in result:
    seasonData=result[key]
 
    player = sorted(
            seasonData.items(),
            key=lambda x: x[1]['count'],
            reverse=True  
        )

       
    playerInEachSeason[key] = player[0][1]
print(playerInEachSeason)
