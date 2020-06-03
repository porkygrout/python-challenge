import os
import csv
fh = open ('financial_analysis.txt', 'w')
bank_csv = ".../Resources/budget_data.csv"
with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvfile)
    print("Financial Analysis")
    fh.write("Financial Analysis \n")
    print("------------------------------")
    fh.write("------------------------------ \n")
    months = sum(1 for row in bank_csv)
    print(f"Total months: {months}")
    fh.write(f"Total months: {months} \n")
    total = sum(float(row[1]) for row in csvreader)
    print(f"Total: ${total}0")
    fh.write(f"Total: ${total}0 \n")
    average = round(total/months,2)
    print(f"Average change: ${average}")
    fh.write(f"Average change: ${average}\n")


with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    answer = max(int(column[1].replace(',', '')) for column in csvreader)
    print(f"Greatest increase in profits: ${answer}.00")
    fh.write(f"Greatest increase in profits: ${answer}.00\n")
with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)    
    answer1 = min(int(column[1].replace(',', '')) for column in csvreader) 
    print(f"Greatest Decrease in Profits: ${answer1}.00")
    fh.write(f"Greatest Decrease in Profits: ${answer1}.00\n")
fh.close()