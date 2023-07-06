import os
import csv
import collections


election_data = os.path.join("..", "PyPoll", "election_data.csv")
with open('election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

# print title of results
    print('Election Results: ')
    header = next(csvreader)
#Stored Variables
    Votes = 1
    Candidate_list = []
    Count_1 = collections.Counter()
  # The total number of votes cast  
    for row in csvreader: 
        Votes+= 1
        Candidate =(row[2])
    #A complete list of candidates who received votes
        if Candidate not in Candidate_list:
            Candidate_list.append(Candidate)
        
        
        Count_1[Candidate] += 1

        
    print('Total number of votes: ', Votes)
    print(Count_1)



#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote