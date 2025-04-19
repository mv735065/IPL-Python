# // Top 10 economical bowlers in the year 2015

from data import dataDeliveries,dataMatches

# print(dataDeliveries[0])
idsOfTeamsIn2015=set()

for match in dataMatches:
    if match['season']=='2015':
        idsOfTeamsIn2015.add(match['id'])


addBowlersDataEachYearWithBallsRuns={}

for delivery in dataDeliveries:
    batsman_runs=int(delivery['batsman_runs'])
    wide_runs=int(delivery['wide_runs'])
    noball_runs=int(delivery['noball_runs'])
    runs=batsman_runs+wide_runs+noball_runs
    ballIsCounted=noball_runs==0 and wide_runs==0

    bowler=delivery['bowler']
    id=delivery['match_id']
    if id not in idsOfTeamsIn2015:
        continue

    if bowler not in addBowlersDataEachYearWithBallsRuns:
        addBowlersDataEachYearWithBallsRuns[bowler]={
            "runs":0,
            "balls":0
        }
    addBowlersDataEachYearWithBallsRuns[bowler]["runs"]+=runs
    if ballIsCounted:addBowlersDataEachYearWithBallsRuns[bowler]["balls"]+=1

economicalData={}
bowlersAsKeys=list(addBowlersDataEachYearWithBallsRuns.keys())

for bowler in bowlersAsKeys:
    runs=addBowlersDataEachYearWithBallsRuns[bowler]['runs']
    overs=addBowlersDataEachYearWithBallsRuns[bowler]['balls']/6
    if bowler not in economicalData:
        economicalData[bowler]=0
    
    economicalData[bowler] = round(runs / overs, 2)

    
top10=dict(sorted(economicalData.items(),key=lambda x: x[1])[:10])
print(top10)




    



