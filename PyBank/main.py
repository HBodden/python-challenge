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
#Max/Min function found at https://stackoverflow.com/questions/63820220/why-python-max-does-not-return-maximum-value
t_max = max(map(int,tally))
t_min = min(map(int,tally))
#Zip logic found at https://stackoverflow.com/questions/57615420/how-to-perform-element-wise-arithmetic-operations-e-g-add-subtract-multiply
for x, y in zip(tally, tally2):
    newtally.append(int(y) - int(x))
    combinedlist.append(newtally)

tallytotal = combinedlist[0]

for each in tallytotal:
    totalchange += each    
#print(totalchange)
mtallytotal = max(tallytotal)
mintallytotal = min(tallytotal)
print(mtallytotal)
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
#format info found @ https://www.pythonpool.com/remove-brackets-from-list-python/#:~:text=Using%20string%20slicing%20method%20to%20remove%20brackets%20from,so%20we%20are%20giving%20as%20%5B1%3A-1%5D.%20Output%20

format = {39:None,91:None,93:None}
s= str(bincrease).translate(format)
#print(len(bincrease))

while f == False:
    for row in bankdata:
        if t_min == int(row[1]):
            bdecrease.append(row)
            f = True 
t = str(bdecrease).translate(format)
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
print(f"Greatest Increase in Profits: $({round(mtallytotal,2)})")
print(f"Greatest Decrease in Profits: $({round(mintallytotal,2)})")