# Insight Data Science Project

## Input

An input file, censustract-00-10.csv is provided to read the data.

After reading and processing the input file, code will create an output file, report.csv, with as many lines as unique Core Based Statistical Areas found in the input file.

For every line of Core Based Statistical Areas that exists in the output file, the following fields are in this order:

Core Based Statstical Area Code (i.e., CBSA09)
Core Based Statistical Area Code Title (i.e., CBSA_T)
Total number of census tracts
Total population in the CBSA in 2000
Total population in the CBSA in 2010
Average population percent change for census tracts in this CBSA. Round to two decimal places using standard rounding conventions (i.e., Any percentage between 0.005% and 0.010%, inclusive, should round to 0.01% and anything less than 0.005% should round to 0.00%)

The lines in the output file is sorted by Core Based Statstical Area Code (ascending)

Given the above censustract-00-10.csv input file, an output file, report.csv is created in the following format

28540,"Ketchikan, AK",4,14074,13477,-4.41
46900,"Vernon, TX",4,14679,13535,-10.25
