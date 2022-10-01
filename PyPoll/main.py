#Import packages for the project 
import os
import csv
#from tokenize import Double

#Set a varribale for the csv file
poll_csv = os.path.join("Resources","election_data.csv")
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
#print(cand_names)
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

votes = [cand1_count, cand2_count, cand3_count]
sort_votes = sorted(votes)
#print(votes)
#print(sorted(votes))
#print(sort_votes[len(sort_votes)-1])
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
print(str(cand_names[0])+ ": " + str("{:.3%}".format(cand1_count/votecount))+ " " + "(" +str(cand1_count) + ")")
print(str(cand_names[1])+ ": " + str("{:.3%}".format(cand2_count/votecount))+ " " + "("+str(cand2_count)+")")
print(str(cand_names[2])+ ": " + str("{:.3%}".format(cand3_count/votecount))+ " " + "("+str(cand3_count)+")")
print("-------------------------")
print("Winner: " + str(winner) )
print("-------------------------")
