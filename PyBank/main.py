#getting modules
import os
import csv

#settting path
budget_data_csv=os.path.join('Desktop','python_challenge','PyBank','Resources','budget_data.csv')

#opening csv file
with open(budget_data_csv) as csvfile:

    #reading csv file
    csvreader = csv.reader(csvfile, delimiter=',')

    #printing csv file
    print(csvreader)

    #reading header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #setting variables
    total_months = []
    net_total = 0
    profit_loss = []
    changes = []    
    max_changes = None
    max_increase = 0  
    months=[]  

    #reading csv file
    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))

        # Calculate the total number of months
        total_months = len(months)

        # Calculate the net total amount of profit/losses
        net_total = sum(profit_loss)

        # Calculate the changes in profit/losses and store them in a list
for i in range(1, total_months):
        change = profit_loss[i] - profit_loss[i-1]
        changes.append(change)

        # Calculate average change
        average_change = sum(changes) / len(changes)

        # Find the month of the maximum change
        greatest_increase = max(changes)
        greatest_increase_date = months[changes.index(greatest_increase) + 1]
        greatest_decrease= min(changes)
        greatest_decrease_date = months[changes.index(greatest_decrease) + 1]   

#printing results           
print("Financial Analysis")
print("-----------------------------")
print(f"Total months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})") 

#writing to text file
# Set variable for output file
output_file = os.path.join('Desktop','python_challenge','PyBank','Resources','budget_data.txt')
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Financial Analysis"])
    writer.writerow(["-----------------------------"])

    # Write in zipped rows
    writer.writerow([f"Total months: {total_months}"])
    writer.writerow([f"Total: ${net_total}"])
    writer.writerow([f"Average Change: ${average_change}"])
    writer.writerow([f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})"])
    writer.writerow([f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"])