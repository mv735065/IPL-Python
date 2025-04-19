

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


