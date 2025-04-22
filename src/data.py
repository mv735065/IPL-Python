

import csv

dataMatches = []

dataDeliveries=[]

# Open the CSV file
with open('public/matches.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)  
    for row in reader:
        dataMatches.append(row)


# Open the CSV file
with open('public/deliveries.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)  
    for row in reader:
        dataDeliveries.append(row)



# with open('data.csv',mode='r',encoding='utf-8') as file:
#     reader=csv.DictReader(file)
#     for row in reader:
#         dataMatches.append(row)


# import json

# with open('public/data.json', mode='r', encoding='utf-8') as file:
#     data = json.load(file)  # Loads the entire JSON into a Python dict (or list, depending on the structure)
