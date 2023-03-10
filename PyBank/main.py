# This script is written in VS Code
import csv
# CSV file is in Resources folder in PyBank folder
file_path = r"PyBank\Resources\budget_data.csv"

with open(file_path, "r", encoding="utf-8") as csv_file:
    content = csv.reader(csv_file, delimiter=",")
    # Storing header
    header = next(content)
    
    # Creating tuples for month values and profit/loss values and storing them under respective variables
    month, profit_loss = zip(*list(content))

print("Financial Analysis")
print("-"*25)
   
# For a count of total months we just need the total number of items in month tuple
total_months = len(month)
print(f"Total Months: {total_months}")
    
# Converting the profit_loss tuple into list with int values and to find the total profit or loss we just need the sum of all iems in profit_loss
profit_loss = [int(i) for i in profit_loss]
total_profit_loss = sum((profit_loss))
print(f"Total: ${total_profit_loss}")
     
# Calculating profit or loss from previous month over entire period and storing the values as a list
monthly_profit_loss_change = [profit_loss[i+1] - profit_loss[i] for i in range(len(profit_loss)-1)]
    
# Calculating the average of these monthly profit/loss change
avg_profit_loss_change = round(sum(monthly_profit_loss_change)/len(monthly_profit_loss_change),2)
print(f"Average Change: ${avg_profit_loss_change}")
   
# To calculate the greatest increase in profit over entire period, we need to find the max value in monthly changes
max_change = max(monthly_profit_loss_change)
# To find the corresponding month for a greatest increase in profit we can find index of max value and then return the month value from months tuple based on index
index_max_value = monthly_profit_loss_change.index(max_change)
max_month = month[index_max_value + 1]
print(f"Greatest Increase in Profits: {max_month} (${max_change})")

# To calculate the greatest decrease in profit over entire period, we need to find the min value in monthly changes
min_change = min(monthly_profit_loss_change)
# To find the corresponding month for a greatest decrease in profit we can find index of min value and then return the month value from months tuple based on index
index_min_value = monthly_profit_loss_change.index(min_change)
min_month = month[index_min_value + 1]
print(f"Greatest Decrease in Profits: {min_month} (${min_change})")

# Exporting the analysis to a text file
with open(r"PyBank\Analysis\analysis.txt", "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("-"*25 + "\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${total_profit_loss}\n")
    txt_file.write(f"Average Change: ${avg_profit_loss_change}\n")
    txt_file.write(f"Greatest Increase in Profits: {max_month} (${max_change})\n")
    txt_file.write(f"Greatest Decrease in Profits: {min_month} (${min_change})")
