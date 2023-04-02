import csv

# Define the input file name
input_file = "../resources/budget_data.csv"

# Define variables to store the calculated values
total_months = 0
net_total_amount = 0
previous_month_amount = None
profit_changes = []
greatest_increase = {"amount": 0, "date": ""}
greatest_decrease = {"amount": 0, "date": ""}

# Open the input file and read the data 
with open(input_file, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  # Skip the header row

    # Loop through each row of data
    for row in csvreader:
        # Extract the month and amount values from the current row
        month = row[0]
        amount = int(row[1])

        # Increment the total number of months
        total_months += 1

        # Add the current amount to the net total amount
        net_total_amount += amount

        # Calculate the profit change from the previous month (if there is one)
        if previous_month_amount is not None:
            profit_change = amount - previous_month_amount
            profit_changes.append(profit_change)

            # Check if the current profit change is the greatest increase or decrease
            if profit_change > greatest_increase["amount"]:
                greatest_increase["amount"] = profit_change
                greatest_increase["date"] = month
            elif profit_change < greatest_decrease["amount"]:
                greatest_decrease["amount"] = profit_change
                greatest_decrease["date"] = month

        # Save the current amount as the previous month's amount for the next iteration
        previous_month_amount = amount

# Calculate the average of the profit changes
average_change = sum(profit_changes) / len(profit_changes)

# Print the calculated values
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")


with open('financial_analysis.txt', 'w') as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${net_total_amount}\n")
    textfile.write(f"Average Change: ${average_change}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")