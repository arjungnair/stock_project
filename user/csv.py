import csv
input_file = csv.DictReader(open("data/1.csv"))
for row in input_file:
    print row