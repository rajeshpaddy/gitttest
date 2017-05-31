import json
data ={}
data['productslinks']=[]
Productname = input()
while(Productname!="exit"):
    
    ProductProperties = Productname.split(";")
    for i in ProductProperties[1:]:
        data['productslinks'].append({ProductProperties[0]:i})
    Productname = input()
with open('moviedata.txt','a') as outfile:
    json.dump(data,outfile)

