import os

import csv

votes = []

candidate = []

file = "/Users/jassjones/cwru-cle-virt-data-pt-07-2021-u-c/Homework/03-Python/PyPoll/Resources/election_data.csv"
#file = ("PyPoll\Resources\eletcion_data.csv")

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
        winner = "Khan"

    elif correy > khan and li and tooley:
        winnner = "Correy"

    elif li > khan and correy and li:
        winner = "Li"

    elif tooley > khan and correy and li:
        winner = "O'Tooley"

    print (f"Winner: {winner}")

    print ("---------------------------------")


text_file = "/Users/jassjones/cwru-cle-virt-data-pt-07-2021-u-c/Homework/03-Python/PyPoll/Analysis/text_file.txt"
with open (text_file, 'w') as text:

    text.write('Election Results')
    text.write('\n-------------------------------')
    text.write(f'\nTotal Votes: {total}')
    text.write(f'\n--------------------------------')
    text.write(f'\nKhan: {khan_percent}% ({khan})')
    text.write(f'\nCorrey: {correy_percent}% ({correy})')
    text.write(f'\nOTooley: {tooley_percent}% ({tooley})')
    text.write(f'\n--------------------------------')
    text.write(f'\nWinner: {winner}')
    text.write('\n---------------------------------')


    