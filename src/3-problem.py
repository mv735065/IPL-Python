# // Extra runs conceded per team in the year 2016

from data import dataDeliveries,dataMatches


idsOfTeamsIn2016=set()

for match in dataMatches:
    if match['season']=='2016':
        idsOfTeamsIn2016.add(match['id'])

# print(idsOfTeamsIn2016)


extraRunPerTeam={}

for delivery in dataDeliveries:
    runs=  int (delivery['extra_runs'])
    id=delivery['match_id']
    team=delivery['bowling_team']
    if id not in idsOfTeamsIn2016:
        continue
    
    if team not in extraRunPerTeam:
        extraRunPerTeam[team]=0
    
    extraRunPerTeam[team]+=runs



print(extraRunPerTeam)


