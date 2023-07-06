import os
import csv 

budget_data = os.path.join('..','budget_data.csv')
with open('budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

# print title of results
    print('Financial Analysis: ')
    header = next(csvreader)
    first_row = next(csvreader)
# variables
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
#The total number of months included in the dataset
        rowcount+= 1
# The net total amount of "Profit/Losses" over the entire period
        total += current
#The changes in "Profit/Losses" over the entire period+ average of those changes
        change = current - previous
        total_change += change
        previous = current
#The greatest increase/decrease in profits (date and amount) over the entire period
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
          
output_file = os.path.join('Results.txt')
with open(output_file) as textfile:
    



    
    





    
