import csv
filedname=['No','Company','Model']
car=[{"No":123,"Company":"Duster","Model":"ASD"},
     {"No":124,"Company":"Maruthy","Model":"PWS"},
     {"No": 125, "Company": "Audi", "Model": "7series"},
     {"No": 126, "Company": "BMW", "Model": "Fortuner"},]
with open("third.csv","w")as csvfile:
    writer=csv.DictWriter(csvfile,fieldnames=filedname)
    writer.writeheader()
    writer.writerows(car)

with open("third.csv",newline="")as csvfile:
    d=csv.reader(csvfile,delimiter=' ')
    for i in d:
        print(','.join(i))