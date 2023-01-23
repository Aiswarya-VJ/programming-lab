import csv
my_dict = {'1': 'aaa', '2': 'bbb', '3': 'ccc'}
with open('sample.csv', 'w') as f:
    for key in my_dict.keys():
        strng = str(key)+","+str(my_dict[key])+"\n"
        f.write(strng)

with open('sample.csv',mode="r")as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        print(line)