import csv

with open('assets/2023/1T2023.csv', mode='rb') as csv_file:
    reader = csv.reader(csv_file)

    next(reader)

    for row in reader:
        print(row)