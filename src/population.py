# packages
import sys
import csv
import numpy as np
import pandas as pd

# load Data File
file_to_open = "input\\censustract-00-10.csv"

# open csv file
with open(file_to_open, encoding='utf-8-sig', mode='r') as csvfile:
    # get number of columns

    for line in csvfile.readlines():
        array = line.split(',')
        first_item = array[0]

    csvfile.seek(0)

    reader = csv.reader(csvfile, delimiter=',')

    # total population in the CBSA in 2000 & 2010
    sum_2000 = 0
    sum_2010 = 0
    rowcount = 0
    my_data = []

    for row in reader:
        for col in reader:
            sum_2000 += int(col[12].replace(",", ""))
            sum_2010 += int(col[14].replace(",", ""))
            rowcount += 1
            if(col[7] != ''):
                my_data: [int, str] = [col[7], col[8]]
                # print(my_data)

    # average population percent change for census tracts in this Core Based Statistical Area
    mean = sum_2010/rowcount


print("Sum Population in 2000: ", sum_2000)
print("Sum Population in 2000: ", sum_2010)
print("Mean Population % change: ", mean)

# Read csv
data = pd.read_csv("input\\censustract-00-10.csv")
# print(data[0:10])

# Create table
df = pd.DataFrame(data)
all_columns = df.mean(axis=0)
# all_columns

# Core Based Statistical Area Code
CBSA09 = data['CBSA09']
# print(CBSA09[0:10])

# Core Based Statistical Area Code Title
CBSA_T = data['CBSA_T']
# print(CBSA_T[0:10])

# Total number of census tracts
Tracts = data['TRACT10'].value_counts()
# print(Tracts[0:10])

# Total population in 2000
POP2000 = data['POP00']
# print(POP2000[0:10])

# Total population in 2010
POP2010 = data['POP10']
# print(POP2010[0:10])

# Saving the data
new_data = [CBSA09, CBSA_T, Tracts, POP2000, POP2010]
report = pd.concat(new_data, axis=1)
# print(report[0:10])

# Exporting my data to a file
report.to_csv('output\\report.csv')
print("Created output file successfully")
