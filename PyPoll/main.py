import os
import csv
 

election_data = os.path.join("..", "PyPoll", "election_data.csv")
with open('budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

# print title of results
    print('Election Results: ')
    header = next(csvreader)
# The total number of votes cast
    rowcount = 1
    for row in csvreader: 
        rowcount+= 1
        
    print('Total number of votes: ', rowcount)

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote