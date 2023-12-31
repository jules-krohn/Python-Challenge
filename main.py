import os
import csv 

budget_data = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')
with open('budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

# print title of results
    print('Financial Analysis: ')
    header = next(csvreader)
    first_row = next(csvreader)
# The total number of months included in the dataset
    rowcount = 1
    total = int(first_row[1])
    previous = int(first_row[1])
    total_change = 0
    greatest_increase = 0
    greatest_decrease = 0
    greatest_increase_month = ""
    greatest_decrease_month = ""

    for row in csvreader: 
        current = int(row[1])
        rowcount+= 1
        total += current
        change = current - previous
        total_change += change
        previous = current
        if change > greatest_increase: 
            greatest_increase = change
            greatest_increase_month = row[0]
        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_month = row[0] 
        #print(row)
    print('Total number of months: ', rowcount)
    print('Total: ', total)
    print('Average change: ', total_change / (rowcount -1))
    print('Greatest increase: ', greatest_increase_month, greatest_increase)
    print('Greatest Decrease: ', greatest_decrease_month, greatest_decrease)
          
output_file = os.path.join(Results.txt)



    
    





    
