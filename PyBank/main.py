#import Modules to standardize system and read in csv file 
import os
import csv 
#set variable for csv path

rowcount = 0
totalprofloss = 0
totalchange = 0
tally = []
tally2 = []
newtally = []
final = []

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
tally2.append(0)
#print(type(tally))
#print(tally2)
# def element_wise(a, b, f):
#      return [element_wise(i, j, f) 
#      #if type(i) == list and type(j) == list else 
#      f(i, j) for i, j in zip(a, b)]

# totalchange = element_wise(int(tally2), int(tally), lambda x, y: x + y) 

for x, y in zip(tally, tally2):
    newtally.append(int(y) - int(x))
    final.append(newtally)
print(len(final[0]))
    #return pl
for each in final:
    totalchange += each[0]
print(totalchange)

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
print("Average Change: $")
print("Greatest Increase in Profits: ")
print("Greatest Decrease in Profits: ")

    
# list1 = [1,2,3,4]
# list2 = ['a','b','c','d']

# my_zip = zip(list1,list2)
# print(my_zip)
# #loop over the object
# for each in my_zip:
#     print(max(each[0]))