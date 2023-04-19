# Importing modules
import os
import csv

# Creating input path for csv file
budget_data_csv = os.path.join('Resources','budget_data.csv')

# Defining tracking variables to start at 0
total_months = 0
total_net = 0
total_net_change = 0

# Opening list to save individual monthly Profit/Loss net changes
net_change_list = []

# Opening list to save printed results in list
print_result = []

# Opening csv file to read as csv file
with open(budget_data_csv, "r", encoding="utf-8") as csvfile:

    # Reading csv file with "," as delimiter
    csvreader = csv.reader(csvfile,delimiter=",")
    
    # Pulling out header row
    csv_header = next(csvreader)
       
    # Converting csv file to a list minus header
    budget_data_list = list(csvreader)
    
# Setting "previous_row" variable as the first Profit/Loss figure in data set
# This will act as the starting point to calculate net changes
# Wrapped as integer for calculation
previous_row = int(budget_data_list[0][1])

# For loop to run through all rows of the list  
for row in budget_data_list:
       
    # Defining profit_loss variable
    # Profit/Loss value is index 1 of each row
    profit_loss = int(row[1])
    
    # Defining total_month to increase by 1 every loop to track the number of months
    total_months = total_months + 1

    # Defining total_net to increase by the Profit/Loss value every loop
    # This calculation will sum to the total net amount of Profit/Loss
    total_net = total_net + profit_loss
    
    # Net change calculation
    # Current row Profit/Loss minus the Profit/Loss saved from the previous row
    net_change = profit_loss - previous_row
    
    # Adding the new net_change calculation to list
    net_change_list.append(net_change)
    
    # Overriding the previous row Profit/Loss figure with the current Profit/Loss figure
    # When next loop is run this will become the previous row for net change calculation
    previous_row = profit_loss
    
    # Defining total_net_change to increase by the current net_change with every loop
    # This calculation will sum the total net monthly changes
    total_net_change = total_net_change + net_change
    

# Calulating the average monhtly net change in Profit/Loss
# Subtracting 1 month from total months as there is no net change in the first month
# Wrapped to round to 2 decimal places
average_net_change = round(total_net_change/(total_months-1),2)

# Variable to identifying the highest and lowest net_change in list
max_increase = max(net_change_list)
max_decrease = min(net_change_list)

# Variable to identify the index value for the maximum increase and maximum decrease in list
max_index = int(net_change_list.index(max_increase))
min_index = int(net_change_list.index(max_decrease))

# Using the above index to identify the corresponding date of maximum increase and maximum decrease
# Budget_data_list is nested, "Date" is held in index 0 of each nest
max_date = (budget_data_list[max_index][0])
min_date = (budget_data_list[min_index][0])


# Print commands to output analysis result
# Add output to print_result list for txt file printing
print("Financial Analysis")
print_result.append("Financial Analysis")
print("----------------------------")
print_result.append("----------------------------")
print(f"Total Months: {total_months}")
print_result.append(f"Total Months: {total_months}")
print(f"Total: ${total_net}")
print_result.append(f"Total: ${total_net}")
print(f"Average Change: ${average_net_change}")
print_result.append(f"Average Change: ${average_net_change}")
print(f"Greatest Increase in Profits: {max_date} (${max_increase})")
print_result.append(f"Greatest Increase in Profits: {max_date} (${max_increase})")
print(f"Greatest Decrease in Profits: {min_date} (${max_decrease})")
print_result.append(f"Greatest Decrease in Profits: {min_date} (${max_decrease})")

# Creating output path for Results text file
output_path = os.path.join("Analysis","Results.txt")

# Printing output analysis results from list into a text file

with open(output_path,"w") as txtfile:
    for lines in print_result:
        txtfile.write(lines+"\n")
txtfile.close()