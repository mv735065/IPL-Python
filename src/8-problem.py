# // Find the highest number of times one player has been dismissed by another player
from data import dataDeliveries

result = {}

for delivery in dataDeliveries:
    player_dismissed = delivery.get('player_dismissed')
    dismissal_kind = delivery.get('dismissal_kind')

    if not player_dismissed or dismissal_kind == 'run out':
        continue

    bowler = delivery['bowler']

    if player_dismissed not in result:
        result[player_dismissed] = {}

    if bowler in result[player_dismissed]:
        result[player_dismissed][bowler] += 1
    else:
        result[player_dismissed][bowler] = 1



def get_highest_dismissed(players_data):
    max_value = 0
    most_player = None
    dismissed_by = None

    for player, bowlers in players_data.items():
        for bowler, count in bowlers.items():
            if count > max_value:
                max_value = count
                most_player = player
                dismissed_by = bowler

    return {
        most_player: {
            "dismissed_by": dismissed_by,
            "count": max_value
        }
    }



result_player = get_highest_dismissed(result)

print(result_player)