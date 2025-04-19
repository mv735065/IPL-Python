# // Find the number of times each team won the toss and also won the match

from data import dataMatches

result={}

for match in dataMatches:
    toss_winner=match['toss_winner']
    winner=match['winner']
    if toss_winner==winner:
        if winner not in  result:
            result[winner]=1
        else :result[winner]+=1

print(result)