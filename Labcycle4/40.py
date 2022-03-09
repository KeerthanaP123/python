import csv
with open("second.csv",newline='')as csvfile:
    d=csv.DictReader(csvfile)
    print("name     age")
    print("-------------")
    for i in d:
        print(i['name'],":",i['age'])