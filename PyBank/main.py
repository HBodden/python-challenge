#import Modules to standardize system and read in csv file 
import os
import csv 
#set variable for csv path
t = False
f = False
rowcount = 0
totalprofloss = 0
totalchange = 0
bankdata = []
bankdata1 = []
tally = []
tally2 = []
newtally = []
combinedlist = []
tallytotal = []
bincrease = []
bdecrease = []

bank_csv = os.path.join("Resources","budget_data.csv")

with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    #print(csv_header)
    for row in csvfile:
        rowcount += 1
    #print(rowcount)    
with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)     
    for row in csvreader:
        totalprofloss = totalprofloss + int(row[1])
    #print(totalprofloss)
with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)     
    for row in csvreader:    
        tally.append(row[1])
        tally2.append(row[1])  
tally2.pop(0)
#Max/Min function found on stackoverflow.com
t_max = max(map(int,tally))
t_min = min(map(int,tally))

for x, y in zip(tally, tally2):
    newtally.append(int(y) - int(x))
    combinedlist.append(newtally)

tallytotal = combinedlist[0]

for each in tallytotal:
    totalchange += each    
#print(totalchange)

with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        bankdata.append(row)

while t == False:
    for row in bankdata:
        if t_max == int(row[1]):
            bincrease.append(row)
            t = True

#print(bincrease)

while f == False:
    for row in bankdata:
        if t_min == int(row[1]):
            bdecrease.append(row)
            f = True 

#print(bdecrease)

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {rowcount}")
print(f"Total: ${totalprofloss}")
print(f"Average Change: ${round(totalchange/(len(tallytotal)),2)}")
print("Greatest Increase in Profits:" +  str(bincrease))
print(f"Greatest Decrease in Profits: {bdecrease[0]}")