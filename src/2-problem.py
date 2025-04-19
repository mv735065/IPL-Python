# // Number of matches won per team per year in IPL.
from  data import dataMatches 


result={}

for match in dataMatches:
    season=match['season']
    winner=match['winner']
    if season not in result:
        result[season]={}
    if winner not in  result[season]:
        result[season][winner]=1
    else: result[season][winner]+=1

print(result)



