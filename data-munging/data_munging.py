# read data and create a csv file
f1 = open("data/nasa_data.txt", 'r')
f2 = open("data/clean_data.csv", 'a')

# put data into a list and make empty lists for numbers and headers
nasa_data = f1.readlines()
data = []
header = []

# fill in the lists for numbers and headers
for line in nasa_data:
    if line[0].isnumeric():
        data.append(line)
    elif line[0:4] == 'Year' and header == []:
        header.append(line)

# make a function for deleting spaces
def del_space(lines):
    clean_lines = []
    for line in lines:
        data1 = line.strip().split(' ')
        data2 = []
        for i in data1:
            if i != '':
                if '*' in i:
                    data2.append('None')
                else:
                    data2.append(i)
        del data2[-1]
        clean_lines.append(data2)
    return clean_lines

# delete spaces in lists of numbers and headers
clean_data = del_space(data)
clean_header = del_space(header)

# change C to F
for line in clean_data:
    for i in range(len(line)):
        if i == 0 or line[i] == 'None':
            continue
        else:
            line[i] = format(int(line[i])/100*1.8, '.1f')

# use commas to separate headers
csv_header = ','.join(clean_header[0]) + '\n'

# add headers to the csv file
f2.write(csv_header)

# use commas to separate numbers and add numbers to the csv file
for line in clean_data:
    csv_data = ','.join(line) + '\n'
    f2.write(csv_data)

# close the csv file
f2.close()