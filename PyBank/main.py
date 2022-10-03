#import Modules to standardize system and read in csv file 
import os
import csv 
#set variable for csv path
t = False
f = False
rowcount = 0
countrow = 1
countrow2 = 1
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
#Initiate varriable to read csv file
bank_csv = os.path.join("Resources","budget_data.csv")
#Count the number of rows in the file
with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    #print(csv_header)
    for row in csvfile:
        rowcount += 1
    #print(rowcount)    
#calculate the total profit/loss (add up all values in the list)
with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)     
    for row in csvreader:
        totalprofloss = totalprofloss + int(row[1])
    #print(totalprofloss)
#create lists to set up the calculation to find the biggest increase and biggest decrease
with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)     
    for row in csvreader:    
        tally.append(row[1])
        tally2.append(row[1])  
        bankdata.append(row[0])
tally2.pop(0)
#print(bankdata)

#for loop logic from at https://stackoverflow.com/questions/57615420/how-to-perform-element-wise-arithmetic-operations-e-g-add-subtract-multiply
for x, y in zip(tally, tally2):
    newtally.append(int(y) - int(x))
    combinedlist.append(newtally)

tallytotal = combinedlist[0]

for each in tallytotal:
    totalchange += each    
#print(totalchange)
mtallytotal = max(tallytotal)
mintallytotal = min(tallytotal)
#print(len(tallytotal))

#identify the line number where the biggest increase occurs 
for row in tallytotal:
    if int(mtallytotal) != int(row):
        countrow += 1 
    elif int(mtallytotal) == int(row):
        s = countrow
#print(s)        
#using the line number (countrow) pop the date associated with the biggest increase and assign it to the variable
increasedate = bankdata.pop(s)
#print(increasedate)
#Identify the line number of the biggest decrease 
for row in tallytotal:
    if int(mintallytotal) != int(row):
        countrow2 += 1 
    elif int(mintallytotal) == int(row):
        t = countrow2
#print(t)   
#Using the line number associated with the biggest decrease pop the correspnding date
decreasedate = bankdata.pop(t)  
#print(decreasedate)   

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
print(f"Greatest Increase in Profits: {increasedate} $({round(mtallytotal,2)})")
print(f"Greatest Decrease in Profits: {decreasedate} $({round(mintallytotal,2)})")