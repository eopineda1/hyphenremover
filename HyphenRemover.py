#Eric Pineda 2022
# This script is used to remove unwanted hypens from a csv file

import csv

with open (r"testfile.csv") as infile, open (r"testfile2.csv" , 'w') as outfile:        #opens the csv file we want to alter, as well as the file we want the new data to go to with the removed hypens. Replace filename here with your file path
    reader = csv.reader(infile)        
    writer = csv.writer(outfile)
    conversion = set('-')               #sets what character to remove, we want the hypens from phone numbers removed but this can be changed to include more special characters if needed
    for row in reader:
        newrow = [''.join('' if c in conversion else c for c in entry) for entry in row]        #writes to the new csv file and essentially deletes the hyphen from the old file, you can replace this with another character if you wish to replace the hypen with something else
        writer.writerow(newrow)