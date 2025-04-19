# //Number of matches played per year for all the years in IPL.

from  data import dataMatches 

# Print the result
result={}

for match in dataMatches:
    season=match['season']
    if season in result:
        result[season]+=1 
    else: 
        result[season]=1


print(result)



