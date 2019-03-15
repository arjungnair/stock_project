import csv
input_file = csv.DictReader(open("/static/1.csv"))
for row in input_file:
    print row