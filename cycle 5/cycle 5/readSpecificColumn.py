import csv

with open('letter_frequency.csv',mode="r")as file:
    csvFile = csv.reader(file)

    content1, content2, content3 = [],[],[]
    for line in csvFile:
        content1.append(line[0])
        content2.append(line[1])
        content3.append(line[2])

    print("column 1 : ")
    print(content1)
    print("\n")

    print("column 2 : ")
    print(content2)
    print("\n")

    print("column 3 : ")
    print(content3)
    print("\n")
    