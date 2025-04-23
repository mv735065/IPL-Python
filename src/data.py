
import pandas as pd
import csv
dataDeliveries=[]

# dfMatches=pd.read_csv('public/matches.csv')
# dfDeleiveries=pd.read_csv('public/deliveries.csv')


with open('public/deliveries.csv','r') as file:
    reader=csv.DictReader(file)
    dataDeliveries=[row for row in reader]



