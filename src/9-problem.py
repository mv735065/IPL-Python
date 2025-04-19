# //Find the bowler with the best economy in super overs


from data import dataDeliveries

result = {}

for delivery in dataDeliveries:
    if delivery.get("is_super_over") == "0":
        continue

    bowler = delivery["bowler"]
    runs = int(delivery["total_runs"])

    if bowler not in result:
        result[bowler] = {
            "runs": 0,
            "balls": 0
        }

    result[bowler]["runs"] += runs
    result[bowler]["balls"] += 1


def get_best_player_with_economy(bowlers_data):
    best_economy = float('inf')
    best_bowlers = []

    for bowler, stats in bowlers_data.items():
        runs = stats["runs"]
        balls = stats["balls"]
        overs = balls / 6
        if overs == 0:
            continue
        economy = runs / overs

        if economy < best_economy:
            best_economy = economy
            best_bowlers = [{
                "best_player": bowler,
                "economy": round(economy, 2)
            }]
        elif economy == best_economy:
            best_bowlers.append({
                "best_player": bowler,
                "economy": round(economy, 2)
            })

    return best_bowlers

best_bowlers = get_best_player_with_economy(result)


print(best_bowlers)