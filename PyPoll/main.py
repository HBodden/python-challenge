#Import packages for the project 
import os
import csv
#from tokenize import Double

#Set a varribale for the csv file
poll_csv = os.path.join("Resources","election_data.csv")
out_file = os.path.join("Analysis","poll_analysis.txt")
#initiate the variables to capture the required information
votecount = 0
cand1_count =0
cand2_count =0
cand3_count = 0
cand_names = []

#Read in the CSV file 
with open(poll_csv) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")
    
    header = next(csv_reader)
#print(header)
#count the number of rows / votes in the file 
    for row in csv_reader:
        #print(row)
        if int(row[0]) >= 0:        
            votecount += 1
#Count the number of votes    
#print(votecount)
#identify the unique candidates names each candidate has a defined position in the list
with open(poll_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header2 = next(csv_reader)
    for name in csv_reader:
        if name[2] not in cand_names:
            cand_names.append(name[2])
#print(cand_names)
#count the votes for each candidate 
with open(poll_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header2 = next(csv_reader)
    for name in csv_reader:
        if name[2] == cand_names[0]:
            cand1_count += 1 
        elif name[2] == cand_names[1]:
            cand2_count += 1
        elif name[2] == cand_names[2]:
            cand3_count += 1
# print(cand1_count)
# print(cand2_count)
# print(cand3_count)
#sort the votes moving the highest number of votes to the last position in the list
votes = [cand1_count, cand2_count, cand3_count]
sort_votes = sorted(votes)
#print(votes)
#print(sorted(votes))
#print(sort_votes[len(sort_votes)-1])
#Identify the winner of the election by matching the number of votes to the highest vote identifiy in the previous step
t= False 
while t == False:
    if sort_votes[len(sort_votes)-1] == votes[0]:
        winner = cand_names[0]
        t = True
        #print(winner)
    elif sort_votes[len(sort_votes)-1] == votes[1]:
        winner = cand_names[1]
        t = True
       # print(winner)
    elif sort_votes[len(sort_votes)-1] == votes[2]:
        winner = cand_names[2]
        t = True 
#print(winner)
#print(cand_names[len(votes)-1])
cand1_info = str("{:.3%}".format(cand1_count/votecount))
cand2_info = str("{:.3%}".format(cand2_count/votecount))
cand3_info = str("{:.3%}".format(cand3_count/votecount))
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
output = (
    f"Election Results\n"
    f"------------------------\n"
    f"Total Votes: {votecount}\n"
    f"------------------------\n"
    f"{str(cand_names[0])}: {cand1_info} ({str(cand1_count)})\n"
    f"{str(cand_names[1])}: {cand2_info} ({str(cand2_count)}\n"
    f"{str(cand_names[2])}: {cand3_info} ({str(cand3_count)})\n"
    f"------------------------\n"
    f"Winner: {str(winner)}\n"
    f"------------------------\n"
)

print(output)

with open(out_file,"w") as text_file:
    text_file.write(output)
