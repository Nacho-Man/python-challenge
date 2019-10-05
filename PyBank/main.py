import os
import csv

# set the path
budget_data_csv = os.path.join('..', 'Resources.csv')

#Create variables
total_revenue = 0
month_count = 0
current_month_revenue = 0
prior_month_revenue = 0
revenue_change = 0
revenue_changes = []
months = []

# open the budget_data.csv and read rows
with open(budget_data_csv, newline="") as csvfile:
   csvreader = csv.DictReader(csvfile, delimiter=",")
   #print(csvreader)
   
   for row in csvreader:
        month_count = month_count + 1
        months.append(row["Date"])
        current_month_revenue = int(row["Profit/Losses"])
        total_revenue = total_revenue + current_month_revenue
        if month_count > 1 :
            revenue_change = current_month_revenue - prior_month_revenue
            revenue_changes.append(revenue_change)
        prior_month_revenue = current_month_revenue
     
# Month by month analysis
sum_revenue_changes = sum(revenue_changes)
average_change = round(sum_revenue_changes/(month_count - 1), 2)
max_change = max(revenue_changes)
min_change = min(revenue_changes)
max_month_index = revenue_changes.index(max_change) + 1
min_month_index = revenue_changes.index(min_change)
max_month = months[max_month_index ]
min_month = months[min_month_index ]

# print the finanacial analysis
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {month_count} ")
print(f"Total Revenue: ${total_revenue}")
print(f"Average Revenue Change: ${average_change}")
print(f"Greatest Increase in profits: {max_month} (${max_change})")
print(f"Greatest Decrease in profits: {min_month} (${min_change})")
# write it to a text file
# 
# #write it to a text file
output_path= os.path.join("PyBank_output.txt")
# open the file
with open (output_path, 'w', newline='') as txtfile:
     # write rows
     txtwriter = txtfile.write("Financial Analysis\n")
     txtwriter = txtfile.write("-----------------------\n")
     txtwriter = txtfile.write(f"Total Months: {month_count}\n")
     txtwriter = txtfile.write(f"Total: ${total_revenue}\n")
     txtwriter = txtfile.write(f"Average change ${round(float(average_change))}\n")
     txtwriter = txtfile.write(f"Greatest increase in profits: {max_month} (${max_change})\n")
     txtwriter = txtfile.write(f"Greatest decrease in profits: {min_change} (${min_change})")