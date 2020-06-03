import os
import csv
import collections


fh = open ("electon_results.txt", "w")
polls_csv = "C:/Users/powde/Desktop/python-challenge/PyPoll/Resources/election_data.csv"
with open(polls_csv) as csvfile:
    candidates = {}
    csvreader = csv.reader(csvfile)
    csv_header = next(csvfile)
        
    for row in csvreader:
        if row[2] not in candidates.keys():
            candidates[row[2]] = 0
        candidates[row[2]] = candidates[row[2]] + 1
    total_votes=0

    for votes in candidates.values():
        total_votes = total_votes + votes    
    print("Election Results")
    fh.write("Election Results\n")
    print("---------------------------------------")
    fh.write("---------------------------------------\n")   
    for each, votes in candidates.items():
        rate = votes/total_votes
        print(each + " : " + '{:.1%}'.format(votes/total_votes) + " ( " + str(votes) + ")")
        fh.write(each + " : " + '{:.1%}'.format(votes/total_votes) + " ( " + str(votes) + ")\n")        
    print("------------------------------------------")
    fh.write("------------------------------------------\n")
    print("  ")
    fh.write(" \n ")
    print("   Total Votes : " + str(total_votes))
    fh.write("   Total Votes : " + str(total_votes)+ "\n")
    print("------------------------------------------")
    fh.write("------------------------------------------\n")
    
    most_votes = 0
    for politician in candidates.keys():
        if candidates[politician] > most_votes:
            winner = politician
            most_votes= candidates[politician]

    print('The winner is : ' + winner) 
    fh.write('The winner is : ' + winner + "\n") 
    print(" ")       
    fh.write("\n ")
    print("------------------------------------------")
    fh.write("------------------------------------------\n")
    print("  ")
    fh.write("  \n")
    fh.close()