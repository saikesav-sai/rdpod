import csv

# Open the .trn file for reading
with open(r'data_set\statlog+landsat+satellite\sat.trn', 'r') as trn_file:
    # Read lines from the .trn file
    lines = trn_file.readlines()

# Process the lines to extract data and format it into rows and columns
# For demonstration purposes, let's assume each line contains comma-separated values
data = [line.strip().split(' ') for line in lines]

# Write the data to a CSV file
with open(r'data_set\statlog+landsat+satellite\output.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)