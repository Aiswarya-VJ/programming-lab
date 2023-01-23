import csv

with open('letter_frequency.csv',mode="r")as file:
    lst = []
    csvFile = csv.reader(file)
    for line in csvFile:
        lst.append(line)
    print(lst)