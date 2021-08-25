import os

import csv

months = 0
profit_losses = []
net_total = 0
dates = []
change = []
max = 0
min = 0
total = 0

file = "/Users/jassjones/cwru-cle-virt-data-pt-07-2021-u-c/Homework/03-Python/PyBank/Resources/budget_data.csv"
file = ("PyBank\Resources\budget_data.csv")

print ("Financial Analysis")

print ("-----------------------------")

with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    
    next(csvreader)

    for row in csvreader:
      months = months + 1

      net_total += int(row[1])

      dates.append(row[0])
      profit_losses.append(int(row[1]))

    print (f"Total Months: {months}")
    print (f"Total: ${net_total}")


for nums in range(1, len(profit_losses)):
     all_changes = profit_losses[nums] - profit_losses[nums - 1]
     change.append(int(all_changes))


for nums in range(0, len(change)):
     total += change[nums]
     average = round((total / (len(change))), 2)

print(f"Average Change: ${average}")

for p in profit_losses:

    if min== 0:
     max == p
     min == p
    if p > max:
     max = p
    elif p < min:
     min = p

max_index = profit_losses.index(max)
min_index = profit_losses.index(min)

max_date = dates[max_index]
min_date = dates[min_index]

print (f"Greatest Increase in Profits: {max_date} (${max})")
print (f"Greatest Decrease in Profits: {min_date} (${min})")


text_file = "/Users/jassjones/cwru-cle-virt-data-pt-07-2021-u-c/Homework/03-Python/PyBank/Analysis/text_file.txt"
with open (text_file, 'w') as  text:

     text.write('Financial Analysis')
     text.write('\n-----------------------------')
     text.write(f'\nTotal Months: {months}')
     text.write(f'\nTotal: ${net_total}')
     text.write(f'\nAverage Change: ${average}')
     text.write(f'\nGreatest Increase in Profits: {max_date} (${max})')
     text.write(f'\nGreatest Decrease in Profits: {min_date} (${min})')