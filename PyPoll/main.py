#Import packages for the project 
import os
import csv

#Set a varribale for the csv file
poll_csv = os.path.join("..","Resources","election_data.csv")
#Read in the CSV file 
with open(poll_csv) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")
    
    header = next(csv_reader)
    print(header)

    for row in csv_reader:
        print(row)

    

