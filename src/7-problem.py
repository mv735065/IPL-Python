# // Find the strike rate of a batsman for each season

import json
from data import dataMatches, dataDeliveries
from collections import defaultdict

def get_match_id_to_season_map(matches):
    id_to_season = {}
    for match in matches:
        match_id = match['id']
        season = match['season']
        id_to_season[match_id] = season
    return id_to_season

def get_batsman_runs_per_season(id_to_season_map, deliveries):
    result = {}

    for delivery in deliveries:
        match_id = delivery['match_id']
        season = id_to_season_map.get(match_id)

        if not season:
            continue

        batsman = delivery['batsman']
        runs = int(delivery['batsman_runs'])

        if season not in result:
            result[season] = {}

        if batsman not in result[season]:
            result[season][batsman] = {
                "runs": 0,
                "balls": 0
            }

        result[season][batsman]["runs"] += runs
        result[season][batsman]["balls"] += 1

    return result


def add_strike_rate(batsman_data):
    final_result = {}

    for season, players in batsman_data.items():
        season_data = {}

        for batsman, stats in players.items():
            runs = stats["runs"]
            balls = stats["balls"]
            if balls == 0:
                strike_rate = 0
            else:
                strike_rate = round((runs / balls) * 100, 2)

            season_data[batsman] = strike_rate

        final_result[season] = season_data

    return final_result

id_to_season = get_match_id_to_season_map(dataMatches)
batsman_data = get_batsman_runs_per_season(id_to_season, dataDeliveries)
strike_rate_result = add_strike_rate(batsman_data)

print(strike_rate_result)
