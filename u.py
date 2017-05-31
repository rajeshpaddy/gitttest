import json

with open('moviedata.txt') as json_file 
data = json.load(json_file)
for p in data['productslink']:
    print(p)
