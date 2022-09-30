#Import packages for the project 
import os
import csv

#Set a varribale for the csv file
poll_csv = os.path.join("Resources","election_data.csv")

votecount = 0
cand_names = []
#Read in the CSV file 
with open(poll_csv) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")
    
    header = next(csv_reader)
    print(header)

    for row in csv_reader:
        #print(row)
        if int(row[0]) >= 0:        
            votecount += 1
#Count the number of votes    
#print(votecount)

with open(poll_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header2 = next(csv_reader)
    for name in csv_reader:
        if name[2] not in cand_names:
            cand_names.append(name[2])
        
print(cand_names)

    
# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------
#Challenge output
print("Election Results")
print("-------------------------")
print(f"Total Votes: {votecount} ")
print("-------------------------")
print("The Candidates are: ")
print(f"{cand_names[0]}")
print(f"{cand_names[1]}")
print(f"{cand_names[2]}")
print("-------------------------")
print("Winner: ")
print("-------------------------")
