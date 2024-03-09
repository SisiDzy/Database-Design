import csv

# read data and put them into a list
f = open('data/clean_data.csv', 'r')
csv_reader = csv.DictReader(f)
data = list(csv_reader)

# make empty lists for J_D and average temperatures for decades
JD_list = []
final_avg = []

# calculate average temperatures for decades
for i in data:
    if len(JD_list) == 10:
        avg = sum(JD_list) / 10
        final_avg.append(avg)
        JD_list = []
        JD_list.append(float(i['J-D']))
    else:
        JD_list.append(float(i['J-D']))

# calculate the average temperature for years from 2020 to 2022
avg = sum(JD_list) / len(JD_list)
final_avg.append(avg)

# print final results
a = 0
for i in range(int(data[0]['Year']), int(data[-1]['Year']), 10):
    if i + 9 <= int(data[-1]['Year']):
        print(f"The average temperature for the decade from {i} to {i+9} is {final_avg[a]:.2f}")
        a += 1
    else:
        print(f"The average temperature for the decade from {i} to {data[-1]['Year']} is {final_avg[a]:.2f}")