import csv

# Open CSV files of the raw data and the munged data
f1 = open('data/temporaryhousing1819.csv', 'r')
f2 = open("data/clean_data.csv", 'w')

# Get a string of headers
header = f1.readline().strip()
# Add a header of "Others"
header += ',# Others'

# Get lists of data
reader = csv.reader(f1)

rows = []
for row in reader:
    a = []
    # Change "s" to "0"
    for i in range(len(row)):
        if row[i] != 's':
            a.append(row[i])
        else:
            a.append('0')
    # Calculate # of others
    others = int(a[3]) - int(a[5]) - int(a[-1])
    a.append(others)
    rows.append(a)

# Write headers into the new CSV file
f2.write(header)
f2.write('\n')

# Write data into the new CSV file
for row in rows:
    writer = csv.writer(f2)
    writer.writerow(row)

