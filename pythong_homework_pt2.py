import os

import csv

votes = []

candidate = []

file = "/Users/jassjones/cwru-cle-virt-data-pt-07-2021-u-c/Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv"

print ("Election Results")

print ("-------------------------------")

with open(file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

    next(csvreader)

    for column in csvreader:
        votes.append(column[0])
        candidate.append(column[2])

    total = (len(votes))

    print (f"Total Votes: {total}")
    print ("--------------------------------")

    
    for column in csvreader:
        candidate.append(column[2])
    
    khan = int(candidate.count("Khan"))
    correy = int(candidate.count("Correy"))
    li = int(candidate.count("Li"))
    tooley = int(candidate.count("O'Tooley"))

    khan_percent = round((khan/total), 2)* 100
    correy_percent = round((correy/total), 2)* 100
    li_percent = round((li/total), 2)* 100
    tooley_percent = round((tooley/total), 2)* 100

    print (f"Khan: {khan_percent}% ({khan})")
    print (f"Correy: {correy_percent}% ({correy})")
    print (f"Li: {li_percent}% ({li})")
    print (f"O'Tooley: {tooley_percent}% ({tooley})")
    print ("--------------------------------")

    if khan > correy and li and tooley:
        print ("Winner: Khan")

    elif correy > khan and li and tooley:
        print ("Winner: Correy")

    elif li > khan and correy and li:
        print ("Winner: Li")

    elif tooley > khan and correy and li:
        print ("Winner: O'Tooley")

    print ("---------------------------------")







    