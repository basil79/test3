import csv

# Read CSV File
def read_csv(file):
    with open(file, mode='r') as csv_file:
        line_count = 0
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        fieldnames = csv_reader.fieldnames
        csv_rows = []

        print(fieldnames)

        for row in csv_reader:
            csv_rows.extend([{fieldnames[i]: row[fieldnames[i]] for i in range(len(fieldnames))}])

        return csv_rows



data_source = read_csv('data.csv')
print('-' * 40)
for n in data_source:
    x, y = float(n['price']), float(n['old_price'])
    print(x)
    if x == 5:
        print("found 5")





